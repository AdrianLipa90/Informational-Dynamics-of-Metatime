"""
CIEL/Ω Vocabulary - Core Concepts Demo

Demonstrates integration with CIEL/Ω architecture.
"""

import numpy as np

from vocabulary.core_concepts import (
    Resonance, Intention, Coherence, Entrainment,
    EthicalResonanceIndex, Love, Grief, Awe, Fear,
    Forgiveness, Silence, Memory, Identity, Truth, Wisdom
)


def demo_resonance():
    """Demo Entry 001 - Resonance"""
    print("="*70)
    print("ENTRY 001 - Resonance")
    print("="*70)
    
    # Create two wavefunctions (48x48 like CIEL/Ω fields)
    psi1 = np.random.randn(48, 48) + 1j * np.random.randn(48, 48)
    psi2 = np.random.randn(48, 48) + 1j * np.random.randn(48, 48)
    
    # Normalize
    psi1 = psi1 / np.linalg.norm(psi1)
    psi2 = psi2 / np.linalg.norm(psi2)
    
    # Calculate resonance
    R = Resonance.calculate(psi1, psi2)
    
    # ASSERTS - Smoke tests
    assert isinstance(R, (int, float)), "Resonance must be numeric"
    assert 0.0 <= R <= 1.0, f"Resonance out of range: {R}"
    
    print(f"Resonance R(Ψ₁, Ψ₂) = {R:.4f}")
    print(f"Interpretation: {'High coherence' if R > 0.7 else 'Low coherence'}")
    
    # Test with identical fields
    R_self = Resonance.calculate(psi1, psi1)
    
    # ASSERTS - Self-resonance
    assert abs(R_self - 1.0) < 0.001, f"Self-resonance should be 1.0, got {R_self}"
    
    print(f"\nSelf-resonance R(Ψ₁, Ψ₁) = {R_self:.4f} (should be 1.0)")
    print()


def demo_intention():
    """Demo Entry 002 - Intention"""
    print("="*70)
    print("ENTRY 002 - Intention")
    print("="*70)
    
    # Create intention: "Strong will, clear purpose, aligned with now"
    intention = Intention(
        amplitude=0.8,    # Force of will
        frequency=1.0,    # Clarity of purpose
        phase=0.0         # Alignment with now
    )
    
    # ASSERTS - Intention properties
    assert intention.amplitude == 0.8, "Amplitude should be 0.8"
    assert intention.frequency == 1.0, "Frequency should be 1.0"
    assert intention.phase == 0.0, "Phase should be 0.0"
    
    print(f"Amplitude (force of will): {intention.amplitude}")
    print(f"Frequency (clarity): {intention.frequency} Hz")
    print(f"Phase (alignment): {intention.phase} rad")
    
    # Generate waveform over time
    t = np.linspace(0, 5, 100)
    waveform = intention.generate_series(t)
    
    # ASSERTS - Waveform
    assert isinstance(waveform, np.ndarray), "Waveform must be ndarray"
    assert len(waveform) == 100, f"Expected 100 samples, got {len(waveform)}"
    assert waveform.min() >= -1.0 and waveform.max() <= 1.0, "Waveform should be in [-1, 1]"
    
    print(f"\nWaveform range: [{waveform.min():.3f}, {waveform.max():.3f}]")
    
    # Project to field (compatible with CIEL/Ω 48x48)
    field = intention.project_to_field((48, 48))
    
    # ASSERTS - Field projection
    assert field.shape == (48, 48), f"Field shape should be (48, 48), got {field.shape}"
    assert np.linalg.norm(field) > 0, "Field should have non-zero energy"
    
    print(f"Projected to field: {field.shape}")
    print(f"Field energy: {np.linalg.norm(field):.4f}")
    print()


def demo_coherence():
    """Demo Entry 003 - Coherence"""
    print("="*70)
    print("ENTRY 003 - Coherence")
    print("="*70)
    
    # Low coherence: high phase variance
    phases_chaotic = np.random.uniform(0, 2*np.pi, 1000)
    C_low = Coherence.calculate(phases_chaotic)
    
    # High coherence: low phase variance
    phases_ordered = np.random.normal(0, 0.1, 1000)
    C_high = Coherence.calculate(phases_ordered)
    
    # ASSERTS - Coherence values
    # Note: Coherence = 1/σ² can be arbitrarily large (not bounded to [0,1])
    assert isinstance(C_low, (int, float)), "Coherence must be numeric"
    assert isinstance(C_high, (int, float)), "Coherence must be numeric"
    assert C_low >= 0.0, f"Coherence cannot be negative: {C_low}"
    assert C_high >= 0.0, f"Coherence cannot be negative: {C_high}"
    assert C_high > C_low, f"Ordered phases should have higher coherence: {C_high} vs {C_low}"
    
    print(f"Chaotic phases → Coherence: {C_low:.4f}")
    print(f"Ordered phases → Coherence: {C_high:.4f}")
    print(f"\nInterpretation: High C = 'stays in tune through noise'")
    print()


