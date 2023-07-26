import json

from .reg_globals.coverage_reg_globals import(
    BENEFICIARY_DISPLAY,
    BENEFICIARY_TYPE,
    IDENTIFIER_SYSTEM,
    IDENTIFIER_VALUE,
    CODING,
    CODING_VALUE,
    COVERAGE_NETWORK,
    COVERAGE_ORDER,
    COVERAGE_PERIOD_START_DATE,
    COVERAGE_PERIOD_END_DATE,
    COVERAGE_STATUS,
    COVERAGE_SUBSCRIBER_DISPLAY,
    COVERAGE_SUBSCRIBER_VALUE,
    COVERAGE_SUBSCRIBER_TYPE,
    RELATIONSHIP_CODE,
    RELATIONSHIP_DISPLAY,
    SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON,
    SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT,
    N_BENEFICIARY_DISPLAY,
    N_BENEFICIARY_TYPE,
    N_IDENTIFIER_SYSTEM,
    N_IDENTIFIER_VALUE,
    N_CODING,
    N_CODING_VALUE,
    N_COVERAGE_NETWORK,
    N_COVERAGE_ORDER,
    N_COVERAGE_PERIOD_START_DATE,
    N_COVERAGE_PERIOD_END_DATE,
    N_COVERAGE_STATUS,
    N_COVERAGE_SUBSCRIBER_DISPLAY,
    N_COVERAGE_SUBSCRIBER_VALUE,
    N_COVERAGE_SUBSCRIBER_TYPE,
    N_RELATIONSHIP_CODE,
    N_RELATIONSHIP_DISPLAY,
    N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON,
    N_SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT
)

