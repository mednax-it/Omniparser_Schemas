import sys

from http import HTTPStatus
import requests

#from omniparser_schemas.common.globals import(
#   UNIVERSAL_ETL_PARSER_CONTENT_SCHEMA,
#   UNIVERSAL_ETL_PARSER_URL,
#   REQUEST_TIMEOUT
#)
UNIVERSAL_ETL_PARSER_CONTENT_SCHEMA="hl7v2_default"
UNIVERSAL_ETL_PARSER_URL="https://universal-etl-parser.mdnxdev.com/"
REQUEST_TIMEOUT=90

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
