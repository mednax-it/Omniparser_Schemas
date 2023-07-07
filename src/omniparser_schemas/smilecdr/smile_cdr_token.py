import logging
from datetime import datetime, timedelta

import requests
import jwt

from omniparser_schemas.common.globals import(
   CLIENT_ID,
   CLIENT_SECRET,
   AUD,
   ROOT_URL
)

TOKEN = None

def expiration(token):
    return datetime.fromtimestamp(
            jwt.decode(token, options={"verify_signature": False, "verify_aud": False})[
            "exp"
        ]
    )

def valid(token):
    if token is None:
        return False
    try:
        return expiration(token) - timedelta(minutes=30) > datetime.now()
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidAudienceError:
        logging.error(f'token in error: [{token}]')
        return False

def get_token():
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": AUD,
        "grant_type": "client_credentials",
    }
    header_for_post = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        f"{ROOT_URL}/smartauth/oauth/token",
        data=payload,
        headers=header_for_post,
    )
    return response.json()["access_token"]
