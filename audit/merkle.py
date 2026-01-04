import hashlib

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

class MerkleTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.root = self._build(leaves)

    def _build(self, nodes):
        if len(nodes) == 1:
            return nodes[0]

        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i+1] if i+1 < len(nodes) else left
            next_level.append(sha256(left + right))
        return self._build(next_level)
