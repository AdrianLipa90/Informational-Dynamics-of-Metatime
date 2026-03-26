
# -*- coding: utf-8 -*-
"""
Feature-gated mixture over K categorical models.
P_final(b) = sum_k softmax(W x f)_k * P_k(b)
Weights W learned online via gradient descent on log-loss.
"""

from typing import List, Dict
import math

def softmax(xs: List[float]) -> List[float]:
    m = max(xs)
    ex = [math.exp(x - m) for x in xs]
    s = sum(ex)
    return [e/s for e in ex]

class GatedMixture:
    def __init__(self, K: int, F: int, lr: float = 0.05, l2: float = 1e-5):
        self.K, self.F = K, F
        # weights W is K x (F+1) including bias
        self.W = [ [0.0]*(F+1) for _ in range(K) ]
        self.lr = float(lr)
        self.l2 = float(l2)

    def _gate(self, feats: List[float]) -> List[float]:
        x = [1.0] + feats  # bias + features
        logits = [ sum(w_i * x_i for w_i, x_i in zip(w, x)) for w in self.W ]
        return softmax(logits)

    def mix(self, models_probs: List[List[float]], feats: List[float]) -> List[float]:
        g = self._gate(feats)  # K weights
        # weighted sum of categorical distributions (length 256)
        P = [0.0]*256
        for k, pk in enumerate(models_probs):
            gk = g[k]
            for b in range(256):
                P[b] += gk * pk[b]
        # numerical hygiene: normalize
        s = sum(P)
        if s <= 0.0:
            P = [1.0/256.0]*256
        else:
            P = [p/s for p in P]
        return P, g

    def update(self, models_probs: List[List[float]], feats: List[float], true_byte: int):
        # gradients wrt W via chain rule
        P, g = self.mix(models_probs, feats)
        # loss = -log P[true_byte]
        # derivative w.r.t gating logits is (dL/dg) * (dg/dlogits)
        # For mixture, dL/dg_k = sum_b dL/dP_b * dP_b/dg_k = - (P_k(true)/P_true)
        # where P_k(true) = models_probs[k][true]
        pt = max(P[true_byte], 1e-12)
        Pk_true = [mp[true_byte] for mp in models_probs]
        dL_dg = [ -(pk/pt) for pk in Pk_true ]

        # softmax Jacobian: d g_i / d z_j = g_i (delta_ij - g_j)
        # dL/dz_j = sum_i dL/dg_i * g_i (delta_ij - g_j)
        dL_dz = []
        for j in range(self.K):
            acc = 0.0
            for i in range(self.K):
                acc += dL_dg[i] * g[i] * ((1.0 if i == j else 0.0) - g[j])
            dL_dz.append(acc)

        x = [1.0] + feats
        # L2 regularization
        for j in range(self.K):
            for t in range(self.F+1):
                grad = dL_dz[j] * x[t] + self.l2 * self.W[j][t]
                self.W[j][t] -= self.lr * grad
