import json

from .reg_globals.coverage_reg_globals import(
    RELATIONSHIP_CODE,
    RELATIONSHIP_DISPLAY,
    SUBSCRIBER_IDENTIFIER_SYSTEM
)

from omniparser_schemas.parser.main import validate_ETL_parser

def insurancecoverage_test(resource_name, testfile):
    validate_ETL_parser(resource_name, testfile)
    if(testfile == "1"):
        with open("tests/regression/regression_output/" + str(resource_name) + "/hl7_regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "Coverage"
            entries = fhir_bundle["entry"]
            filter_cov = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            COV_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/coverage-id"
            cov = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == COV_IDENTIFIER, filter_cov))

            assert cov[0]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[0]
            assert cov[0]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[0]
            assert cov[0]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM

            assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM

            assert cov[2]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1]
            assert cov[2]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1]
            assert cov[2]["resource"]["subscriber"]["identifier"]["system"] == SUBSCRIBER_IDENTIFIER_SYSTEM

            print("coverage FHIR resource tests were completed")





