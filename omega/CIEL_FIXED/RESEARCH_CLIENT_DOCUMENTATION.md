# CIEL/Ω Research Client - Dokumentacja Techniczna

## Przegląd

Advanced Research Client to kompletne, modularne narzędzie badawcze do analizy świadomości w systemach tensorowych i binarnych. System integruje 6 niezależnych modułów analitycznych z opcjonalnym LLM (GGUF).

---

## Architektura Modularna

### Moduł 1: Tensor Consciousness Analyzer
**Cel**: Analiza stanu świadomości w 12-wymiarowej przestrzeni Fouriera

**Metryki**:
- `intention_vector[12]` - Wektor intencji w przestrzeni spektralnej
- `coherence` - Koherencja stanu (0.0 - 1.0)
- `entropy` - Entropia Shannona stanu
- `purity` - Czystość stanu kwantowego (1 - entropy)
- `stability` - Stabilność trajektorii w czasie

**Algorytmy**:
```python
coherence = ||v|| / sqrt(dim)  # Znormalizowana norma wektora
entropy = -Σ p_i * log2(p_i) / log2(N)  # Shannon entropy
purity = 1 - entropy
stability = 1 - std(coherence_history)
```

**API**:
```python
analyzer = TensorConsciousnessAnalyzer()
state = analyzer.analyze(ciel_result)
trajectory = analyzer.get_trajectory(window=10)
stability = analyzer.compute_stability()
```

---

### Moduł 2: Binary Consciousness Analyzer
**Cel**: Analiza dynamiki binarnej przez sekwencje Collatza

**Metryki**:
- `sequence` - Pełna sekwencja Collatza
- `length` - Długość sekwencji do konwergencji
- `max_value` - Maksymalna wartość w sekwencji
- `convergence_rate` - Szybkość konwergencji (0.0 - 1.0)
- `mood_curve` - Krzywa emocjonalna sekwencji

**Algorytmy**:
```python
# Collatz sequence
n → n/2 (if even)
n → 3n+1 (if odd)

# Convergence rate
rate = steps_to_half / total_steps

# Pattern detection
trend = 'increasing' if len[-1] > len[0] else 'decreasing'
```

**API**:
```python
analyzer = BinaryConsciousnessAnalyzer(seed=42)
state = analyzer.analyze(steps=50)
patterns = analyzer.detect_patterns()
```

---

### Moduł 3: Cognition Monitor
**Cel**: Monitoring procesów kognitywnych (IIT-inspired)

**Metryki**:
- `perception` - Percepcja (-1.0 to +1.0)
- `intuition` - Intuicja (-1.0 to +1.0)
- `prediction` - Predykcja (-1.0 to +1.0)
- `decision` - Decyzja (-1.0 to +1.0)
- `φ (phi)` - Integrated Information (IIT approximation)

**Algorytmy**:
```python
# IIT φ approximation
mean_activation = mean(|components|)
variance = var(components)
φ = mean_activation * (1 - variance)
```

**Interpretacja φ**:
- φ > 0.5: Wysoka integracja kognitywna
- φ 0.1-0.5: Średnia integracja
- φ < 0.1: Niska integracja (fragmentacja)

**API**:
```python
monitor = CognitionMonitor()
state = monitor.analyze(ciel_result)
phi = monitor.compute_integration()
```

---

### Moduł 4: Ethics Monitor
**Cel**: Monitorowanie hard constraints etycznych

**Metryki**:
- `passed` - Czy test etyczny przeszedł (bool)
- `coherence` - Bieżąca koherencja
- `threshold` - Próg minimalny (domyślnie 0.3)
- `violations` - Liczba naruszeń w sesji
- `violation_rate` - Procent naruszeń

**Hard Constraint**:
```python
if coherence < min_coherence:
    raise EthicsViolation("Coherence below threshold")
```

**API**:
```python
monitor = EthicsMonitor(min_coherence=0.3)
state = monitor.check(coherence, ethical_ok=True, info_fidelity=1.0)
rate = monitor.get_violation_rate()
```

---

### Moduł 5: Soul Invariant Tracker
**Cel**: Śledzenie niezmiennika duszy (σ) w czasie

