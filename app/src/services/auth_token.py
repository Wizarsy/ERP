from itsdangerous import BadSignature, BadTimeSignature, SignatureExpired, URLSafeTimedSerializer
from src.config import CONFIG

def encodeToken(payload: any, req_type: str) -> str:
  gen = URLSafeTimedSerializer(CONFIG["token_secret_key"], req_type)
  return gen.dumps(payload)

def decodeToken(token: str, req_type: str, max_age: int = 1800) -> tuple:
  val = URLSafeTimedSerializer(CONFIG["token_secret_key"], req_type)
  try:
    return val.loads(token, max_age), True
  except SignatureExpired:
    return "token expired", False
  except BadSignature:
    return "invalid token", False
