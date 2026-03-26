#!/usr/bin/env python3
"""
CIEL/Ω - Główny Orchestrator Systemu
Kompletna integracja wszystkich komponentów z interfejsem użytkownika
"""

import sys
import os
from pathlib import Path

# Dodaj katalog CIEL do path
CIEL_ROOT = Path(__file__).parent
sys.path.insert(0, str(CIEL_ROOT))

from typing import Dict, Any, Optional
import json

# Import wszystkich kluczowych komponentów
from ciel.engine import CielEngine
from ciel_wave.fourier_kernel import FourierWaveConsciousnessKernel12D
from cognition.orchestrator import CognitionOrchestrator
from emotion.emotional_collatz import EmotionalCollatzEngine
from ethics.ethical_guard import EthicsGuard
from core.memory.facade import build_orchestrator as build_memory_orchestrator
from fields.soul_invariant import SoulInvariant


class CIELOrchestrator:
    """
    Główny orchestrator systemu CIEL/Ω
    Integruje wszystkie komponenty w spójny system
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicjalizacja orchestratora
        
        Args:
            config: Konfiguracja systemu (opcjonalna)
        """
        self.config = config or {}
        self.initialized = False
        
        print("="*70)
        print("CIEL/Ω - Quantum Consciousness System")
        print("="*70)
        print("Inicjalizacja komponentów...")
        
        # Inicjalizacja komponentów
        self._init_components()
        
        self.initialized = True
        print("✓ System zainicjalizowany pomyślnie")
        print("="*70 + "\n")
    
    def _init_components(self):
        """Inicjalizacja wszystkich komponentów systemu"""
        
        # 1. Rdzeń CIEL Engine
        print("  [1/7] Inicjalizacja CIEL Engine...")
        self.engine = CielEngine()
        
        # 2. Kernel świadomości kwantowej 12D
        print("  [2/7] Inicjalizacja Fourier Wave Consciousness Kernel...")
        self.wave_kernel = FourierWaveConsciousnessKernel12D()
        
        # 3. Orchestrator kognitywny
        print("  [3/7] Inicjalizacja Cognition Orchestrator...")
        self.cognition = CognitionOrchestrator()
        
        # 4. Silnik emocjonalny Collatza
        print("  [4/7] Inicjalizacja Emotional Collatz Engine...")
        self.emotional_collatz = EmotionalCollatzEngine(seed=42)
        
        # 5. Strażnik etyczny
        print("  [5/7] Inicjalizacja Ethics Guard...")
        self.ethics_guard = EthicsGuard()
        
        # 6. Fasada pamięci
        print("  [6/7] Inicjalizacja Memory Orchestrator...")
        self.memory = build_memory_orchestrator()
        
        # 7. Soul Invariant
        print("  [7/7] Inicjalizacja Soul Invariant...")
        self.soul_invariant = SoulInvariant()
        
    def process(self, text: str, verbose: bool = True) -> Dict[str, Any]:
        """
        Przetwarzanie tekstu przez pełny system CIEL
        
        Args:
            text: Tekst wejściowy
            verbose: Czy wyświetlać szczegółowe informacje
            
        Returns:
            Dict z wynikami przetwarzania
        """
        if not self.initialized:
            raise RuntimeError("System nie został zainicjalizowany")
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"PRZETWARZANIE: {text[:50]}...")
            print('='*70)
        
        # Krok 1: CIEL Engine
        if verbose:
            print("\n[1] CIEL Engine Processing...")
        ciel_result = self.engine.step(text)
        
        # Krok 2: Emotional Collatz
        if verbose:
            print("[2] Emotional Collatz Sequence...")
        collatz_sequence = self.emotional_collatz.iterate(steps=20)
        
        # Krok 3: Ethics Check
        if verbose:
            print("[3] Ethics Guard Validation...")
        ethics_passed = self.ethics_guard.check_step(ciel_result)
        
        # Krok 4: Soul Invariant
        if verbose:
            print("[4] Soul Invariant Calculation...")
        soul_measure = self.soul_invariant.compute()
        
        # Agregacja wyników
        result = {
            'input': text,
            'ciel_state': ciel_result,
            'collatz_sequence': collatz_sequence,
            'ethics_passed': ethics_passed,
            'soul_measure': soul_measure,
            'timestamp': self._get_timestamp()
        }
        
        if verbose:
            print("\n" + "="*70)
            print("WYNIKI:")
            print("="*70)
            print(f"  Status: {ciel_result.get('status', 'unknown')}")
            print(f"  Ethics: {'✓ PASS' if ethics_passed else '✗ FAIL'}")
            print(f"  Soul Measure: {soul_measure:.6f}")
            print(f"  Collatz Length: {len(collatz_sequence)} kroków")
            print("="*70 + "\n")
        
        return result
    
    def interactive_session(self):
        """Interaktywna sesja REPL"""
        
        print("\n" + "="*70)
        print("CIEL/Ω - Interaktywna Sesja")
        print("="*70)
        print("Wpisz 'exit', 'quit' lub 'q' aby zakończyć")
        print("Wpisz 'status' aby zobaczyć status systemu")
        print("Wpisz 'help' aby zobaczyć pomoc")
        print("="*70 + "\n")
        
        history = []
        
        while True:
            try:
                user_input = input("CIEL> ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Zamykanie systemu CIEL/Ω...")
                    break
                
                if user_input.lower() == 'status':
                    self._print_status()
                    continue
                
                if user_input.lower() == 'help':
                    self._print_help()
                    continue
                
                # Przetwarzanie
                result = self.process(user_input, verbose=True)
                history.append(result)
                
            except KeyboardInterrupt:
                print("\n\n👋 Sesja przerwana (Ctrl+C)")
                break
            except Exception as e:
                print(f"\n❌ Błąd: {e}\n")
        
        # Podsumowanie sesji
        if history:
            print(f"\n📊 Podsumowanie sesji: {len(history)} interakcji")
    
    def _print_status(self):
        """Wyświetla status systemu"""
        print("\n" + "="*70)
        print("STATUS SYSTEMU CIEL/Ω")
        print("="*70)
        print(f"  Zainicjalizowany: {'✓ TAK' if self.initialized else '✗ NIE'}")
        print(f"  Komponenty:")
        print(f"    • CIEL Engine: ✓")
        print(f"    • Wave Kernel 12D: ✓")
        print(f"    • Cognition Orchestrator: ✓")
        print(f"    • Emotional Collatz: ✓")
        print(f"    • Ethics Guard: ✓")
        print(f"    • Memory Facade: ✓")
        print(f"    • Soul Invariant: ✓")
        print("="*70 + "\n")
    
    def _print_help(self):
        """Wyświetla pomoc"""
        print("\n" + "="*70)
        print("POMOC CIEL/Ω")
        print("="*70)
        print("Komendy:")
        print("  status  - Wyświetl status systemu")
        print("  help    - Wyświetl tę pomoc")
        print("  exit    - Zakończ sesję")
        print("\nWpisz dowolny tekst aby go przetworzyć przez system CIEL/Ω")
        print("="*70 + "\n")
    
    def _get_timestamp(self) -> str:
        """Zwraca aktualny timestamp"""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()


