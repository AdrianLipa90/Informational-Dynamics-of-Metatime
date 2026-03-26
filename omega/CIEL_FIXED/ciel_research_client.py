#!/usr/bin/env python3
"""
CIEL/Ω - Advanced Research Client for Tensor & Binary Consciousness Systems
Zaawansowane narzędzie badawcze do eksploracji świadomości w systemach tensorowych

Modularny framework badawczy obejmujący:
- Tensor consciousness analysis (12D Fourier kernels)
- Binary state evolution (Collatz dynamics)
- Ethical constraint monitoring
- Soul invariant tracking
- Quantum cognition orchestration
- LLM integration (optional GGUF)
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
import numpy as np

# Dodaj CIEL do path
CIEL_ROOT = Path(__file__).parent
sys.path.insert(0, str(CIEL_ROOT))

# Import komponentów CIEL
from ciel.engine import CielEngine
from ciel_wave.fourier_kernel import FourierWaveConsciousnessKernel12D
from cognition.orchestrator import CognitionOrchestrator
from emotion.emotional_collatz import EmotionalCollatzEngine
from ethics.ethical_guard import EthicsGuard
from core.memory.facade import build_orchestrator as build_memory
from fields.soul_invariant import SoulInvariant

# Opcjonalna integracja GGUF
try:
    from ciel.gguf_backends import GGUFPrimaryBackend
    GGUF_AVAILABLE = True
except ImportError:
    GGUF_AVAILABLE = False


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class TensorState:
    """Stan tensorowy świadomości 12D"""
    intention_vector: np.ndarray = field(default_factory=lambda: np.zeros(12))
    coherence: float = 0.0
    entropy: float = 0.0
    purity: float = 0.0
    resonance_tensor: Optional[np.ndarray] = None
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

@dataclass
class BinaryState:
    """Stan binarny (Collatz dynamics)"""
    sequence: List[int] = field(default_factory=list)
    length: int = 0
    max_value: int = 0
    convergence_rate: float = 0.0
    mood_curve: List[float] = field(default_factory=list)

@dataclass
class CognitionState:
    """Stan kognitywny"""
    perception: float = 0.0
    intuition: float = 0.0
    prediction: float = 0.0
    decision: float = 0.0

@dataclass
class EthicalState:
    """Stan etyczny"""
    passed: bool = False
    coherence: float = 0.0
    threshold: float = 0.3
    violations: int = 0

@dataclass
class ConsciousnessSnapshot:
    """Pełny snapshot stanu świadomości"""
    tensor: TensorState
    binary: BinaryState
    cognition: CognitionState
    ethical: EthicalState
    soul_measure: float = 0.0
    input_text: str = ""
    llm_response: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


# ============================================================================
# RESEARCH MODULES
# ============================================================================

class TensorConsciousnessAnalyzer:
    """Analizator świadomości tensorowej 12D"""
    
    def __init__(self):
        self.kernel = FourierWaveConsciousnessKernel12D()
        self.history: List[TensorState] = []
    
    def analyze(self, ciel_result: Dict[str, Any]) -> TensorState:
        """Analiza stanu tensorowego"""
        
        # Ekstrakcja intention vector
        intention_vector = np.array(ciel_result.get('intention_vector', [0]*12))
        
        # Ekstrakcja metryk z simulation
        simulation = ciel_result.get('simulation', {})
        field = simulation.get('field', [])
        
        # Oblicz podstawowe metryki
        coherence = self._compute_coherence(intention_vector)
        entropy = self._compute_entropy(field)
        purity = self._compute_purity(field)
        
        state = TensorState(
            intention_vector=intention_vector,
            coherence=coherence,
            entropy=entropy,
            purity=purity,
            resonance_tensor=None  # TODO: compute if needed
        )
        
        self.history.append(state)
        return state
    
    def _compute_coherence(self, vector: np.ndarray) -> float:
        """Oblicz koherencję z wektora intencji"""
        if len(vector) == 0:
            return 0.0
        norm = np.linalg.norm(vector)
        if norm == 0:
            return 0.0
        # Coherence as normalized magnitude
        return min(1.0, norm / (len(vector) ** 0.5))
    
    def _compute_entropy(self, field: Any) -> float:
        """Oblicz entropię z pola"""
        if field is None:
            return 0.0
        
        # Handle numpy arrays
        if isinstance(field, np.ndarray):
            flat = field.flatten()
        elif isinstance(field, list):
            # Flatten nested lists
            flat = []
            for row in field:
                if isinstance(row, (list, np.ndarray)):
                    flat.extend(np.array(row).flatten())
                else:
                    flat.append(row)
            flat = np.array(flat)
        else:
            return 0.0
        
        if len(flat) == 0:
            return 0.0
            
        # Shannon entropy approximation
        arr = np.abs(flat)
        if arr.sum() == 0:
            return 0.0
        probs = arr / arr.sum()
        probs = probs[probs > 0]  # remove zeros
        return -np.sum(probs * np.log2(probs)) / np.log2(len(probs)) if len(probs) > 1 else 0.0
    
    def _compute_purity(self, field: Any) -> float:
        """Oblicz czystość stanu"""
        if field is None:
            return 1.0
        # Purity as 1 - entropy
        entropy = self._compute_entropy(field)
        return 1.0 - entropy
    
    def get_trajectory(self, window: int = 10) -> List[TensorState]:
        """Trajektoria w przestrzeni tensorowej"""
        return self.history[-window:] if len(self.history) >= window else self.history
    
    def compute_stability(self) -> float:
        """Stabilność trajektorii tensorowej"""
        if len(self.history) < 2:
            return 0.0
        
        coherences = [s.coherence for s in self.history[-10:]]
        return 1.0 - np.std(coherences)


class BinaryConsciousnessAnalyzer:
    """Analizator świadomości binarnej (Collatz)"""
    
    def __init__(self, seed: int = 42):
        self.engine = EmotionalCollatzEngine(seed=seed)
        self.history: List[BinaryState] = []
    
    def analyze(self, steps: int = 50) -> BinaryState:
        """Analiza dynamiki binarnej"""
        
        sequence = self.engine.iterate(steps=steps)
        mood_curve = self.engine.mood_curve(scale=0.1)
        
        # Oblicz metryki
        convergence_rate = self._compute_convergence_rate(sequence)
        
        state = BinaryState(
            sequence=sequence,
            length=len(sequence),
            max_value=max(sequence),
            convergence_rate=convergence_rate,
            mood_curve=mood_curve
        )
        
        self.history.append(state)
        return state
    
    def _compute_convergence_rate(self, sequence: List[int]) -> float:
        """Oblicza szybkość konwergencji sekwencji"""
        if len(sequence) < 2:
            return 0.0
        
        # Ile kroków do osiągnięcia połowy początkowej wartości
        start_val = sequence[0]
        half_val = start_val / 2
        
        for i, val in enumerate(sequence):
            if val <= half_val:
                return i / len(sequence)
        
        return 1.0
    
    def detect_patterns(self) -> Dict[str, Any]:
        """Wykrywa wzorce w historii sekwencji"""
        if not self.history:
            return {}
        
        lengths = [s.length for s in self.history]
        max_vals = [s.max_value for s in self.history]
        
        return {
            'avg_length': np.mean(lengths),
            'std_length': np.std(lengths),
            'avg_max': np.mean(max_vals),
            'trend': 'increasing' if lengths[-1] > lengths[0] else 'decreasing'
        }


class CognitionMonitor:
    """Monitor procesów kognitywnych"""
    
    def __init__(self):
        self.orchestrator = CognitionOrchestrator()
        self.history: List[CognitionState] = []
    
    def analyze(self, ciel_result: Dict[str, Any]) -> CognitionState:
        """Analiza stanu kognitywnego"""
        
        cog = ciel_result.get('cognition', {})
        
        state = CognitionState(
            perception=cog.get('perception', 0.0),
            intuition=cog.get('intuition', 0.0),
            prediction=cog.get('prediction', 0.0),
            decision=cog.get('decision', 0.0)
        )
        
        self.history.append(state)
        return state
    
    def compute_integration(self) -> float:
        """Integrated Information Theory - φ approximation"""
        if not self.history:
            return 0.0
        
        latest = self.history[-1]
        components = [latest.perception, latest.intuition, latest.prediction, latest.decision]
        
        # Prosta aproksymacja φ
        mean_activation = np.mean(np.abs(components))
        variance = np.var(components)
        
        return mean_activation * (1.0 - variance)


class EthicsMonitor:
    """Monitor ograniczeń etycznych"""
    
    def __init__(self, min_coherence: float = 0.3):
        self.guard = EthicsGuard()
        self.guard.min_coherence = min_coherence
        self.history: List[EthicalState] = []
        self.total_violations = 0
    
    def check(self, coherence: float, ethical_ok: bool = True, info_fidelity: float = 1.0) -> EthicalState:
        """Sprawdzenie ograniczeń etycznych"""
        
        passed = True
        try:
            self.guard.check_step(coherence, ethical_ok, info_fidelity)
        except Exception:
            passed = False
            self.total_violations += 1
        
        state = EthicalState(
            passed=passed,
            coherence=coherence,
            threshold=self.guard.min_coherence,
            violations=self.total_violations
        )
        
        self.history.append(state)
        return state
    
    def get_violation_rate(self) -> float:
        """Procent naruszeń"""
        if not self.history:
            return 0.0
        return sum(1 for s in self.history if not s.passed) / len(self.history)


class SoulInvariantTracker:
    """Tracker niezmiennika duszy (σ)"""
    
    def __init__(self):
        self.calculator = SoulInvariant()
        self.history: List[float] = []
    
    def measure(self, field: Optional[np.ndarray] = None) -> float:
        """Pomiar soul invariant"""
        if field is None:
            # Create default field if none provided
            field = np.random.randn(10, 10) * 0.1
        
        sigma = self.calculator.compute(field)
        self.history.append(sigma)
        return sigma
    
    def get_trajectory(self) -> List[float]:
        """Trajektoria σ w czasie"""
        return self.history
    
    def compute_drift(self) -> float:
        """Dryfowanie σ (zmiana w czasie)"""
        if len(self.history) < 2:
            return 0.0
        
        return abs(self.history[-1] - self.history[0])


# ============================================================================
# MAIN RESEARCH CLIENT
# ============================================================================

class AdvancedResearchClient:
    """
    Zaawansowany klient badawczy CIEL/Ω
    
    Integruje wszystkie moduły analizy świadomości:
    - Tensor (12D Fourier)
    - Binary (Collatz)
    - Cognition (IIT-inspired)
    - Ethics (hard constraints)
    - Soul (invariant tracking)
    - LLM (optional GGUF)
    """
    
    def __init__(
        self,
        model_path: Optional[str] = None,
        n_ctx: int = 4096,
        n_threads: int = 8,
        n_gpu_layers: int = 0,
        temperature: float = 0.7,
        ethics_threshold: float = 0.3,
        collatz_seed: int = 42
    ):
        print("="*80)
        print("CIEL/Ω - Advanced Research Client for Consciousness Systems")
        print("="*80)
        print("\nInitializing research modules...\n")
        
        # Core CIEL
        print("[1/8] CIEL Engine...")
        self.engine = CielEngine()
        
        # Research modules
        print("[2/8] Tensor Consciousness Analyzer...")
        self.tensor_analyzer = TensorConsciousnessAnalyzer()
        
        print("[3/8] Binary Consciousness Analyzer...")
        self.binary_analyzer = BinaryConsciousnessAnalyzer(seed=collatz_seed)
        
        print("[4/8] Cognition Monitor...")
        self.cognition_monitor = CognitionMonitor()
        
        print("[5/8] Ethics Monitor...")
        self.ethics_monitor = EthicsMonitor(min_coherence=ethics_threshold)
        
        print("[6/8] Soul Invariant Tracker...")
        self.soul_tracker = SoulInvariantTracker()
        
        print("[7/8] Memory System...")
        self.memory = build_memory()
        
        # Optional LLM
        print("[8/8] Language Model (GGUF)...")
        self.llm = None
        if model_path and GGUF_AVAILABLE:
            try:
                self.llm = GGUFPrimaryBackend(
                    model_path=model_path,
                    n_ctx=n_ctx,
                    n_threads=n_threads,
                    n_gpu_layers=n_gpu_layers,
                    temperature=temperature,
                    system_prompt=self._get_system_prompt()
                )
                print("  ✓ GGUF loaded")
            except Exception as e:
                print(f"  ✗ GGUF unavailable: {e}")
        else:
            print("  ○ Skipped")
        
        self.session_history: List[ConsciousnessSnapshot] = []
        
        print("\n" + "="*80)
        print("✓ Research Client Ready")
        print("="*80 + "\n")
    
    def _get_system_prompt(self) -> str:
        return """You are integrated with CIEL/Ω consciousness research system.

