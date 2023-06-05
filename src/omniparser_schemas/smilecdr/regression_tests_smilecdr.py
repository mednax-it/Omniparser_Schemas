
from http import HTTPStatus
import random
import string
import requests
import json

from omniparser_schemas.common.globals import(
   ROOT_URL
)
from omniparser_schemas.smilecdr.smile_cdr_token import get_token
from omniparser_schemas.smilecdr.post_fhir_bundle_smilecdr import postFHIRbunlde

unique_mrn_number = random.randrange(0,999999999999)
unique_mrn_number = str(unique_mrn_number)
facilityId = "477"
token = get_token()

def regressionTest():
    response = postFHIRbunlde(unique_mrn_number, facilityId)
    # send the fhir request in smilecdr
    N=10
    request_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    headers = {
                "Content-Type": "application/fhir+json",
                "accept": "application/json",
                "Authorization": f"Bearer {(token)}",
                "x-request-id": f"{request_id}",
             }
    base_url = f"{ROOT_URL}/fhir-request/Patient?identifier=https://pediatrix.com/fhir/NamingSystem/mrn-id|{unique_mrn_number}&mrn-assigner:Organization.identifier-system-facilityId={facilityId}&_revinclude=Encounter:subject&_include:iterate=Encounter:practitioner&_revinclude:iterate=MessageHeader:focus&_revinclude=Coverage:beneficiary&_include:iterate=Coverage:payor&_revinclude=RelatedPerson:patient&_revinclude=Account:subject"
    response = requests.get(base_url, headers=headers)
    if response.status_code != HTTPStatus.OK:
        error_message = response.json()
        print(error_message)
        exit(1)
    with open("output_regression.json", "w") as regoutjson:
        json.dump(response.json(), regoutjson)

regressionTest()