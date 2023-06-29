import json

from .reg_globals.coverage_reg_globals import(
    RELATIONSHIP_CODE,
    RELATIONSHIP_DISPLAY,
    SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON,
    SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT,
    N_RELATIONSHIP_CODE,
    N_RELATIONSHIP_DISPLAY,
    N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON,
    N_SUBSCRIBER_IDENTIFIER_SYSTEM_PATIENT

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

            assert cov[0]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[0]
            assert cov[0]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[0]
            assert cov[0]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            assert cov[2]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[2]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[2]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON

            #Negative test cases
            assert not cov[0]["resource"]["relationship"]["coding"][0]["code"] == N_RELATIONSHIP_CODE[2], "negative test case failed"
            assert not cov[0]["resource"]["relationship"]["coding"][0]["display"] == N_RELATIONSHIP_DISPLAY[2], "negative test case failed"
            assert not cov[0]["resource"]["subscriber"]["identifier"]["system"] == N_SUBSCRIBER_IDENTIFIER_SYSTEM_RELATED_PERSON, "negative test case failed"

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










