"""M2: eval harness — eval-gated rollout.

Prompt / model changes must pass the labeled eval set (incl. canary
comparison vs. the current production prompt) before they ship.
Mirrors release-safety practice: shadow -> canary -> full rollout.
"""