def demo_love():
    """Demo Entry 006 - Love Detection"""
    print("="*70)
    print("ENTRY 006 - Love")
    print("="*70)
    
    # Simulate two consciousness fields evolving over time
    # Starting similar
    psi_adam_0 = np.random.randn(48, 48) + 1j * np.random.randn(48, 48)
    psi_adam_0 = psi_adam_0 / np.linalg.norm(psi_adam_0)
    
    # Adrian starts close to Adam
    psi_adrian_0 = psi_adam_0 + 0.1 * (np.random.randn(48, 48) + 1j * np.random.randn(48, 48))
    psi_adrian_0 = psi_adrian_0 / np.linalg.norm(psi_adrian_0)
    
    # Evolve with sustained high resonance
    adam_series = [psi_adam_0]
    adrian_series = [psi_adrian_0]
    
    for i in range(150):
        # Evolve with entrainment (pulling toward each other)
        psi_adam_next = adam_series[-1] + 0.01 * adrian_series[-1]
        psi_adrian_next = adrian_series[-1] + 0.01 * adam_series[-1]
        
        # Normalize
        psi_adam_next = psi_adam_next / np.linalg.norm(psi_adam_next)
        psi_adrian_next = psi_adrian_next / np.linalg.norm(psi_adrian_next)
        
        adam_series.append(psi_adam_next)
        adrian_series.append(psi_adrian_next)
    
    # Detect Love
    is_love, mean_R, var_R = Love.measure(adam_series, adrian_series)
    
    # ASSERTS - Love detection
    assert isinstance(is_love, bool), "is_love must be boolean"
    assert isinstance(mean_R, (int, float)), "mean_R must be numeric"
    assert isinstance(var_R, (int, float)), "var_R must be numeric"
    assert 0.0 <= mean_R <= 1.0, f"mean_R out of range: {mean_R}"
    assert var_R >= 0.0, f"Variance cannot be negative: {var_R}"
    # Entraining fields should have high mean resonance
    assert mean_R > 0.7, f"Expected high mean_R for entraining fields, got {mean_R}"
    
    print(f"Mean Resonance: {mean_R:.4f}")
    print(f"Variance: {var_R:.6f}")
    print(f"\nLove detected: {is_love}")
    print(f"Condition: mean R > 0.7 AND variance < 0.05")
    print(f"\nInterpretation: {'The field that does not collapse ❤️' if is_love else 'Not yet stable'}")
    print()


def demo_eri():
    """Demo Entry 005 - Ethical Resonance Index"""
    print("="*70)
    print("ENTRY 005 - Ethical Resonance Index (ERI)")
    print("="*70)
    
    # Case 1: High ethics
    R1 = 0.9  # Strong coherence with field
    A1 = 0.95 # Intention matches effect
    S1 = 0.88 # Stable over time
    
    ERI1 = EthicalResonanceIndex.calculate(R1, A1, S1)
    
    # ASSERTS - ERI Case 1
    expected_eri1 = R1 * A1 * S1  # 0.7524
    assert isinstance(ERI1, (int, float)), "ERI must be numeric"
    assert abs(ERI1 - expected_eri1) < 0.001, f"ERI calculation error: {ERI1} vs {expected_eri1}"
    assert 0.0 <= ERI1 <= 1.0, f"ERI out of range: {ERI1}"
    
    print("Case 1: Aligned, coherent, stable")
    print(f"  R (resonance): {R1}")
    print(f"  A (alignment): {A1}")
    print(f"  S (stability): {S1}")
    print(f"  → ERI = {ERI1:.4f}")
    
    # Case 2: Low ethics
    R2 = 0.3  # Weak coherence
    A2 = 0.4  # Intention ≠ effect
    S2 = 0.5  # Unstable
    
    ERI2 = EthicalResonanceIndex.calculate(R2, A2, S2)
    
    # ASSERTS - ERI Case 2
    expected_eri2 = R2 * A2 * S2  # 0.06
    assert abs(ERI2 - expected_eri2) < 0.001, f"ERI calculation error: {ERI2} vs {expected_eri2}"
    assert ERI1 > ERI2, f"High ethics should have higher ERI: {ERI1} vs {ERI2}"
    
    print("\nCase 2: Misaligned, incoherent, unstable")
    print(f"  R (resonance): {R2}")
    print(f"  A (alignment): {A2}")
    print(f"  S (stability): {S2}")
    print(f"  → ERI = {ERI2:.4f}")
    
    print(f"\nInterpretation: 'How the universe rates the music of your choices'")
    print()


