from .reg_globals.reference_urls import(
    ATTENDING_PRACTIONER_FULL_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
)

from .reg_globals.practitioner_reg_globals import(
    PRACTITIONER_NPI_NUMBER,
    PRACTITIONER_CODING_CODE,
    PRACTITIONER_CODING_DSIPLAY,
    PRACTITIONER_CODING_SYSTEM,
    PRACTITIONER_GIVEN_NAME,
    PRACTITIONER_FAMILY_NAME
)

from .reg_globals.patient_reg_global import(
    MRN
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

def practitioner_attending_test(resource_name, testfile, identifier_url, identifier_id):
    attphys = filter_resource(resource_name, testfile, identifier_url, identifier_id)
    assert attphys[0]["fullUrl"] == ATTENDING_PRACTIONER_FULL_URL, "did not match organization resource full url"
    assert attphys[0]["request"]["ifNoneExist"] == f'identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[10]}|{MRN}-{FACILITY_ID}-{PRACTITIONER_NPI_NUMBER[0]}', "did not match practitioner identifier"
    assert attphys[0]["request"]["method"] == REQUEST_TYPE[1], "did not match request"
    assert attphys[0]["request"]["url"] == RESOURCE_NAME[6], "did not match URL"
    assert attphys[0]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[10]}', "did not match practitioner identifier system"
    assert attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[0], "did not match practitioner code"
    assert attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM, "did not match practitioner coding system"
    assert attphys[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{FACILITY_ID}-{PRACTITIONER_NPI_NUMBER[0]}', "did not match practitioner identifier value"
    assert attphys[0]["resource"]["identifier"][1]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[11]}', "did not match practitioner identifier system"
    assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[1], "did not match practitioner code"
    assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM, "did not match practitioner coding system"
    assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == PRACTITIONER_CODING_DSIPLAY, "did not match practitioner coding display"
    assert attphys[0]["resource"]["identifier"][1]["value"] == PRACTITIONER_NPI_NUMBER[0], "did not match practitioner identifier value"
    assert attphys[0]["resource"]["name"][0]["family"] == PRACTITIONER_FAMILY_NAME[0], "did not match practitioner family name"
    assert attphys[0]["resource"]["name"][0]["given"][0] == PRACTITIONER_GIVEN_NAME[0], "did not match practitioner given name"

    #negative test cases
    assert not attphys[0]["fullUrl"] == PRACTITIONER_NPI_NUMBER[0], "negative test case failed"
    assert not attphys[0]["request"]["ifNoneExist"] == f'{MRN}-{PRACTITIONER_NPI_NUMBER[0]}', "negative test case failed"
    assert not attphys[0]["request"]["method"] == REQUEST_TYPE[0], "negative test case failed"
    assert not attphys[0]["request"]["url"] == IDENTIFIER_ID[2], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_ID[1], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[1],  "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM[1],  "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][0]["value"] == PRACTITIONER_NPI_NUMBER[1], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][1]["system"] == IDENTIFIER_ID[0], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[0], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM[0], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == REQUEST_TYPE[1], "negative test case failed"
    assert not attphys[0]["resource"]["identifier"][1]["value"] == PRACTITIONER_NPI_NUMBER[1], "negative test case failed"
    assert not attphys[0]["resource"]["name"][0]["family"] == PRACTITIONER_GIVEN_NAME, "negative test case failed"
    assert not attphys[0]["resource"]["name"][0]["given"][0] == PRACTITIONER_FAMILY_NAME, "negative test case failed"


    print("FHIR bundle attending practitioner resource tests were successful")