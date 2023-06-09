import json
import sys

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ORGANIZATION_FULL_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE
)

def org_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Organization"
        entries = fhir_bundle["entry"]
        filter_org = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
        ORG_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/facilityId-id"
        org = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == ORG_IDENTIFIER, filter_org))

    assert org[0]["fullUrl"] == ORGANIZATION_FULL_URL, "did not match organization resource full url"
    assert org[0]["request"]["method"] == REQUEST_TYPE[1], "did not match post request type"
    print("FHIR bundle organization resource tests were successful")