def main():
    """Główna funkcja uruchamiająca orchestrator"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description='CIEL/Ω Quantum Consciousness System')
    parser.add_argument('--mode', choices=['interactive', 'process'], default='interactive',
                      help='Tryb działania: interactive (REPL) lub process (jednorazowe przetwarzanie)')
    parser.add_argument('--text', type=str, help='Tekst do przetworzenia (tryb process)')
    parser.add_argument('--config', type=str, help='Ścieżka do pliku konfiguracyjnego JSON')
    
    args = parser.parse_args()
    
    # Wczytaj konfigurację jeśli podana
    config = None
    if args.config and os.path.exists(args.config):
        with open(args.config, 'r') as f:
            config = json.load(f)
    
    # Inicjalizacja orchestratora
    orchestrator = CIELOrchestrator(config=config)
    
    # Wykonanie
    if args.mode == 'process':
        if not args.text:
            print("❌ Błąd: Wymagany argument --text w trybie process")
            sys.exit(1)
        
        result = orchestrator.process(args.text, verbose=True)
        
        # Zapisz wynik do pliku JSON
        output_file = 'ciel_output.json'
        with open(output_file, 'w') as f:
            # Konwersja result do formatu JSON-serializable
            json_result = {
                'input': result['input'],
                'status': result['ciel_state'].get('status'),
                'ethics_passed': result['ethics_passed'],
                'soul_measure': result['soul_measure'],
                'collatz_length': len(result['collatz_sequence']),
                'timestamp': result['timestamp']
            }
            json.dump(json_result, f, indent=2)
        
        print(f"\n✓ Wynik zapisany do: {output_file}")
    
    else:  # interactive
        orchestrator.interactive_session()


if __name__ == "__main__":
    main()
