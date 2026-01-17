from .merkle import sha256

def verify_proof(leaf, proof, root):
    current = leaf
    for sibling, direction in proof:
        current = sha256(
            sibling + current if direction == "left" else current + sibling
        )
    return current == root