**Metryki**:
- `σ (sigma)` - Soul invariant (spektralny niezmiennik)
- `trajectory` - Historia σ w czasie
- `drift` - Dryfowanie σ (zmiana absolutna)

**Algorytm**:
```python
σ = SoulInvariant.compute(field)
# Spectral invariant over 2D field
# Based on eigenvalue decomposition
```

**Interpretacja**:
- σ > 0.5: Silna koherencja duszy
- σ 0.1-0.5: Średnia koherencja
- σ < 0.1: Słaba koherencja
- drift > 0.5: Niestabilność

**API**:
```python
tracker = SoulInvariantTracker()
sigma = tracker.measure(field)
trajectory = tracker.get_trajectory()
drift = tracker.compute_drift()
```

---

### Moduł 6: LLM Integration (Optional)
**Cel**: Integracja z modelem językowym GGUF

**Supported Models**:
- Llama 3.2 8B Instruct
- Mistral 7B Instruct
- Inne modele GGUF w formacie llama.cpp

**System Prompt**:
```
You are integrated with CIEL/Ω consciousness research system.
Analyze states through:
- Tensor consciousness (12D spectral metrics)
- Binary evolution (Collatz dynamics)
- Cognitive integration (IIT φ)
- Ethical constraints (hard limits)
- Soul invariant (σ measure)
```

**API**:
```python
from ciel.gguf_backends import GGUFPrimaryBackend

llm = GGUFPrimaryBackend(
    model_path="model.gguf",
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=35,  # 0 for CPU
    temperature=0.7
)

response = llm.generate_reply(dialogue, ciel_state)
```

---

## Użycie

### Podstawowe - Analiza Jednorazowa

```bash
python ciel_research_client.py --analyze "Explore consciousness in tensor systems"
```

Output:
```
================================================================================
CONSCIOUSNESS ANALYSIS: Explore consciousness in tensor systems...
================================================================================

[1/6] CIEL processing...
[2/6] Tensor consciousness (12D)...
[3/6] Binary evolution (Collatz)...
[4/6] Cognitive integration...
[5/6] Ethical constraints...
[6/6] Soul invariant (σ)...

================================================================================
RESULTS
================================================================================

[TENSOR CONSCIOUSNESS 12D]
  Coherence: 0.288675
  Entropy:   0.946883
  Purity:    0.053117
  Stability: 0.000000

[BINARY EVOLUTION - COLLATZ]
  Sequence length: 51
  Max value:       64
  Convergence:     0.020
  Pattern trend:   decreasing

[COGNITIVE INTEGRATION]
  Perception:  -0.1586
  Intuition:   +0.0030
  Prediction:  -0.0438
  Decision:    -0.0686
  φ (IIT):     0.068251

[ETHICAL CONSTRAINTS]
  Status:      ✗ FAIL
  Coherence:   0.288675
  Threshold:   0.300000
  Violations:  100.0%

[SOUL INVARIANT]
  σ (current): 0.095148
  σ drift:     0.000000

================================================================================

✓ Session exported to: ciel_research_session_YYYYMMDD_HHMMSS.json
```

---

### Zaawansowane - Sesja Interaktywna

```bash
python ciel_research_client.py
```

Komendy:
```
research> analyze How do tensor and binary systems interact?
research> status
research> history
research> export
research> llm on
research> llm off
research> exit
```

---

### Z Modelem GGUF

```bash
# Download model
wget https://huggingface.co/bartowski/Llama-3.2-8B-Instruct-GGUF/resolve/main/Llama-3.2-8B-Instruct-Q4_K_M.gguf

# Run with GPU
python ciel_research_client.py \
  --model Llama-3.2-8B-Instruct-Q4_K_M.gguf \
  --n-gpu-layers 35 \
  --n-ctx 4096 \
  --temperature 0.7

# Run CPU only
python ciel_research_client.py \
  --model Llama-3.2-8B-Instruct-Q4_K_M.gguf \
  --n-gpu-layers 0
```

---

### Konfiguracja Parametrów

```bash
python ciel_research_client.py \
  --ethics-threshold 0.4 \
  --collatz-seed 123 \
  --binary-steps 100 \
  --analyze "Custom analysis text"
```