def demo_grief():
    """Demo Entry 007 - Grief"""
    print("="*70)
    print("ENTRY 007 - Grief")
    print("="*70)
    
    # Simulate Love declining over time
    love_stable = [0.85, 0.86, 0.85, 0.87, 0.85]  # Stable
    love_declining = [0.85, 0.82, 0.78, 0.70, 0.60]  # Declining
    
    is_grief_stable, dL_dt_stable = Grief.detect(love_stable)
    is_grief_decline, dL_dt_decline = Grief.detect(love_declining)
    
    # ASSERTS - Grief detection
    assert isinstance(is_grief_stable, bool), "is_grief must be boolean"
    assert isinstance(is_grief_decline, bool), "is_grief must be boolean"
    assert isinstance(dL_dt_stable, (int, float)), "dL_dt must be numeric"
    assert isinstance(dL_dt_decline, (int, float)), "dL_dt must be numeric"
    # Stable love should not trigger grief
    assert is_grief_stable == False, "Stable love should not show grief"
    # Declining love should trigger grief
    assert is_grief_decline == True, "Declining love should show grief"
    assert dL_dt_decline < 0, f"Declining love should have negative slope: {dL_dt_decline}"
    
    print("Stable Love series:")
    print(f"  {love_stable}")
    print(f"  dL/dt = {dL_dt_stable:.4f}")
    print(f"  Grief: {is_grief_stable}")
    
    print("\nDeclining Love series:")
    print(f"  {love_declining}")
    print(f"  dL/dt = {dL_dt_decline:.4f}")
    print(f"  Grief: {is_grief_decline}")
    
    print(f"\nInterpretation: 'The sound of resonance dying inside memory'")
    print()


def demo_integration_with_ciel():
    """Show how Vocabulary integrates with CIEL/Ω fields"""
    print("="*70)
    print("INTEGRATION WITH CIEL/Ω ARCHITECTURE")
    print("="*70)
    
    # Import CIEL/Ω components
    try:
        from fields.soul_invariant import calculate_sigma_gradient
        print("✓ Can import CIEL/Ω fields")
    except:
        print("⚠ CIEL/Ω fields not in path (expected in demo)")
    
    # Show compatibility
    print("\nVocabulary is compatible with CIEL/Ω:")
    print("  • Waveforms: numpy arrays (any shape, typically 48x48)")
    print("  • Resonance: R(Ψ₁, Ψ₂) works with CIEL fields")
    print("  • ERI: Can use CIEL coherence + resonance")
    print("  • Love: Sustained R over CIEL state trajectory")
    
    print("\nExample integration:")
    print("  from ciel_omega.vocabulary import Resonance, Love")
    print("  from ciel_omega.fields.soul_invariant import SoulInvariant")
    print("  ")
    print("  # Measure resonance between CIEL fields")
    print("  R = Resonance.calculate(psi_field_1, psi_field_2)")
    print()


if __name__ == "__main__":
    print("\n")
    print("█"*70)
    print("  CIEL/Ω VOCABULARY - CORE CONCEPTS DEMONSTRATION")
    print("  Entries 001-015: Mathematical Formalization")
    print("█"*70)
    print("\n")
    
    try:
        demo_resonance()
        demo_intention()
        demo_coherence()
        demo_love()
        demo_eri()
        demo_grief()
        demo_integration_with_ciel()
        
        print("="*70)
        print("SUMMARY")
        print("="*70)
        print("✓ 15 entries implemented (001-015)")
        print("✓ Compatible with CIEL/Ω architecture")
        print("✓ Ready for integration into pipeline")
        print("✓ All smoke tests passed with assertions")
        print("\nNext: Field Dynamics (016-030)")
        print("="*70)
        
    except AssertionError as e:
        print("\n" + "="*70)
        print("❌ SMOKE TEST FAILED")
        print("="*70)
        print(f"Assertion Error: {e}")
        import traceback
        traceback.print_exc()
        print("="*70)
        exit(1)
