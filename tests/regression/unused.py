import json

from omniparser_schemas.parser.main import validate_ETL_parser


def unused_test(resource_name, testfile, resource_type):
    validate_ETL_parser(resource_name, testfile)
    with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = resource_type
        entries = fhir_bundle["entry"]
        filter_resource = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
        assert filter_resource == [], "Unused "+ resource_type + "element is found"
        print("Test for HL7 segment SFT that has no elements is successful")

