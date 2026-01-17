class RegulatoryPolicy:
    """Tarcza prawna EU AI Act (Art. 5, 14)"""
    HALTED_AGENTS = set()

    @staticmethod
    def validate_target(target_type: str):
        # Art. 5: Zakaz social scoringu ludzi
        assert target_type == "MACHINE_ACCOUNT", "CRITICAL: Human scoring is strictly prohibited."

    @staticmethod
    def emergency_halt(agent_id: str):
        # Art. 14: Nadzór ludzki (Kill-Switch)
        RegulatoryPolicy.HALTED_AGENTS.add(agent_id)

    @staticmethod
    def check_halt_status(agent_id: str):
        if agent_id in RegulatoryPolicy.HALTED_AGENTS:
            raise Exception("POLICY_HALT: Operation stopped by human oversight.")

    @staticmethod
    def calculate_penalties(sa_score: float) -> float:
        # Kara za nagły dryf behawioralny (Sim < 0.7)
        return 1.5 if sa_score < 0.7 else 0.0


class PolicyRule:
    def __init__(self, name, check_fn):
        self.name = name
        self.check_fn = check_fn

    def is_violated(self, event):
        return self.check_fn(event)
