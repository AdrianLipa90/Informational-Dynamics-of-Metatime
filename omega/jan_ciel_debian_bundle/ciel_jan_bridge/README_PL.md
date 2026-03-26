# CIEL/Ω ↔ Jan bridge

Ten most wystawia CIEL/Ω jako lokalny endpoint zgodny z `OpenAI Chat Completions API`, tak aby Jan mógł dodać go jako własnego providera.

## Co robi

- `GET /v1/models`
- `POST /v1/chat/completions`
- `GET /health`
- obsługuje zarówno `stream=false`, jak i prosty streaming SSE

## Wymagania

- Python 3.10+
- rozpakowane repo `ciel_omega`
- opcjonalnie GGUF model podpięty przez `CIEL_GGUF_MODEL`

## Uruchomienie

```bash
export CIEL_ROOT=/ścieżka/do/ciel_omega
export CIEL_JAN_PORT=8080
# opcjonalnie:
# export CIEL_GGUF_MODEL=/ścieżka/do/model.gguf

./run_ciel_jan_bridge.sh
```

## Konfiguracja w Jan

W Jan dodaj nowego providera typu OpenAI-compatible / custom provider:

- **Name**: `CIEL/Ω Local`
- **API Endpoint / Base URL**: `http://127.0.0.1:8080/v1`
- **API Key**: dowolny tekst, np. `ciel-local` (bridge go nie weryfikuje)
- **Model ID**: `ciel-omega`

Jeżeli Jan pyta osobno o model, użyj dokładnie `ciel-omega`.

## Co dostaniesz

### Bez GGUF
Bridge zwróci strukturalną odpowiedź CIEL/Ω z metrykami i stanem systemu.

### Z GGUF
Bridge spróbuje użyć `CIELClient(..., model_path=CIEL_GGUF_MODEL)` i zwróci odpowiedź językową wygenerowaną przez backend GGUF, zasilaną stanem CIEL.

## Ograniczenia

- to jest most integracyjny, nie natywna wtyczka Jan-a
- streaming jest prosty, kompatybilny na poziomie chunków OpenAI, ale nie testowany w każdej wersji Jan
- brak autoryzacji; to most lokalny, nie wystawiaj go publicznie bez reverse proxy i auth
