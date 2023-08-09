import json
from datetime import datetime

from .reg_globals.claim_reg_globals import(
    CLAIM_IDENTIFIER_SYSTEM,
    CLAIM_AUTH_NUMBER,
    CLAIM_SEQUENCE,
    CLAIM_STATUS,
    CLAIM_CODE,
    CLAIM_CODE_SYSTEM,
    CLAIM_CODE_DISPLAY,
    CLAIM_USE
)

from .reg_globals.reference_urls import(
   CLAIM_RESOURCE_FULL_URL_2,
   COVERAGE_FULL_URL_2,
   PATIENT_FULL_URL,
   ORGANIZATION_FULL_URL
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

from .reg_globals.reference_urls import(
    URL
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

from .reg_globals.patient_reg_global import(
    MRN
)

from omniparser_schemas.parser.main import validate_ETL_parser

def claim_2_test(resource_name, testfile):
    if(testfile == "1"):
        DATE_TIME_NOW = datetime.now()
        CURRENT_DATE = DATE_TIME_NOW.strftime("%Y-%m-%d")
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "Claim"
            entries = fhir_bundle["entry"]
            filter_cov = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            CLAIM_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/claim-id"
            claim = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == CLAIM_IDENTIFIER, filter_cov))

            assert claim[1]["fullUrl"] == CLAIM_RESOURCE_FULL_URL_2, "did not match full url"
            assert claim[1]["request"]["url"] == f'Claim?identifier={CLAIM_IDENTIFIER_SYSTEM}|{MRN}-{VALUE}-{CLAIM_AUTH_NUMBER[1]}', "did not match request url"
            CLAIM_DATE = claim[1]["resource"]["created"]
            CREATED_DATE = CLAIM_DATE[:10]
            assert CURRENT_DATE == CREATED_DATE, "did not match claim created date"
            assert claim[1]["resource"]["identifier"][0]["system"] == CLAIM_IDENTIFIER_SYSTEM, "did not match claim identifier system"
            assert claim[1]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}-{CLAIM_AUTH_NUMBER[1]}', "did not match claim value"
            assert claim[1]["resource"]["insurance"][0]["coverage"]["reference"] == COVERAGE_FULL_URL_2, "did not match coverage URL"
            assert claim[1]["resource"]["insurance"][0]["coverage"]["type"] == URL[5], "did not match coverage type"
            assert claim[1]["resource"]["insurance"][0]["focal"] == 1, "did not match focal"
            assert claim[1]["resource"]["insurance"][0]["preAuthRef"][0] == CLAIM_AUTH_NUMBER[1], "did not match preAuthRef"
            assert claim[1]["resource"]["insurance"][0]["sequence"] == CLAIM_SEQUENCE, "did not match insurance sequence"
            assert claim[1]["resource"]["patient"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
            assert claim[1]["resource"]["patient"]["type"] == URL[0], "did not match patient type"
            assert claim[1]["resource"]["priority"]["coding"][0]["code"] == CLAIM_CODE[0], "did not match claim code"
            assert claim[1]["resource"]["priority"]["coding"][0]["system"] == CLAIM_CODE_SYSTEM[0], "did not match coding system"
            assert claim[1]["resource"]["provider"]["reference"] == ORGANIZATION_FULL_URL, "did not match provider "
            assert claim[1]["resource"]["provider"]["type"] == URL[1]
            assert claim[1]["resource"]["status"] == CLAIM_STATUS
            assert claim[1]["resource"]["type"]["coding"][0]["code"] == CLAIM_CODE[1]
            assert claim[1]["resource"]["type"]["coding"][0]["display"] == CLAIM_CODE_DISPLAY
            assert claim[1]["resource"]["type"]["coding"][0]["system"] == CLAIM_CODE_SYSTEM[1]
            assert claim[1]["resource"]["use"] == CLAIM_USE

            #Negative test cases
            assert not claim[1]["fullUrl"] == ORGANIZATION_FULL_URL, "did not match full url"
            assert not claim[1]["request"]["url"] == f'Claim?identifier={CLAIM_IDENTIFIER_SYSTEM}|{MRN}-{VALUE}'
            CLAIM_DATE = claim[1]["resource"]["created"]
            CREATED_DATE = CLAIM_DATE[:9]
            assert not CURRENT_DATE == CREATED_DATE
            assert not claim[1]["resource"]["identifier"][0]["system"] == MRN, "negative test case failed"
            assert not claim[1]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}', "negative test case failed"
            assert not claim[1]["resource"]["insurance"][0]["coverage"]["reference"] == ORGANIZATION_FULL_URL, "negative test case failed"
            assert not claim[1]["resource"]["insurance"][0]["coverage"]["type"] == URL[4], "negative test case failed"
            assert not claim[1]["resource"]["insurance"][0]["focal"] == 0, "negative test case failed"
            assert not claim[1]["resource"]["insurance"][0]["preAuthRef"][0] == CLAIM_CODE, "negative test case failed"
            assert not claim[1]["resource"]["insurance"][0]["sequence"] == CLAIM_AUTH_NUMBER[1], "negative test case failed"
            assert not claim[1]["resource"]["patient"]["reference"] == ORGANIZATION_FULL_URL, "negative test case failed"
            assert not claim[1]["resource"]["patient"]["type"] == URL[1], "negative test case failed"
            assert not claim[1]["resource"]["priority"]["coding"][0]["code"] == CLAIM_CODE[1], "negative test case failed"
            assert not claim[1]["resource"]["priority"]["coding"][0]["system"] == CLAIM_CODE_SYSTEM[1], "negative test case failed"
            assert not claim[1]["resource"]["provider"]["reference"] == PATIENT_FULL_URL, "negative test case failed"
            assert not claim[1]["resource"]["provider"]["type"] == URL[2], "negative test case failed"
            assert not claim[1]["resource"]["status"] == CLAIM_IDENTIFIER, "negative test case failed"
            assert not claim[1]["resource"]["type"]["coding"][0]["code"] == CLAIM_CODE[0], "negative test case failed"
            assert not claim[1]["resource"]["type"]["coding"][0]["display"] == CLAIM_CODE[1], "negative test case failed"
            assert not claim[1]["resource"]["type"]["coding"][0]["system"] == CLAIM_CODE_SYSTEM[0], "negative test case failed"
            assert not claim[1]["resource"]["use"] == CLAIM_STATUS, "negative test case failed"

            print("FHIR bundle claim 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")
