import base64

def b64_encode(text: str) -> str:
    raw = text.encode("utf-8")
    enc = base64.b64encode(raw)
    return enc.decode("utf-8")

def b64_decode(text: str) -> str:
    raw = text.strip().encode("utf-8")
    dec = base64.b64decode(raw, validate=True)
    return dec.decode("utf-8")


