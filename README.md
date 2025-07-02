# CustomGPTs Repository (WebUI / Modular-)

Dieses Repository dient sich als zentrales Basis kün alle deine CustomGPTßs (Module, Policies, API-spes) in der WebUI eingesetzt werden.

## Struktur

- `core/`       - Gemeinsame Logik, Policies, WebUI
- `gpts/`      - Alle CustomGPTßs als eigenständige Module/Plugins
- `apispecs/`  - APISpecs zentral, pro GPT
- `scripts/`   - Test/Migration/Setup
- `docs/`      - Developer-Dokumentation, Kallien, HowTos

- `.github/`    - GitHok [Workflows, Issue-Templates, etc]

- **SpielRENners:* *
Jeder customGPTer gibt eigenen Unterordner im `gpts/`, inkl. Konfig, Instruktionen. API-Specs in `apispecs/`, Nomens belieb).
