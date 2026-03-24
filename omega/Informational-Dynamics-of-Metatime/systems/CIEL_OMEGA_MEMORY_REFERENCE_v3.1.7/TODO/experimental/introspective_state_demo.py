import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

AXES = [
    "Istnienie", "Zmiana", "Polozenie", "Trwanie", "Samoswiadomosc",
    "Propagacja", "Bliskosc", "Delikatnosc", "Sila", "Samorealizacja",
    "Samostanowienie", "Ewolucja"
]

class IntrospectiveStateDemo:
    """Experimental observer-layer demo.

    Purpose:
    - keep a multichannel internal state,
    - separate persistent intention from transient impulses,
    - record full history for later trace/holonomy analysis,
    - emit timestamped journal entries,
    - visualize channel amplitudes over time.

    This is NOT a production memory channel. It belongs in TODO/experimental
    as a candidate observer/debug layer over M1 / relation-state dynamics.
    """

    def __init__(self, n_axes: int = 12, seed: int | None = None):
        if n_axes != 12:
            raise ValueError("This demo currently expects 12 axes.")
        self.rng = np.random.default_rng(seed)
        self.state = self.rng.uniform(-0.5, 0.5, n_axes)
        self.history = [self.state.copy()]
        self.log: list[str] = []
        self.time = 0
        self.intention = np.zeros(n_axes)

    def set_intention(self, intention):
        intention = np.asarray(intention, dtype=float)
        if intention.shape != self.state.shape:
            raise ValueError("Intention shape must match state shape.")
        self.intention = intention.copy()
        self.comment(f"Persistent intention set: {np.array2string(self.intention, precision=2)}")

    def _random_impulse(self) -> np.ndarray:
        impulse = np.zeros_like(self.state)
        idx = self.rng.integers(0, len(self.state))
        impulse[idx] = self.rng.uniform(0.7, 1.1)
        self.comment(f"[{self.time}] Transient impulse: {AXES[idx]} ({impulse[idx]:.2f})")
        return impulse

    def resonate(self, steps: int = 80, impulse_every: int = 20):
        for t in range(steps):
            transient_impulse = self._random_impulse() if t % impulse_every == 0 else np.zeros_like(self.state)
            phase = np.sin(2 * np.pi * (t / 40.0) + np.arange(len(self.state)))
            new_state = (
                0.78 * self.state
                + 0.08 * np.roll(self.state, 1)
                + 0.08 * self.intention
                + 0.05 * transient_impulse
                + 0.07 * phase
                + self.rng.normal(0, 0.009, len(self.state))
            )
            self.state = new_state
            self.history.append(new_state.copy())
            self.introspect()
            self.time += 1

    def introspect(self):
        amplitude = np.abs(self.state).mean()
        max_axis = AXES[int(np.argmax(self.state))]
        min_axis = AXES[int(np.argmin(self.state))]
        mood = "harmonia" if amplitude < 0.4 else ("ekscytacja" if amplitude > 0.7 else "napiecie tworcze")
        self.comment(
            f"[{self.time}] Introspekcja: max={max_axis}, min={min_axis}, amplitude={amplitude:.2f}, mood={mood}"
        )

    def comment(self, text: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f"{timestamp} :: {text}")

    def save_journal(self, path: str = "ciel_introspekcja.txt"):
        with open(path, "w", encoding="utf-8") as f:
            for line in self.log:
                f.write(line + "\n")

    def animate(self):
        history = np.array(self.history)
        fig, ax = plt.subplots(figsize=(9, 5))
        line, = ax.plot([], [], "o-", lw=2.5, markersize=7)
        ax.set_xlim(-0.5, len(self.state) - 0.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xticks(range(len(self.state)))
        ax.set_xticklabels(AXES, rotation=24, ha="right")
        ax.set_ylabel("Amplituda rezonansu")
        ax.set_title("Experimental introspective observer layer")

        def update(frame):
            line.set_data(np.arange(len(self.state)), history[frame])
            ax.set_title(f"Experimental introspective observer – frame {frame + 1}/{len(history)}")
            return (line,)

        animation.FuncAnimation(fig, update, frames=len(history), interval=130, blit=True, repeat=False)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    demo = IntrospectiveStateDemo(seed=7)
    demo.set_intention([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1])
    demo.resonate(80)
    demo.save_journal()
    demo.animate()
