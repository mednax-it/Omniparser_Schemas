import sys
import os
import requests
from omniparser_schemas.common.globals import(
    PARSER_SCHEMA,
    PARSER_TIMEOUT
)
from http import HTTPStatus

UNIVERSAL_ETL_PARSER_CONTENT_SCHEMA=PARSER_SCHEMA
UNIVERSAL_ETL_PARSER_URL=os.environ['PARSER']
REQUEST_TIMEOUT=PARSER_TIMEOUT

def fetch_parsed_text(text_to_parse):
    headers = {"Content-Schema": UNIVERSAL_ETL_PARSER_CONTENT_SCHEMA}

    http_response = requests.post(
        url=UNIVERSAL_ETL_PARSER_URL,
        headers=headers,
        data=text_to_parse,
        timeout=REQUEST_TIMEOUT,
    )

    if http_response.status_code != HTTPStatus.OK:
        error_message = http_response.status_code
        print(error_message)
        exit(1)

    return http_response.text
