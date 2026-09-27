"""M2: cost-aware model router.

Routes each request to the cheapest model that holds quality:
classification / triage -> vLLM self-hosted small model,
generation (cover letters, tailored bullets) -> large API model.
Every decision is logged with cost/latency/quality for the dashboard.
"""
