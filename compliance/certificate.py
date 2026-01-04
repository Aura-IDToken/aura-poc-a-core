# compliance/certificate.py

from dataclasses import dataclass
from typing import Dict, Any
import json
import hashlib


@dataclass(frozen=True)
class AuraEventCertificate:
    """
    Deterministic, compliance-ready representation of a single evaluated event.
    This object is the ONLY external-facing output of the PoCA core.
    """

    agent_id: str
    timestamp: str

    poca_score: float
    drift: float
    status: str

    merkle_root: str
    leaf_hash: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": "1.0.0",
            "agent_id": self.agent_id,
            "timestamp": self.timestamp,
            "poca": {
                "score": self.poca_score,
                "drift": self.drift,
                "status": self.status,
            },
            "audit": {
                "leaf_hash": self.leaf_hash,
                "merkle_root": self.merkle_root,
            },
        }

    def fingerprint(self) -> str:
        """
        Deterministic hash of the entire certificate.
        This is what can be anchored, signed, or published.
        """
        payload = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()
