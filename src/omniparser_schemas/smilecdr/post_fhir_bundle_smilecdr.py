from http import HTTPStatus
import random
import string
import importlib

import requests

from omniparser_schemas.common.globals import(
   ROOT_URL
)
from omniparser_schemas.smilecdr.universal_etl_parser import fetch_parsed_text
from omniparser_schemas.smilecdr.smile_cdr_token import get_token

def postFHIRbunlde(mrn, facilityId):
   with importlib.resources.path("omniparser_schemas.smilecdr", "RegressionTestData.txt") as f:
      hl7content = f.read_text()

   # The universal parser need to have carriage return
   hl7content = hl7content.replace('\\r', '\r')

   # call universal utl parser
   fhir_bundle_from_hl7 = fetch_parsed_text(hl7content)

   # Replace test file MRN with unique MRN
   fhir_bundle_with_unique_mrn = fhir_bundle_from_hl7.replace('TEST333345038900', mrn)

   # Assign facilityid to fhir bundle
   fhir_bundle_with_unique_mrn = fhir_bundle_with_unique_mrn.replace('{{FacilityId}}', facilityId)

   # Remove first and last character of fhir bundle
   fhir_bundle_with_unique_mrn_format = fhir_bundle_with_unique_mrn[1:-1]

   # Get Smilecdr Token
   token = get_token()

   # Post the fhir bundle in smilecdr
   N=10
   request_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
   headers = {
                "Content-Type": "application/fhir+json",
                "accept": "application/json",
                "Authorization": f"Bearer {(token)}",
                "x-request-id": f"{request_id}",
             }
   base_url = f"{ROOT_URL}/fhir-request/"
   response = requests.post(base_url, headers=headers, data=fhir_bundle_with_unique_mrn_format)
   if response.status_code != HTTPStatus.OK:
        error_message = response.json()
        print(error_message)
        exit(1)

   return(response.json())
