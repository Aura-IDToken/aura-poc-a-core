def embed_text(text: str):
    """
    Placeholder for deterministic embedding.
    MUST be frozen + reproducible in production.
    """
    return [float(ord(c) % 32) / 32.0 for c in text][:32]
