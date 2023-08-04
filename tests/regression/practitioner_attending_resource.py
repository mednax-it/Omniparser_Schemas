import json

from omniparser_schemas.parser.main import validate_ETL_parser

from .reg_globals.reference_urls import(
    ATTENDING_PRACTIONER_FULL_URL,
    URL,
    N_ATTENDING_PRACTIONER_FULL_URL,
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
)

from .reg_globals.practitioner_reg_globals import(
    PRACTITIONER_NPI_NUMBER,
    PRACTITIONER_IDENTIFIER_SYSTEM,
    PRACTITIONER_CODING_CODE,
    PRACTITIONER_CODING_DSIPLAY,
    PRACTITIONER_CODING_SYSTEM,
    PRACTITIONER_GIVEN_NAME,
    PRACTITIONER_FAMILY_NAME,
    N_PRACTITIONER_CODING_DSIPLAY,
)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.organization_reg_globals import(
    VALUE,
    N_VALUE
)

def practitioner_attending_test(resource_name, testfile ):
    validate_ETL_parser(resource_name, testfile)
    with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Practitioner"
        entries = fhir_bundle["entry"]
        filter_org = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
        PRAC_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/us-npi-id"
        attphys = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == PRAC_IDENTIFIER, filter_org))

        assert attphys[0]["fullUrl"] == ATTENDING_PRACTIONER_FULL_URL, "did not match organization resource full url"
        assert attphys[0]["request"]["ifNoneExist"] == f'identifier={PRAC_IDENTIFIER}|{MRN}-{VALUE}-{PRACTITIONER_NPI_NUMBER[0]}', "did not match practitioner identifier"
        assert attphys[0]["request"]["method"] == REQUEST_TYPE[1], "did not match request"
        assert attphys[0]["request"]["url"] == URL[4], "did not match URL"
        assert attphys[0]["resource"]["identifier"][0]["system"] == PRACTITIONER_IDENTIFIER_SYSTEM[0], "did not match practitioner identifier system"
        assert attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[0], "did not match practitioner code"
        assert attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM, "did not match practitioner coding system"
        assert attphys[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}-{PRACTITIONER_NPI_NUMBER[0]}', "did not match practitioner identifier value"
        assert attphys[0]["resource"]["identifier"][1]["system"] == PRACTITIONER_IDENTIFIER_SYSTEM[1], "did not match practitioner identifier system"
        assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[1], "did not match practitioner code"
        assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM, "did not match practitioner coding system"
        assert attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == PRACTITIONER_CODING_DSIPLAY, "did not match practitioner coding display"
        assert attphys[0]["resource"]["identifier"][1]["value"] == PRACTITIONER_NPI_NUMBER[0], "did not match practitioner identifier value"
        assert attphys[0]["resource"]["name"][0]["family"] == PRACTITIONER_FAMILY_NAME[0], "did not match practitioner family name"
        assert attphys[0]["resource"]["name"][0]["given"][0] == PRACTITIONER_GIVEN_NAME[0], "did not match practitioner given name"

        #negative test cases
        assert not attphys[0]["fullUrl"] == N_ATTENDING_PRACTIONER_FULL_URL, "negative test case failed"
        assert not attphys[0]["request"]["ifNoneExist"] == f'identifier={PRAC_IDENTIFIER}|{MRN}-{N_VALUE}-{PRACTITIONER_NPI_NUMBER[0]}', "negative test case failed"
        assert not attphys[0]["request"]["method"] == REQUEST_TYPE[0], "negative test case failed"
        assert not attphys[0]["request"]["url"] == URL[2], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][0]["system"] == PRACTITIONER_IDENTIFIER_SYSTEM[1], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[1],  "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM[1],  "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][0]["value"] == PRACTITIONER_NPI_NUMBER[1], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][1]["system"] == PRACTITIONER_IDENTIFIER_SYSTEM[0], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == PRACTITIONER_CODING_CODE[0], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == PRACTITIONER_CODING_SYSTEM[0], "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == N_PRACTITIONER_CODING_DSIPLAY, "negative test case failed"
        assert not attphys[0]["resource"]["identifier"][1]["value"] == PRACTITIONER_NPI_NUMBER[1], "negative test case failed"
        assert not attphys[0]["resource"]["name"][0]["family"] == PRACTITIONER_GIVEN_NAME, "negative test case failed"
        assert not attphys[0]["resource"]["name"][0]["given"][0] == PRACTITIONER_FAMILY_NAME, "negative test case failed"


    print("FHIR bundle attending practitioner resource tests were successful")