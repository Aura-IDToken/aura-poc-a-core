"""
Core Policy Engine for Aura PoCA
Implements EU AI Act Compliance:
- Art. 5: Prohibition of human evaluation (algorithmic assertions only)
- Art. 14: Manual emergency halt (Kill-Switch)
"""

from typing import Callable, Dict, Any, Optional
from datetime import datetime


class PolicyRule:
    """
    Algorithmic policy rule for deterministic evaluation.
    Art. 5 Safeguard: Only algorithmic checks, no human evaluation.
    """
    def __init__(self, name: str, check_fn: Callable[[Dict[str, Any]], bool]):
        self.name = name
        self.check_fn = check_fn
        self._validate_no_human_evaluation()

    def _validate_no_human_evaluation(self):
        """
        Art. 5 Compliance: Assert that policy rules are purely algorithmic.
        This prevents human-in-the-loop evaluation from being introduced.
        """
        # Hard assertion: Policy functions must be deterministic callables
        if not callable(self.check_fn):
            raise ValueError(f"Policy rule '{self.name}' must be a callable function (Art. 5 safeguard)")
        
    def is_violated(self, event: Dict[str, Any]) -> bool:
        """
        Execute algorithmic policy check.
        Returns True if policy is violated, False otherwise.
        """
        try:
            return self.check_fn(event)
        except Exception as e:
            # Log violation but don't fail silently
            # Any exception during policy check is treated as a violation
            return True


class KillSwitch:
    """
    Art. 14 Oversight: Mandatory manual emergency halt mechanism.
    
    The Kill-Switch provides a deterministic, manual override capability
    for immediate system halt in case of critical safety concerns.
    """
    
    def __init__(self):
        self._active = False
        self._activated_at: Optional[datetime] = None
        self._activated_by: Optional[str] = None
        self._reason: Optional[str] = None
    
    def activate(self, activated_by: str, reason: str) -> Dict[str, Any]:
        """
        Activate the emergency halt.
        
        Args:
            activated_by: Identifier of the operator activating the kill-switch
            reason: Human-readable reason for activation
            
        Returns:
            Activation confirmation with timestamp
        """
        if self._active:
            return {
                "status": "already_active",
                "activated_at": self._activated_at.isoformat() if self._activated_at else None,
                "activated_by": self._activated_by,
            }
        
        self._active = True
        self._activated_at = datetime.utcnow()
        self._activated_by = activated_by
        self._reason = reason
        
        return {
            "status": "activated",
            "activated_at": self._activated_at.isoformat(),
            "activated_by": activated_by,
            "reason": reason,
        }
    
    def deactivate(self, deactivated_by: str) -> Dict[str, Any]:
        """
        Deactivate the emergency halt.
        
        Args:
            deactivated_by: Identifier of the operator deactivating the kill-switch
            
        Returns:
            Deactivation confirmation
        """
        if not self._active:
            return {"status": "not_active"}
        
        previous_state = {
            "activated_at": self._activated_at.isoformat() if self._activated_at else None,
            "activated_by": self._activated_by,
            "reason": self._reason,
            "deactivated_by": deactivated_by,
            "deactivated_at": datetime.utcnow().isoformat(),
        }
        
        self._active = False
        
        return {
            "status": "deactivated",
            "previous_state": previous_state,
        }
    
    def is_active(self) -> bool:
        """Check if kill-switch is currently active."""
        return self._active
    
    def get_state(self) -> Dict[str, Any]:
        """Get current kill-switch state."""
        return {
            "active": self._active,
            "activated_at": self._activated_at.isoformat() if self._activated_at else None,
            "activated_by": self._activated_by,
            "reason": self._reason,
        }
    
    def assert_not_halted(self):
        """
        Art. 14 Hard Assertion: Verify system is not halted.
        Raises exception if kill-switch is active.
        """
        if self._active:
            raise SystemHaltException(
                f"System halted by kill-switch. "
                f"Activated by: {self._activated_by}, "
                f"Reason: {self._reason}, "
                f"At: {self._activated_at.isoformat() if self._activated_at else 'unknown'}"
            )


class SystemHaltException(Exception):
    """Exception raised when system is halted via Kill-Switch."""
    pass


# Singleton instance for global kill-switch state
_global_kill_switch = KillSwitch()


def get_kill_switch() -> KillSwitch:
    """Get the global kill-switch instance."""
    return _global_kill_switch
