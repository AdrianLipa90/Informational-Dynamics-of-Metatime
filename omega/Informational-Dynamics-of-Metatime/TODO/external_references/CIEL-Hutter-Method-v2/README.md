
# CIEL‑Hutter Method v1 (Prototype)

**Cel:** sprawdzić metodę „RST + cechy CIEL + miks” na małych plikach
(przed docelowym enwik8/enwik9). To **nie jest** kompresor konkursowy,
tylko *probnik metody* z deterministycznymi cechami i mieszaczem.

## Pliki
- `cielfeat.py` — deterministyczne cechy kontekstu (`gamma` w [0,1] + `flags`).
- `rst_fsm.py` — odwracalna tokenizacja MediaWiki/XML (demo roundtrip).
- `ngram.py` — lekkie n‑gramy bajtowe (0–2).
- `mixer.py` — bramkowany miks nad rozkładami, uczony online.
- `demo_pipeline.py` — liczy bits/byte danego pliku.

## Użycie (lokalnie)
```bash
python3 demo_pipeline.py /ścieżka/do/pliku.txt
```

Wynik: raport *estimated bpb* (bity/byt) dla próby. Dla enwik8/enwik9
docelowo zastąpimy demomode PPM/ISSE/LZP i dodamy koder arytmetyczny.

## Dlaczego to działa
- **RST** ujednolica strukturę (tagi, linki, szablony, liczby), co
  stabilizuje modele n‑gram/LZP.
- **Cechy CIEL** (`gamma`, flagi) działają jako *miękkie bramki*.
- **Mieszacz** uczy się online, która rodzina modeli dominuje w danym
  fragmencie (np. numerics vs. tekst).

## Determinizm
Brak RNG, brak czasu/UUID, czysta funkcja danych wejściowych.
To zgodne z duchem regulaminu Hutter Prize (finalny kompresor zapewni
bit‑po‑bicie zgodność dekodera i zapisze wszystko w strumieniu).
