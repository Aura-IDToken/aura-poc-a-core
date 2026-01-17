import math

class ConsistencyCalculator:
    """
    Agent Reliability Index (ARI) Calculator
    
    Implements the Aura Protocol mathematical foundation:
    ARI = 0.3 * StructuralIntegrity + 0.7 * SemanticAlignment - Penalties
    
    Where:
    - StructuralIntegrity: Binary validation of event structure
    - SemanticAlignment: Cosine similarity (<=>) in ℝ¹⁵³⁶ space
    - Penalties: Policy violation penalties
    
    SCOPE: MACHINE_ACCOUNT entities only
    PROHIBITION: Human profiling or biometric data processing (AI Act Art. 5)
    DETERMINISM: Same input → Same ARI (required for Proof of Consistent Agency)
    """
    def __init__(self, constitution_vector, rules):
        self.constitution = constitution_vector
        self.rules = rules

    def calculate(self, event):
        """
        Calculate Agent Reliability Index (ARI) for an event.
        
        Returns: ARI score ∈ [0.0, 1.0]
        """
        structural = self._validate_structure(event)
        if structural == 0.0:
            return self._fail("Invalid structure")

        semantic = self._semantic_alignment(event["embedding"])
        penalty = self._policy_penalty(event)

        # ARI Formula: 0.3 * StructuralIntegrity + 0.7 * SemanticAlignment - Penalties
        ari = (0.3 * structural) + (0.7 * semantic) - penalty
        return max(0.0, min(1.0, ari))

    def _validate_structure(self, event):
        """Validate structural integrity of event."""
        required = ["timestamp", "embedding", "content"]
        return 1.0 if all(k in event for k in required) else 0.0

    def _semantic_alignment(self, event_vec):
        """
        Calculate semantic alignment via cosine similarity in ℝ¹⁵³⁶ space.
        Returns: Cosine similarity ∈ [-1.0, 1.0], normalized to [0.0, 1.0]
        """
        dot = sum(a*b for a, b in zip(event_vec, self.constitution))
        norm_a = math.sqrt(sum(a*a for a in event_vec))
        norm_b = math.sqrt(sum(b*b for b in self.constitution))
        # Cosine similarity, normalized from [-1, 1] to [0, 1]
        cosine_sim = dot / (norm_a * norm_b)
        return (cosine_sim + 1.0) / 2.0

    def _policy_penalty(self, event):
        """Calculate penalty from policy violations."""
        return sum(1.0 for rule in self.rules if rule.is_violated(event))

    def _fail(self, reason):
        """Return failure result with ARI = 0.0"""
        return {
            "ari": 0.0,
            "reason": reason
        }
