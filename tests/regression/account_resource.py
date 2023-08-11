from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ACCOUNT_FULL_URL,
    COVERAGE_FULL_URL_1,
    COVERAGE_FULL_URL_2,
    COVERAGE_FULL_URL_3,
    RELATED_PERSON_GUARANTOR_FULL_URL,
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
)

from .reg_globals.account_reg_globals import(
    STATUS,
    ACCOUNT_CODE,
    ACCOUNT_DISPLAY,
    CODE_SYSTEM
)

from .reg_globals.organization_reg_globals import(
    FACILITY_ID
)

from omniparser_schemas.parser.filter import filter_resource

def acc_test(resource_name, testfile, identifier_url, identifier_id):
    acc = filter_resource(resource_name, testfile, identifier_url, identifier_id)
    assert acc[0]["fullUrl"] == ACCOUNT_FULL_URL, "did not match account URL"
    assert acc[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request type"
    assert acc[0]["request"]["url"] == f'{RESOURCE_NAME[0]}?identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[0]}|{MRN}-{FACILITY_ID}', "did not match request url"
    assert acc[0]["resource"]["coverage"][0]["coverage"]["reference"] == COVERAGE_FULL_URL_1, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][0]["priority"] == 1,  "did not match priority"
    assert acc[0]["resource"]["coverage"][1]["coverage"]["reference"] == COVERAGE_FULL_URL_2, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][1]["priority"] == 2,  "did not match priority"
    assert acc[0]["resource"]["coverage"][2]["coverage"]["reference"] == COVERAGE_FULL_URL_3, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][2]["priority"] == 3,  "did not match priority"
    assert acc[0]["resource"]["guarantor"][0]["party"]["reference"] == RELATED_PERSON_GUARANTOR_FULL_URL,  "did not match guarantor reference"
    assert acc[0]["resource"]["guarantor"][0]["party"]["type"] == RESOURCE_NAME[7], "did not match reference type"
    assert acc[0]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[0]}', "did not match indentifier system"
    assert acc[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{FACILITY_ID}', "did not match identifier value"
    assert acc[0]["resource"]["resourceType"] == RESOURCE_NAME[0], "did not match resource"
    assert acc[0]["resource"]["status"] == STATUS, "did not match status"
    assert acc[0]["resource"]["subject"][0]["reference"] == PATIENT_FULL_URL, "did not match reference URL"
    assert acc[0]["resource"]["subject"][0]["type"] == RESOURCE_NAME[5], "did not match reference type"
    assert acc[0]["resource"]["type"]["coding"][0]["code"] == ACCOUNT_CODE, "did not match account code"
    assert acc[0]["resource"]["type"]["coding"][0]["display"] == ACCOUNT_DISPLAY, "did not match account display"
    assert acc[0]["resource"]["type"]["coding"][0]["system"] == CODE_SYSTEM, "did not match code system"

    # Negative test cases
    assert not acc[0]["fullUrl"] == PATIENT_FULL_URL, "negative test case failed"
    assert not acc[0]["request"]["method"] == REQUEST_TYPE[1], "negative test case failed"
    assert not acc[0]["request"]["url"] == {MRN}-{FACILITY_ID}, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][0]["coverage"]["reference"] == RELATED_PERSON_GUARANTOR_FULL_URL, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][0]["priority"] == 3,  "negative test case failed"
    assert not acc[0]["resource"]["coverage"][1]["coverage"]["reference"] == ACCOUNT_FULL_URL, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][1]["priority"] == 1,  "negative test case failed"
    assert not acc[0]["resource"]["coverage"][2]["coverage"]["reference"] == PATIENT_FULL_URL, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][2]["priority"] == 2,  "negative test case failed"
    assert not acc[0]["resource"]["guarantor"][0]["party"]["reference"] == ACCOUNT_FULL_URL,  "negative test case failed"
    assert not acc[0]["resource"]["guarantor"][0]["party"]["type"] == RESOURCE_NAME[0], "negative test case failed"
    assert not acc[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_URL, "negative test case failed"
    assert not acc[0]["resource"]["identifier"][0]["value"] == f'{FACILITY_ID}-{MRN}', "negative test case failed"
    assert not acc[0]["resource"]["resourceType"] == RESOURCE_NAME[3], "negative test case failed"
    assert not acc[0]["resource"]["status"] == 1, "negative test case failed"
    assert not acc[0]["resource"]["subject"][0]["reference"] == ACCOUNT_FULL_URL, "negative test case failed"
    assert not acc[0]["resource"]["subject"][0]["type"] == RESOURCE_NAME[3], "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["code"] == CODE_SYSTEM, "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["display"] == ACCOUNT_CODE, "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["system"] == ACCOUNT_DISPLAY, "negative test case failed"

    print("FHIR bundle account resource tests were successful")