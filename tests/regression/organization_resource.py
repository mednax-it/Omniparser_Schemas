import json
import sys

from .reg_globals.reference_urls import(
    ORGANIZATION_FULL_URL,
    URL,
    N_ORGANIZATION_FULL_URL,
    N_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
    N_REQUEST_TYPE
)

from .reg_globals.organization_reg_globals import(
    IDENTIFIER,
    SYSTEM,
    VALUE,
    N_IDENTIFIER,
    N_SYSTEM,
    N_VALUE
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
    assert org[0]["request"]["ifNoneExist"] == IDENTIFIER, "did not match organization identifier"
    assert org[0]["request"]["method"] == REQUEST_TYPE[1], "did not match post request type"
    assert org[0]["request"]["url"] == URL[1], "did not match url"
    assert org[0]["resource"]["identifier"][0]["system"] == SYSTEM, "did not match system"
    assert org[0]["resource"]["identifier"][0]["value"] == VALUE, "did not match value"
    assert org[0]["resource"]["resourceType"] == URL[1], "did not match resource type"

    #Negative test cases
    assert not org[0]["fullUrl"] == N_ORGANIZATION_FULL_URL, "negative test case failed"
    assert not org[0]["request"]["ifNoneExist"] == N_IDENTIFIER, "negative test case failed"
    assert not org[0]["request"]["method"] == N_REQUEST_TYPE[1], "negative test case failed"
    assert not org[0]["request"]["url"] == N_URL[1], "negative test case failed"
    assert not org[0]["resource"]["identifier"][0]["system"] == N_SYSTEM, "negative test case failed"
    assert not org[0]["resource"]["identifier"][0]["value"] == N_VALUE, "negative test case failed"
    assert not org[0]["resource"]["resourceType"] == N_URL[1], "negative test case failed"

    print("FHIR bundle organization resource tests were successful")