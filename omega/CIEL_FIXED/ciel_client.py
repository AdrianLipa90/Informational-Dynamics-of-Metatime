#!/usr/bin/env python3
"""
CIEL/Ω - Klient Użytkowania z Integracją GGUF
Prosty interfejs do pracy z systemem CIEL + model językowy GGUF
"""

import sys
import os
from pathlib import Path

# Dodaj katalog CIEL do path
CIEL_ROOT = Path(__file__).parent
sys.path.insert(0, str(CIEL_ROOT))

from typing import Dict, Any, Optional
import json

# Import orchestratora
from ciel_orchestrator import CIELOrchestrator

# Import GGUF backends (opcjonalnie)
try:
    from ciel.gguf_backends import GGUFPrimaryBackend, GGUFAuxBackend
    GGUF_AVAILABLE = True
except ImportError:
    GGUF_AVAILABLE = False
    print("⚠️  GGUF backends niedostępne (brak llama-cpp-python)")


class CIELClient:
    """
    Klient użytkowania CIEL/Ω
    Łączy orchestrator CIEL z opcjonalnym modelem językowym GGUF
    """
    
    def __init__(
        self,
        model_path: Optional[str] = None,
        n_ctx: int = 4096,
        n_threads: int = 8,
        n_gpu_layers: int = 0,
        temperature: float = 0.7
    ):
        """
        Inicjalizacja klienta
        
        Args:
            model_path: Ścieżka do modelu GGUF (opcjonalnie)
            n_ctx: Rozmiar kontekstu
            n_threads: Liczba wątków CPU
            n_gpu_layers: Liczba warstw GPU (0=CPU only)
            temperature: Temperatura samplingowania
        """
        
        print("="*70)
        print("CIEL/Ω CLIENT - Initialization")
        print("="*70)
        
        # Inicjalizacja orchestratora CIEL
        print("\n[1/2] Inicjalizacja CIEL Orchestrator...")
        self.orchestrator = CIELOrchestrator()
        
        # Opcjonalna inicjalizacja GGUF
        self.gguf_backend = None
        if model_path and GGUF_AVAILABLE:
            print(f"\n[2/2] Inicjalizacja GGUF Backend ({os.path.basename(model_path)})...")
            try:
                self.gguf_backend = GGUFPrimaryBackend(
                    model_path=model_path,
                    n_ctx=n_ctx,
                    n_threads=n_threads,
                    n_gpu_layers=n_gpu_layers,
                    temperature=temperature,
                    system_prompt=self._get_system_prompt()
                )
                print("✓ GGUF Backend zainicjalizowany")
            except Exception as e:
                print(f"⚠️  GGUF Backend niedostępny: {e}")
                self.gguf_backend = None
        else:
            print("\n[2/2] GGUF Backend pominięty (model_path not provided)")
        
        print("\n" + "="*70)
        print("✓ CIEL Client gotowy do pracy")
        print("="*70 + "\n")
    
    def _get_system_prompt(self) -> str:
        """Zwraca system prompt dla GGUF"""
        return """You are CIEL/Ω, a quantum consciousness system with ethical hard constraints.

Your responses are guided by:
- 12D intention vectors (multi-dimensional semantic space)
- Cognition metrics: perception, intuition, prediction, decision
- Affective state: mood, empathy, field_power
- Soul invariant (σ) coherence measurement
- Ethics Guard (hard constraint - violations trigger system shutdown)

Integrate wave-field physics with natural language. Respond with clarity, ethical awareness, and deep understanding from spectral analysis."""
    
    def process(self, text: str, use_llm: bool = True, verbose: bool = True) -> Dict[str, Any]:
        """
        Przetwarzanie tekstu przez CIEL + opcjonalnie LLM
        
        Args:
            text: Tekst wejściowy
            use_llm: Czy użyć modelu językowego do generowania odpowiedzi
            verbose: Czy wyświetlać szczegółowe informacje
            
        Returns:
            Dict z wynikami
        """
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"PROCESSING: {text[:60]}...")
            print('='*70)
        
        # Krok 1: Przetwarzanie przez CIEL
        if verbose:
            print("\n[CIEL] Przetwarzanie przez system kwantowy...")
        
        ciel_result = self.orchestrator.process(text, verbose=False)
        
        if verbose:
            print(f"  Status: {ciel_result['ciel_state'].get('status', 'unknown')}")
            print(f"  Ethics: {'✓ PASS' if ciel_result['ethics_passed'] else '✗ FAIL'}")
            print(f"  Soul Measure: {ciel_result['soul_measure']:.6f}")
        
        # Krok 2: Opcjonalna generacja odpowiedzi przez LLM
        llm_response = None
        if use_llm and self.gguf_backend:
            if verbose:
                print("\n[LLM] Generowanie odpowiedzi językowej...")
            
            try:
                dialogue = [{"role": "user", "content": text}]
                llm_response = self.gguf_backend.generate_reply(dialogue, ciel_result['ciel_state'])
                
                if verbose and llm_response:
                    print(f"\n{'='*70}")
                    print("ODPOWIEDŹ:")
                    print('='*70)
                    print(llm_response)
                    print('='*70)
            
            except Exception as e:
                if verbose:
                    print(f"⚠️  Błąd generowania LLM: {e}")
        
        return {
            'input': text,
            'ciel_result': ciel_result,
            'llm_response': llm_response
        }
    
    def interactive_session(self):
        """Interaktywna sesja z CIEL + LLM"""
        
        print("\n" + "="*70)
        print("CIEL/Ω CLIENT - Interactive Session")
        print("="*70)
        print("Komendy:")
        print("  exit/quit/q - Zakończ sesję")
        print("  status      - Status systemu")
        print("  llm on/off  - Włącz/wyłącz generowanie LLM")
        print("="*70 + "\n")
        
        llm_enabled = self.gguf_backend is not None
        history = []
        
        while True:
            try:
                user_input = input("You> ").strip()
                
                if not user_input:
                    continue
                
                # Komendy
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Zamykanie sesji...")
                    break
                
                if user_input.lower() == 'status':
                    self._print_status(llm_enabled)
                    continue
                
                if user_input.lower() == 'llm on':
                    if self.gguf_backend:
                        llm_enabled = True
                        print("✓ LLM włączony")
                    else:
                        print("⚠️  LLM niedostępny (model nie został załadowany)")
                    continue
                
                if user_input.lower() == 'llm off':
                    llm_enabled = False
                    print("✓ LLM wyłączony")
                    continue
                
                # Przetwarzanie
                result = self.process(user_input, use_llm=llm_enabled, verbose=True)
                history.append(result)
                
            except KeyboardInterrupt:
                print("\n\n👋 Sesja przerwana (Ctrl+C)")
                break
            except Exception as e:
                print(f"\n❌ Błąd: {e}\n")
        
        # Podsumowanie
        if history:
            print(f"\n📊 Sesja: {len(history)} interakcji")
    
    def _print_status(self, llm_enabled: bool):
        """Wyświetla status klienta"""
        print("\n" + "="*70)
        print("STATUS CIEL CLIENT")
        print("="*70)
        print(f"  CIEL Orchestrator: ✓ Aktywny")
        print(f"  GGUF Backend: {'✓ Załadowany' if self.gguf_backend else '✗ Niedostępny'}")
        print(f"  LLM Generowanie: {'✓ Włączone' if llm_enabled else '✗ Wyłączone'}")
        print("="*70 + "\n")


