import math
from typing import List, Dict
from core.policy import RegulatoryPolicy

class PoCAEvaluator:
    """Implementation of ARI formula: C(Et) = 0.3*S + 0.7*SA - P"""
    
    # ARI calculation constants
    COMPLIANCE_THRESHOLD = 0.8  # Minimum ARI score for COMPLIANT status
    
    def __init__(self, constitution_vector: List[float]):
        self.constitution = constitution_vector
        self.weights = {"structural": 0.3, "semantic": 0.7}

    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag = math.sqrt(sum(a**2 for a in v1)) * math.sqrt(sum(b**2 for b in v2))
        return dot / mag if mag > 0 else 0.0

    def evaluate(self, agent_id: str, vector: List[float], valid_schema: bool):
        RegulatoryPolicy.check_halt_status(agent_id)
        
        si = 1.0 if valid_schema else 0.0
        sa = self.cosine_similarity(vector, self.constitution)
        penalty = RegulatoryPolicy.calculate_penalties(sa)
        
        ari = (self.weights["structural"] * si) + (self.weights["semantic"] * sa) - penalty
        return {
            "ari": max(0.0, ari), 
            "drift": 1.0 - sa, 
            "status": "COMPLIANT" if ari > self.COMPLIANCE_THRESHOLD else "RISK"
        }