from .reg_globals.reference_urls import(
    COVERAGE_FULL_URL_1,
    RELATED_PERSON_INSURANCE_FULL_URL_1,
    PATIENT_FULL_URL,
    ORGANIZATION_PAYOR_FULL_URL,
    N_COVERAGE_FULL_URL_1,
    N_RELATED_PERSON_INSURANCE_FULL_URL_1,
    N_PATIENT_FULL_URL,
    N_ORGANIZATION_PAYOR_FULL_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
    N_REQUEST_TYPE
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

from .reg_globals.patient_reg_global import(
    MRN
)

from omniparser_schemas.parser.main import validate_ETL_parser

def insurancecoverage_test(resource_name, testfile):
    if(testfile == "1"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "Coverage"
            entries = fhir_bundle["entry"]
            filter_cov = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            COV_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/coverage-id"
            cov = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == COV_IDENTIFIER, filter_cov))

            assert cov[0]["fullUrl"] == COVERAGE_FULL_URL_1, "did not match full url"
            assert cov[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request type"
            assert cov[0]["request"]["url"] ==  f'Coverage?identifier=https://pediatrix.com/fhir/NamingSystem/coverage-id|{MRN}-{VALUE}-{CODING_VALUE[0]}', "did not match request url"
            assert cov[0]["resource"]["beneficiary"]["display"] == BENEFICIARY_DISPLAY, "did not match beneficiary display"
            assert cov[0]["resource"]["beneficiary"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
            assert cov[0]["resource"]["beneficiary"]["type"] == BENEFICIARY_TYPE, "did not match beneficiary type"
            assert cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == CODING[0], "did not match codiing"
            assert cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == CODING[1], "did not match coding display"
            assert cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == CODING[2], "did not match coding system"
            assert cov[0]["resource"]["identifier"][1]["value"] == CODING_VALUE[0], "did not match coding value"
            assert cov[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM[0], "did not match identifier system"
            assert cov[0]["resource"]["identifier"][0]["value"] == IDENTIFIER_VALUE, "did not match identifier value"
            assert cov[0]["resource"]["identifier"][1]["system"] == IDENTIFIER_SYSTEM[1], "did not match identifier system"
            assert cov[0]["resource"]["identifier"][1]["value"] == CODING_VALUE[0], "did not match coding value"
            assert cov[0]["resource"]["network"] == COVERAGE_NETWORK[0], "did not match coverage network"
            assert cov[0]["resource"]["order"] == COVERAGE_ORDER[0], "did not match coverage order"
            assert cov[0]["resource"]["payor"][0]["reference"] == ORGANIZATION_PAYOR_FULL_URL, "did not match coverage full url"
            assert cov[0]["resource"]["period"]["end"] == COVERAGE_PERIOD_END_DATE[0], "did not match coverage end date"
            assert cov[0]["resource"]["period"]["start"] == COVERAGE_PERIOD_START_DATE[0], "did not match coverage start date"
            assert cov[0]["resource"]["policyHolder"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
            assert cov[0]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[0], "did not match relationship code"
            assert cov[0]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[0], "did not match relationship display"
            assert cov[0]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "did not match subscriber system"
            assert cov[0]["resource"]["status"] == COVERAGE_STATUS[0], "did not match coverage status"
            assert cov[0]["resource"]["subscriber"]["display"] == COVERAGE_SUBSCRIBER_DISPLAY, "did not match coverage subscriber display"
            assert cov[0]["resource"]["subscriber"]["identifier"]["value"] == COVERAGE_SUBSCRIBER_VALUE, "did not match subscriber identifier value"
            assert cov[0]["resource"]["subscriber"]["reference"] == RELATED_PERSON_INSURANCE_FULL_URL_1, "did not match subscriber reference"
            assert cov[0]["resource"]["subscriber"]["type"] == COVERAGE_SUBSCRIBER_TYPE, "did not match subscriber type"

            assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            assert cov[2]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[2]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[2]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            #Negative test cases

            assert not cov[0]["fullUrl"] == N_COVERAGE_FULL_URL_1, "did not match full url"
            assert not cov[0]["request"]["method"] == N_REQUEST_TYPE[0], "did not match request type"
            assert not cov[0]["request"]["url"] ==  f'Coverage?identifier=https://pediatrix.com/fhir/NamingSystem/coverage-id|{MRN}-{VALUE}-{N_CODING_VALUE[0]}', "did not match request url"
            assert not cov[0]["resource"]["beneficiary"]["display"] == N_BENEFICIARY_DISPLAY, "did not match beneficiary display"
            assert not cov[0]["resource"]["beneficiary"]["reference"] == N_PATIENT_FULL_URL, "did not match patient full url"
            assert not cov[0]["resource"]["beneficiary"]["type"] == N_BENEFICIARY_TYPE, "did not match beneficiary type"
            assert not cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == N_CODING[0], "did not match codiing"
            assert not cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == N_CODING[1], "did not match coding display"
            assert not cov[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == N_CODING[2], "did not match coding system"
            assert not cov[0]["resource"]["identifier"][1]["value"] == N_CODING_VALUE[0], "did not match coding value"
            assert not cov[0]["resource"]["identifier"][0]["system"] == N_IDENTIFIER_SYSTEM[0], "did not match identifier system"
            assert not cov[0]["resource"]["identifier"][0]["value"] == N_IDENTIFIER_VALUE, "did not match identifier value"
            assert not cov[0]["resource"]["identifier"][1]["system"] == N_IDENTIFIER_SYSTEM[1], "did not match identifier system"
            assert not cov[0]["resource"]["identifier"][1]["value"] == N_CODING_VALUE[0], "did not match coding value"
            assert not cov[0]["resource"]["network"] == N_COVERAGE_NETWORK[0], "did not match coverage network"
            assert not cov[0]["resource"]["order"] == N_COVERAGE_ORDER[0], "did not match coverage order"
            assert not cov[0]["resource"]["payor"][0]["reference"] == N_ORGANIZATION_PAYOR_FULL_URL, "did not match coverage full url"
            assert not cov[0]["resource"]["period"]["end"] == N_COVERAGE_PERIOD_END_DATE[0], "did not match coverage end date"
            assert not cov[0]["resource"]["period"]["start"] == N_COVERAGE_PERIOD_START_DATE[0], "did not match coverage start date"
            assert not cov[0]["resource"]["policyHolder"]["reference"] == N_PATIENT_FULL_URL, "did not match patient full url"
            assert not cov[0]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[2], "negative test case failed"
            assert not cov[0]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[2], "negative test case failed"
            assert not cov[0]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"
            assert not cov[0]["resource"]["status"] == N_COVERAGE_STATUS[0], "did not match coverage status"
            assert not cov[0]["resource"]["subscriber"]["display"] == N_COVERAGE_SUBSCRIBER_DISPLAY, "did not match coverage subscriber display"
            assert not cov[0]["resource"]["subscriber"]["identifier"]["value"] == N_COVERAGE_SUBSCRIBER_VALUE, "did not match subscriber identifier value"
            assert not cov[0]["resource"]["subscriber"]["reference"] == N_RELATED_PERSON_INSURANCE_FULL_URL_1, "did not match subscriber reference"
            assert not cov[0]["resource"]["subscriber"]["type"] == N_COVERAGE_SUBSCRIBER_TYPE, "did not match subscriber type"

            assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[3], "negative test case failed"
            assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[3], "negative test case failed"
            assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

            assert not cov[2]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[0], "negative test case failed"
            assert not cov[2]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[0], "negative test case failed"
            assert not cov[2]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

            print("FHIR bundle coverage resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "Coverage"
            entries = fhir_bundle["entry"]
            filter_cov = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            COV_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/coverage-id"
            cov = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == COV_IDENTIFIER, filter_cov))

            assert cov[0]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[0]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[0]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            assert cov[2]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[2]
            assert cov[2]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[2]
            assert cov[2]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            #Negative test cases
            assert not cov[0]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[3], "negative test case failed"
            assert not cov[0]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[3], "negative test case failed"
            assert not cov[0]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

            assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[2], "negative test case failed"
            assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[2], "negative test case failed"
            assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

            assert not cov[2]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[0], "negative test case failed"
            assert not cov[2]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[0], "negative test case failed"
            assert not cov[2]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

            print("FHIR bundle coverage resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "Coverage"
            entries = fhir_bundle["entry"]
            filter_cov = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            COV_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/coverage-id"
            cov = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == COV_IDENTIFIER, filter_cov))

            assert cov[0]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[3]
            assert cov[0]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[3]
            assert cov[0]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT

            assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[3]
            assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[3]
            assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT

            #Negative test cases
            assert not cov[0]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[1], "negative test case failed"
            assert not cov[0]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[1], "negative test case failed"
            assert not cov[0]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT, "negative test case failed"

            assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[0], "negative test case failed"
            assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[0], "negative test case failed"
            assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT, "negative test case failed"

            assert not cov[2]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[2], "negative test case failed"
            assert not cov[2]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[2], "negative test case failed"
            assert not cov[2]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT, "negative test case failed"

            print("FHIR bundle coverage resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")