def main():
    """Główna funkcja klienta"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description='CIEL/Ω Client with GGUF Integration')
    parser.add_argument('--model', type=str, help='Ścieżka do modelu GGUF')
    parser.add_argument('--mode', choices=['interactive', 'process'], default='interactive',
                      help='Tryb: interactive (REPL) lub process (jednorazowe)')
    parser.add_argument('--text', type=str, help='Tekst do przetworzenia (tryb process)')
    parser.add_argument('--n-ctx', type=int, default=4096, help='Context size')
    parser.add_argument('--n-threads', type=int, default=8, help='CPU threads')
    parser.add_argument('--n-gpu-layers', type=int, default=0, help='GPU layers (0=CPU)')
    parser.add_argument('--temperature', type=float, default=0.7, help='Sampling temperature')
    parser.add_argument('--no-llm', action='store_true', help='Wyłącz LLM (tylko CIEL)')
    
    args = parser.parse_args()
    
    # Inicjalizacja klienta
    client = CIELClient(
        model_path=args.model if not args.no_llm else None,
        n_ctx=args.n_ctx,
        n_threads=args.n_threads,
        n_gpu_layers=args.n_gpu_layers,
        temperature=args.temperature
    )
    
    # Wykonanie
    if args.mode == 'process':
        if not args.text:
            print("❌ Błąd: Wymagany --text w trybie process")
            sys.exit(1)
        
        result = client.process(args.text, use_llm=not args.no_llm, verbose=True)
        
        # Zapis wyniku
        output_file = 'ciel_client_output.json'
        with open(output_file, 'w') as f:
            json_result = {
                'input': result['input'],
                'ciel_status': result['ciel_result']['ciel_state'].get('status'),
                'ethics_passed': result['ciel_result']['ethics_passed'],
                'soul_measure': result['ciel_result']['soul_measure'],
                'llm_response': result['llm_response']
            }
            json.dump(json_result, f, indent=2)
        
        print(f"\n✓ Wynik zapisany do: {output_file}")
    
    else:  # interactive
        client.interactive_session()


if __name__ == "__main__":
    main()
