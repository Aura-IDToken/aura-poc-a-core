"""
Aura PoCA Core — Compliance Layer

This package is responsible for:
- Transforming PoCA Core results into compliance-ready artifacts
- Producing machine-readable (JSON) and human-readable (PDF/HTML) outputs
- Binding cryptographic audit proofs to semantic explanations

This layer does NOT:
- Make decisions
- Modify scores
- Perform policy enforcement

It is a pure output / representation layer.
"""

from .certificate import AuraEventCertificate
from .renderer import render_certificate

__all__ = [
    "AuraEventCertificate",
    "render_certificate",
]