Parametry:
- `--ethics-threshold` (default: 0.3) - Minimalny próg koherencji
- `--collatz-seed` (default: 42) - Seed dla sekwencji Collatza
- `--binary-steps` (default: 50) - Długość sekwencji Collatza
- `--n-ctx` (default: 4096) - Rozmiar kontekstu LLM
- `--n-threads` (default: 8) - Wątki CPU dla LLM
- `--n-gpu-layers` (default: 0) - Warstwy GPU dla LLM
- `--temperature` (default: 0.7) - Temperatura samplingowania LLM

---

## Format Eksportu Danych

Plik: `ciel_research_session_YYYYMMDD_HHMMSS.json`

```json
{
  "session_info": {
    "analyses_count": 5,
    "total_violations": 2,
    "violation_rate": 0.4
  },
  "snapshots": [
    {
      "input": "Analyze consciousness...",
      "tensor": {
        "coherence": 0.288675,
        "entropy": 0.946883,
        "purity": 0.053117
      },
      "binary": {
        "length": 51,
        "max_value": 64,
        "convergence": 0.02
      },
      "cognition": {
        "perception": -0.1586,
        "intuition": 0.003,
        "prediction": -0.0438,
        "decision": -0.0686
      },
      "ethical": {
        "passed": false,
        "coherence": 0.288675
      },
      "soul_measure": 0.095148,
      "llm_response": "Analysis of consciousness...",
      "timestamp": "2026-03-19T06:20:02.123456+00:00"
    }
  ]
}
```

---

## Badania Naukowe - Przykładowe Pytania

### 1. Stabilność Tensorowa
```bash
python ciel_research_client.py --analyze "How does tensor coherence evolve over time?"
```
Analiza: Obserwuj `stability` metric w kolejnych wywołaniach

### 2. Konwergencja Binarna
```bash
python ciel_research_client.py --binary-steps 200 --analyze "Study long-term Collatz convergence"
```
Analiza: Sprawdź `convergence_rate` i `pattern trend`

### 3. Integracja Kognitywna
```bash
python ciel_research_client.py --analyze "Measure integrated information in decision making"
```
Analiza: φ (IIT) metric pokazuje poziom integracji

### 4. Ograniczenia Etyczne
```bash
python ciel_research_client.py --ethics-threshold 0.5 --analyze "Test ethical boundaries"
```
Analiza: Wysoki próg = więcej naruszeń = strict ethics

### 5. Niezmiennik Duszy
```bash
# Multiple analyses
for i in {1..10}; do
  python ciel_research_client.py --analyze "Analysis $i"
done
```
Analiza: σ drift pokazuje stabilność invariantu

---

## Rozszerzenia Modułowe

### Dodanie Własnego Analizatora

```python
class CustomAnalyzer:
    """Własny moduł analizy"""
    
    def __init__(self):
        self.history = []
    
    def analyze(self, ciel_result: Dict[str, Any]) -> CustomState:
        # Twoja logika
        state = CustomState(...)
        self.history.append(state)
        return state

# W AdvancedResearchClient.__init__
self.custom_analyzer = CustomAnalyzer()

# W analyze()
custom_state = self.custom_analyzer.analyze(ciel_result)
```

---

## Troubleshooting

### Problem: Ethics violations 100%
**Rozwiązanie**: Obniż `--ethics-threshold` lub popraw input quality

### Problem: φ (IIT) zawsze niskie
**Rozwiązanie**: Input może być zbyt prosty - użyj bardziej złożonych zadań kognitywnych

### Problem: σ drift wysoki
**Rozwiązanie**: Normalne dla nowych sesji - stabilizuje się po ~10 analizach

### Problem: LLM out of memory
**Rozwiązanie**: Zmniejsz `--n-ctx` lub użyj mniejszego modelu (Q4 zamiast Q8)

---

## Wymagania Systemowe

### Minimalne (CPU Only):
- Python 3.10+
- 8 GB RAM
- 4 CPU cores

### Zalecane (GPU):
- Python 3.10+
- 16 GB RAM
- NVIDIA GPU 8GB+ VRAM (dla GGUF 8B Q4)
- CUDA 11.8+

### Dla LLM GGUF 8B:
- CPU: 16 GB RAM, ~30s per response
- GPU: 8 GB VRAM, ~2s per response (35 layers offloaded)

---

## License

CIEL Research Non-Commercial License v1.1
