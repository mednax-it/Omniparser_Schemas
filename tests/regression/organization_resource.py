from .reg_globals.reference_urls import(
    ORGANIZATION_FULL_URL,
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
)

from .reg_globals.organization_reg_globals import(
    FACILITY_ID
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from omniparser_schemas.parser.filter import filter_resource

def org_test(resource_name, testfile, identifier_url, identifier_id):
    org = filter_resource(resource_name, testfile, identifier_url, identifier_id)
    assert org[0]["fullUrl"] == ORGANIZATION_FULL_URL, "did not match organization resource full url"
    assert org[0]["request"]["ifNoneExist"] == f"identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[8]}|{FACILITY_ID}", "did not match organization identifier"
    assert org[0]["request"]["method"] == REQUEST_TYPE[1], "did not match post request type"
    assert org[0]["request"]["url"] == RESOURCE_NAME[4], "did not match url"
    assert org[0]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[8]}', "did not match system"
    assert org[0]["resource"]["identifier"][0]["value"] == FACILITY_ID, "did not match value"
    assert org[0]["resource"]["resourceType"] == RESOURCE_NAME[4], "did not match resource type"

    #Negative test cases
    assert not org[0]["fullUrl"] == IDENTIFIER_ID[3], "negative test case failed"
    assert not org[0]["request"]["ifNoneExist"] == ORGANIZATION_FULL_URL, "negative test case failed"
    assert not org[0]["request"]["method"] == REQUEST_TYPE[0], "negative test case failed"
    assert not org[0]["request"]["url"] == RESOURCE_NAME[1], "negative test case failed"
    assert not org[0]["resource"]["identifier"][0]["system"] == FACILITY_ID, "negative test case failed"
    assert not org[0]["resource"]["identifier"][0]["value"] == IDENTIFIER_URL, "negative test case failed"
    assert not org[0]["resource"]["resourceType"] == IDENTIFIER_ID[3], "negative test case failed"

    print("FHIR bundle organization resource tests were successful")