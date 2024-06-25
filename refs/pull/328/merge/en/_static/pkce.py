import hashlib
import base64
import re

def get_pkce(code_challenge_method: str = "S256", code_challenge_length: int = 64):
    hashers = {"S256": hashlib.sha256}

    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

    code_challenge = hashers.get(code_challenge_method)(
        code_verifier.encode("utf-8")
    ).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")

    return {
        "code_verifier": code_verifier,
        "code_challenge": code_challenge,
        "code_challenge_method": code_challenge_method,
    }