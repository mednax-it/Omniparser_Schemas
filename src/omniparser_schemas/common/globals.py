import os

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
AUD = "cdr_all_user_authorities"
ROOT_URL = os.environ["ROOT_URL"]

UNIVERSAL_ETL_PARSER_CONTENT_SCHEMA = "hl7v2_default"
UNIVERSAL_ETL_PARSER_URL = os.environ["UNIVERSAL_ETL_PARSER_URL"]
REQUEST_TIMEOUT = 90