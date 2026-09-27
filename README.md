# JobMatch Agent

An end-to-end AI job-search platform, built as a portfolio project for AI
platform / MLOps engineering roles:

**job discovery → dedup → resume matching → tailored applications → tracking**,
with a production-minded twist — a cost-aware model router, an eval-gated
rollout pipeline, and full observability underneath a single-agent core.

## Why this exists

Most open-source job agents are thin prompt→API wrappers. This project explores
the *platform* side of AI systems:

| AI platform concern | Implementation here |
|---|---|
| Cost-aware LLM routing | `router/` — route by task type to the cheapest model that holds quality |
| Eval-gated rollout | `evalharness/` — prompt/model changes must pass evals (canary + regression) |
| Safe deployment | canary prompts, shadow scoring — release-safety thinking applied to AI |
| Observability | `observability/` — tracing, per-request token/cost accounting |
| Reproducible deploys | Docker, Helm, `eval` in CI |

## Architecture

```
                 ┌──────────────┐
                 │  Ingestion   │  Greenhouse / Lever / Ashby public APIs
                 └──────┬───────┘
                        ▼
                 ┌──────────────┐
                 │    Dedup     │  URL + simhash, Postgres
                 └──────┬───────┘
                        ▼
 ┌───────────┐   ┌──────────────┐   ┌───────────────┐
 │   vLLM    │──▶│ Model Router │──▶│ Eval Harness  │
 │(small LM) │   │  (FastAPI)   │   │               │
 └───────────┘   └──────┬───────┘   └───────────────┘
                        ▼
                 ┌──────────────┐
                 │   Workers    │  async pipeline: score, tailor, track
                 └──────────────┘
```

## Roadmap

- **M0** ✅ — repo skeleton, Docker, CI
- **M1** — scrapers (reuse OSS adapters) + dedup + resume-vs-JD scoring CLI
- **M2** — model router + eval harness + prompt canary (the core)
- **M3** — Helm deploy, Grafana dashboards, eval-in-CI, demo

## Quickstart (M0)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m jobmatch health
pytest
```

## License

MIT
