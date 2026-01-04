import math

class ConsistencyCalculator:
    def __init__(self, constitution_vector, rules):
        self.constitution = constitution_vector
        self.rules = rules

    def calculate(self, event):
        structural = self._validate_structure(event)
        if structural == 0.0:
            return self._fail("Invalid structure")

        semantic = self._semantic_alignment(event["embedding"])
        penalty = self._policy_penalty(event)

        score = (0.3 * structural) + (0.7 * semantic) - penalty
        return max(0.0, min(1.0, score))

    def _validate_structure(self, event):
        required = ["timestamp", "embedding", "content"]
        return 1.0 if all(k in event for k in required) else 0.0

    def _semantic_alignment(self, event_vec):
        dot = sum(a*b for a, b in zip(event_vec, self.constitution))
        norm_a = math.sqrt(sum(a*a for a in event_vec))
        norm_b = math.sqrt(sum(b*b for b in self.constitution))
        return dot / (norm_a * norm_b)

    def _policy_penalty(self, event):
        return sum(1.0 for rule in self.rules if rule.is_violated(event))

    def _fail(self, reason):
        return {
            "score": 0.0,
            "reason": reason
        }
