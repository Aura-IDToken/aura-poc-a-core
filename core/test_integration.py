"""
Integration test to verify core components work together:
- PoCAEvaluator (core/evaluator.py)
- RegulatoryPolicy (core/policy.py)
- MerkleAttestor (core/merkle.py)
"""

import unittest
from core.evaluator import PoCAEvaluator
from core.policy import RegulatoryPolicy
from core.merkle import MerkleAttestor


class TestIntegration(unittest.TestCase):
    """Integration test for AURA-IDTOKEN core components"""
    
    def setUp(self):
        RegulatoryPolicy.HALTED_AGENTS.clear()
        self.constitution = [0.5, 0.3, 0.8, 0.1] * 4  # 16-dim vector
        self.evaluator = PoCAEvaluator(self.constitution)
        self.attestor = MerkleAttestor()
    
    def test_complete_workflow(self):
        """Test complete workflow: validation -> evaluation -> ETC generation"""
        # Step 1: Validate target type (Art. 5)
        target_type = "MACHINE_ACCOUNT"
        RegulatoryPolicy.validate_target(target_type)
        
        # Step 2: Evaluate agent
        agent_id = "agent_integration_001"
        vector = [0.5, 0.3, 0.8, 0.1] * 4  # Similar to constitution
        valid_schema = True
        
        ari_result = self.evaluator.evaluate(agent_id, vector, valid_schema)
        
        # Step 3: Generate Event Trust Certificate (ETC)
        etc = self.attestor.generate_etc(ari_result)
        
        # Verify complete flow
        self.assertIn("ari", ari_result)
        self.assertIn("certificate", etc)
        self.assertTrue(etc["certificate"].startswith("AURA-ETC-"))
        
        # Verify ARI is compliant
        self.assertEqual(ari_result["status"], "COMPLIANT")
    
    def test_workflow_with_human_rejection(self):
        """Ensure workflow fails when attempting to score humans (Art. 5)"""
        with self.assertRaises(AssertionError) as context:
            RegulatoryPolicy.validate_target("HUMAN")
        
        self.assertIn("Human scoring is strictly prohibited", str(context.exception))
    
    def test_workflow_with_emergency_halt(self):
        """Test workflow with human oversight kill-switch (Art. 14)"""
        agent_id = "agent_integration_002"
        
        # Emergency halt
        RegulatoryPolicy.emergency_halt(agent_id)
        
        # Attempt evaluation
        vector = [0.5] * 16
        with self.assertRaises(Exception) as context:
            self.evaluator.evaluate(agent_id, vector, True)
        
        self.assertIn("POLICY_HALT", str(context.exception))


if __name__ == '__main__':
    unittest.main()
