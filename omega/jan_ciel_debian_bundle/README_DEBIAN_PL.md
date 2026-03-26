# CIEL/Ω + Jan — samowystarczalny bundle dla Debiana/Ubuntu

Ten bundle zawiera:
- `Jan_0.7.8_amd64.deb` — lokalny pakiet Jan dla Linux/Debian
- `ciel_omega/` — spatchowane repo CIEL/Ω
- `ciel_jan_bridge/` — lokalny bridge OpenAI-compatible
- `install_jan_debian.sh` — instaluje Jan z dołączonego `.deb`
- `start_jan_with_ciel_debian.sh` — uruchamia bridge i próbuje otworzyć Jan
- `stop_ciel_bridge.sh` — zatrzymuje bridge

## Szybki start

```bash
./install_jan_debian.sh
./start_jan_with_ciel_debian.sh
```

## Ustawienia providera w Jan

- Name: `CIEL/Ω Local`
- Base URL: `http://127.0.0.1:8080/v1`
  (jeżeli port 8080 jest zajęty, skrypt wybierze pierwszy wolny port od 8080 wzwyż i wypisze go w terminalu)
- API Key: `ciel-local`
- Model: `ciel-omega`

## Opcjonalne zmienne środowiskowe

```bash
export CIEL_JAN_PORT=8080
export CIEL_JAN_HOST=127.0.0.1
export CIEL_ROOT=/absolutna/sciezka/do/ciel_omega
export JAN_DEB=/absolutna/sciezka/do/Jan_0.7.8_amd64.deb
```

## Uwagi

- To jest bundle dla systemów Debian/Ubuntu.
- Jan instaluje się z dołączonego pliku `.deb`, bez pobierania z internetu.
- Do instalacji Jan potrzebujesz `sudo`.