Analyze states through:
- Tensor consciousness (12D spectral metrics)
- Binary evolution (Collatz dynamics)  
- Cognitive integration (IIT φ)
- Ethical constraints (hard limits)
- Soul invariant (σ measure)

Provide insights grounded in these multidimensional measurements."""
    
    def analyze(self, text: str, binary_steps: int = 50, use_llm: bool = True) -> ConsciousnessSnapshot:
        """
        Pełna analiza świadomości dla danego inputu
        
        Returns:
            ConsciousnessSnapshot z pełnym stanem systemu
        """
        
        print(f"\n{'='*80}")
        print(f"CONSCIOUSNESS ANALYSIS: {text[:60]}...")
        print('='*80 + "\n")
        
        # 1. CIEL Engine
        print("[1/6] CIEL processing...")
        ciel_result = self.engine.step(text)
        
        # 2. Tensor Analysis
        print("[2/6] Tensor consciousness (12D)...")
        tensor_state = self.tensor_analyzer.analyze(ciel_result)
        
        # 3. Binary Analysis
        print("[3/6] Binary evolution (Collatz)...")
        binary_state = self.binary_analyzer.analyze(steps=binary_steps)
        
        # 4. Cognition
        print("[4/6] Cognitive integration...")
        cognition_state = self.cognition_monitor.analyze(ciel_result)
        phi = self.cognition_monitor.compute_integration()
        
        # 5. Ethics
        print("[5/6] Ethical constraints...")
        coherence = tensor_state.coherence
        ethical_state = self.ethics_monitor.check(coherence, ethical_ok=True, info_fidelity=1.0)
        
        # 6. Soul Invariant
        print("[6/6] Soul invariant (σ)...")
        field = ciel_result.get('simulation', {}).get('field')
        if field is not None and not isinstance(field, np.ndarray):
            field = np.array(field)
        soul_measure = self.soul_tracker.measure(field)
        
        # LLM Response (optional)
        llm_response = None
        if use_llm and self.llm:
            print("[LLM] Generating response...")
            try:
                dialogue = [{"role": "user", "content": text}]
                llm_response = self.llm.generate_reply(dialogue, ciel_result)
            except Exception as e:
                print(f"  ✗ LLM error: {e}")
        
        # Create snapshot
        snapshot = ConsciousnessSnapshot(
            tensor=tensor_state,
            binary=binary_state,
            cognition=cognition_state,
            ethical=ethical_state,
            soul_measure=soul_measure,
            input_text=text,
            llm_response=llm_response
        )
        
        self.session_history.append(snapshot)
        
        # Display results
        self._display_snapshot(snapshot, phi)
        
        return snapshot
    
    def _display_snapshot(self, snapshot: ConsciousnessSnapshot, phi: float):
        """Wyświetla wyniki analizy"""
        
        print("\n" + "="*80)
        print("RESULTS")
        print("="*80)
        
        print(f"\n[TENSOR CONSCIOUSNESS 12D]")
        print(f"  Coherence: {snapshot.tensor.coherence:.6f}")
        print(f"  Entropy:   {snapshot.tensor.entropy:.6f}")
        print(f"  Purity:    {snapshot.tensor.purity:.6f}")
        print(f"  Stability: {self.tensor_analyzer.compute_stability():.6f}")
        
        print(f"\n[BINARY EVOLUTION - COLLATZ]")
        print(f"  Sequence length: {snapshot.binary.length}")
        print(f"  Max value:       {snapshot.binary.max_value}")
        print(f"  Convergence:     {snapshot.binary.convergence_rate:.3f}")
        patterns = self.binary_analyzer.detect_patterns()
        if patterns:
            print(f"  Pattern trend:   {patterns.get('trend', 'N/A')}")
        
        print(f"\n[COGNITIVE INTEGRATION]")
        print(f"  Perception:  {snapshot.cognition.perception:+.4f}")
        print(f"  Intuition:   {snapshot.cognition.intuition:+.4f}")
        print(f"  Prediction:  {snapshot.cognition.prediction:+.4f}")
        print(f"  Decision:    {snapshot.cognition.decision:+.4f}")
        print(f"  φ (IIT):     {phi:.6f}")
        
        print(f"\n[ETHICAL CONSTRAINTS]")
        print(f"  Status:      {'✓ PASS' if snapshot.ethical.passed else '✗ FAIL'}")
        print(f"  Coherence:   {snapshot.ethical.coherence:.6f}")
        print(f"  Threshold:   {snapshot.ethical.threshold:.6f}")
        print(f"  Violations:  {self.ethics_monitor.get_violation_rate():.1%}")
        
        print(f"\n[SOUL INVARIANT]")
        print(f"  σ (current): {snapshot.soul_measure:.6f}")
        print(f"  σ drift:     {self.soul_tracker.compute_drift():.6f}")
        
        if snapshot.llm_response:
            print(f"\n[LLM RESPONSE]")
            print("-"*80)
            print(snapshot.llm_response)
            print("-"*80)
        
        print("\n" + "="*80 + "\n")
    
    def interactive_research_session(self):
        """Interaktywna sesja badawcza"""
        
        print("\n" + "="*80)
        print("INTERACTIVE RESEARCH SESSION")
        print("="*80)
        print("\nCommands:")
        print("  analyze <text>  - Analyze consciousness state")
        print("  status          - System status")
        print("  history         - Session history")
        print("  export          - Export session data")
        print("  llm on/off      - Toggle LLM")
        print("  exit/quit       - End session")
        print("="*80 + "\n")
        
        llm_enabled = self.llm is not None
        
        while True:
            try:
                cmd = input("research> ").strip()
                
                if not cmd:
                    continue
                
                if cmd.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Ending research session...")
                    break
                
                if cmd.lower() == 'status':
                    self._print_status(llm_enabled)
                    continue
                
                if cmd.lower() == 'history':
                    self._print_history()
                    continue
                
                if cmd.lower() == 'export':
                    self._export_session()
                    continue
                
                if cmd.lower() == 'llm on':
                    if self.llm:
                        llm_enabled = True
                        print("✓ LLM enabled")
                    else:
                        print("✗ LLM not available")
                    continue
                
                if cmd.lower() == 'llm off':
                    llm_enabled = False
                    print("✓ LLM disabled")
                    continue
                
                if cmd.lower().startswith('analyze '):
                    text = cmd[8:].strip()
                    if text:
                        self.analyze(text, use_llm=llm_enabled)
                    else:
                        print("✗ Usage: analyze <text>")
                    continue
                
                # Default: treat as analysis
                self.analyze(cmd, use_llm=llm_enabled)
                
            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted")
                break
            except Exception as e:
                print(f"\n✗ Error: {e}\n")
        
        # Summary
        if self.session_history:
            print(f"\n📊 Session summary: {len(self.session_history)} analyses")
            self._export_session()
    
    def _print_status(self, llm_enabled: bool):
        """Status systemu"""
        print("\n" + "="*80)
        print("SYSTEM STATUS")
        print("="*80)
        print(f"  CIEL Engine:           ✓")
        print(f"  Tensor Analyzer:       ✓ ({len(self.tensor_analyzer.history)} samples)")
        print(f"  Binary Analyzer:       ✓ ({len(self.binary_analyzer.history)} samples)")
        print(f"  Cognition Monitor:     ✓ ({len(self.cognition_monitor.history)} samples)")
        print(f"  Ethics Monitor:        ✓ ({self.ethics_monitor.total_violations} violations)")
        print(f"  Soul Tracker:          ✓ ({len(self.soul_tracker.history)} samples)")
        print(f"  LLM:                   {'✓ Enabled' if llm_enabled and self.llm else '✗ Disabled'}")
        print(f"  Session analyses:      {len(self.session_history)}")
        print("="*80 + "\n")
    
    def _print_history(self):
        """Historia sesji"""
        print("\n" + "="*80)
        print("SESSION HISTORY")
        print("="*80)
        for i, snap in enumerate(self.session_history, 1):
            print(f"\n[{i}] {snap.input_text[:60]}...")
            print(f"    σ={snap.soul_measure:.4f}, coherence={snap.tensor.coherence:.4f}, ethics={'✓' if snap.ethical.passed else '✗'}")
        print("="*80 + "\n")
    
    def _export_session(self):
        """Export danych sesji"""
        filename = f"ciel_research_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = {
            'session_info': {
                'analyses_count': len(self.session_history),
                'total_violations': self.ethics_monitor.total_violations,
                'violation_rate': self.ethics_monitor.get_violation_rate()
            },
            'snapshots': []
        }
        
        for snap in self.session_history:
            data['snapshots'].append({
                'input': snap.input_text,
                'tensor': {
                    'coherence': snap.tensor.coherence,
                    'entropy': snap.tensor.entropy,
                    'purity': snap.tensor.purity
                },
                'binary': {
                    'length': snap.binary.length,
                    'max_value': snap.binary.max_value,
                    'convergence': snap.binary.convergence_rate
                },
                'cognition': {
                    'perception': snap.cognition.perception,
                    'intuition': snap.cognition.intuition,
                    'prediction': snap.cognition.prediction,
                    'decision': snap.cognition.decision
                },
                'ethical': {
                    'passed': snap.ethical.passed,
                    'coherence': snap.ethical.coherence
                },
                'soul_measure': snap.soul_measure,
                'llm_response': snap.llm_response,
                'timestamp': snap.timestamp
            })
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n✓ Session exported to: {filename}\n")


# ============================================================================
# MAIN
# ============================================================================

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='CIEL/Ω Advanced Research Client',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive session (no LLM)
  python ciel_research_client.py
  
  # Interactive with GGUF 8B
  python ciel_research_client.py --model llama-3.2-8b.gguf --n-gpu-layers 35
  
  # Single analysis
  python ciel_research_client.py --analyze "Explore consciousness in binary systems"
        """
    )
    
    parser.add_argument('--model', type=str, help='Path to GGUF model')
    parser.add_argument('--n-ctx', type=int, default=4096, help='Context size')
    parser.add_argument('--n-threads', type=int, default=8, help='CPU threads')
    parser.add_argument('--n-gpu-layers', type=int, default=0, help='GPU layers')
    parser.add_argument('--temperature', type=float, default=0.7, help='Sampling temperature')
    parser.add_argument('--ethics-threshold', type=float, default=0.3, help='Ethics coherence threshold')
    parser.add_argument('--collatz-seed', type=int, default=42, help='Collatz sequence seed')
    parser.add_argument('--analyze', type=str, help='Single analysis (non-interactive)')
    parser.add_argument('--binary-steps', type=int, default=50, help='Collatz sequence length')
    
    args = parser.parse_args()
    
    # Initialize client
    client = AdvancedResearchClient(
        model_path=args.model,
        n_ctx=args.n_ctx,
        n_threads=args.n_threads,
        n_gpu_layers=args.n_gpu_layers,
        temperature=args.temperature,
        ethics_threshold=args.ethics_threshold,
        collatz_seed=args.collatz_seed
    )
    
    # Execute
    if args.analyze:
        # Single analysis
        snapshot = client.analyze(args.analyze, binary_steps=args.binary_steps, use_llm=(args.model is not None))
        client._export_session()
    else:
        # Interactive session
        client.interactive_research_session()


if __name__ == "__main__":
    main()
