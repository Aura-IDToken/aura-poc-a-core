class PolicyRule:
    def __init__(self, name, check_fn):
        self.name = name
        self.check_fn = check_fn

    def is_violated(self, event):
        return self.check_fn(event)
