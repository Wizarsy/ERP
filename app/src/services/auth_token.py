from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from src.config import CONFIG


def encodeToken(payload: any, req_type: str) -> str:
  gen = URLSafeTimedSerializer(CONFIG["token_secret_key"], req_type)
  return gen.dumps(payload)

def decodeToken(token: str, req_type: str, max_age: int = 1800) -> dict[bool, str]:
  val = URLSafeTimedSerializer(CONFIG["token_secret_key"], req_type)
  try:
    return {"status": True,
            "info": val.loads(token, max_age)}
  except SignatureExpired:
    return {"status": False,
            "info": "token expired"}
  except BadSignature:
    return {"status": False,
            "info": "invalid token"}