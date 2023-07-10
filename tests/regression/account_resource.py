import json

from omniparser_schemas.parser.main import validate_ETL_parser

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ACCOUNT_FULL_URL,
    COVERAGE_FULL_URL_1,
    COVERAGE_FULL_URL_2,
    COVERAGE_FULL_URL_3,
    RELATED_PERSON_GUARANTOR_FULL_URL,
    REFERENCE_TYPE,
    N_PATIENT_FULL_URL,
    N_ACCOUNT_FULL_URL,
    N_COVERAGE_FULL_URL_1,
    N_COVERAGE_FULL_URL_2,
    N_COVERAGE_FULL_URL_3,
    N_RELATED_PERSON_GUARANTOR_FULL_URL,
    N_REFERENCE_TYPE
)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
    N_REQUEST_TYPE
)

from .reg_globals.account_reg_globals import(
    IDENTIFIER_SYSTEM,
    STATUS,
    ACCOUNT_CODE,
    ACCOUNT_DISPLAY,
    CODE_SYSTEM,
    N_IDENTIFIER_SYSTEM,
    N_STATUS,
    N_ACCOUNT_CODE,
    N_ACCOUNT_DISPLAY,
    N_CODE_SYSTEM
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

def acc_test(resource_name, testfile):
    validate_ETL_parser(resource_name, testfile)
    with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Account"
        entries = fhir_bundle["entry"]
        acc = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))

    assert acc[0]["fullUrl"] == ACCOUNT_FULL_URL, "did not match account URL"
    assert acc[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request type"
    assert acc[0]["request"]["url"] == f'Account?identifier=https://pediatrix.com/fhir/NamingSystem/patientAccount-id|{MRN}-{VALUE}', "did not match request url"
    assert acc[0]["resource"]["coverage"][0]["coverage"]["reference"] == COVERAGE_FULL_URL_1, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][0]["priority"] == 1,  "did not match priority"
    assert acc[0]["resource"]["coverage"][1]["coverage"]["reference"] == COVERAGE_FULL_URL_2, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][1]["priority"] == 2,  "did not match priority"
    assert acc[0]["resource"]["coverage"][2]["coverage"]["reference"] == COVERAGE_FULL_URL_3, "did not match coverage full URL"
    assert acc[0]["resource"]["coverage"][2]["priority"] == 3,  "did not match priority"
    assert acc[0]["resource"]["guarantor"][0]["party"]["reference"] == RELATED_PERSON_GUARANTOR_FULL_URL,  "did not match guarantor reference"
    assert acc[0]["resource"]["guarantor"][0]["party"]["type"] == REFERENCE_TYPE[5], "did not match reference type"
    assert acc[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM, "did not match indentifier system"
    assert acc[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}', "did not match identifier value"
    assert acc[0]["resource"]["resourceType"] == REFERENCE_TYPE[3], "did not match resource"
    assert acc[0]["resource"]["status"] == STATUS, "did not match status"
    assert acc[0]["resource"]["subject"][0]["reference"] == PATIENT_FULL_URL, "did not match reference URL"
    assert acc[0]["resource"]["subject"][0]["type"] == REFERENCE_TYPE[0], "did not match reference type"
    assert acc[0]["resource"]["type"]["coding"][0]["code"] == ACCOUNT_CODE, "did not match account code"
    assert acc[0]["resource"]["type"]["coding"][0]["display"] == ACCOUNT_DISPLAY, "did not match account display"
    assert acc[0]["resource"]["type"]["coding"][0]["system"] == CODE_SYSTEM, "did not match code system"

    # Negative test cases

    assert not acc[0]["fullUrl"] == N_ACCOUNT_FULL_URL, "negative test case failed"
    assert not acc[0]["request"]["method"] == N_REQUEST_TYPE[1], "negative test case failed"
    assert not acc[0]["request"]["url"] == f'Account?identifier=https://pediatrix.com/fhir/NamingSystem/patientAccount-id|{MRN}-{VALUE}-12345', "negative test case failed"
    assert not acc[0]["resource"]["coverage"][0]["coverage"]["reference"] == N_COVERAGE_FULL_URL_1, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][0]["priority"] == 3,  "negative test case failed"
    assert not acc[0]["resource"]["coverage"][1]["coverage"]["reference"] == N_COVERAGE_FULL_URL_2, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][1]["priority"] == 1,  "negative test case failed"
    assert not acc[0]["resource"]["coverage"][2]["coverage"]["reference"] == N_COVERAGE_FULL_URL_3, "negative test case failed"
    assert not acc[0]["resource"]["coverage"][2]["priority"] == 2,  "negative test case failed"
    assert not acc[0]["resource"]["guarantor"][0]["party"]["reference"] == N_RELATED_PERSON_GUARANTOR_FULL_URL,  "negative test case failed"
    assert not acc[0]["resource"]["guarantor"][0]["party"]["type"] == N_REFERENCE_TYPE[5], "negative test case failed"
    assert not acc[0]["resource"]["identifier"][0]["system"] == N_IDENTIFIER_SYSTEM, "negative test case failed"
    assert not acc[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}-12345', "negative test case failed"
    assert not acc[0]["resource"]["resourceType"] == N_REFERENCE_TYPE[3], "negative test case failed"
    assert not acc[0]["resource"]["status"] == N_STATUS, "negative test case failed"
    assert not acc[0]["resource"]["subject"][0]["reference"] == N_PATIENT_FULL_URL, "negative test case failed"
    assert not acc[0]["resource"]["subject"][0]["type"] == N_REFERENCE_TYPE[0], "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["code"] == N_ACCOUNT_CODE, "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["display"] == N_ACCOUNT_DISPLAY, "negative test case failed"
    assert not acc[0]["resource"]["type"]["coding"][0]["system"] == N_CODE_SYSTEM, "negative test case failed"

    print("FHIR bundle account resource tests were successful")