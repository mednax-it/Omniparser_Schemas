import json

from omniparser_schemas.parser.main import validate_ETL_parser

def filter_resource(resource_name, testfile, identifier_url, identifier_id):
    validate_ETL_parser(resource_name, testfile)
    with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = resource_name
        entries = fhir_bundle["entry"]
        filter_resource = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
        RESOURCE_IDENTIFIER = f'{identifier_url}/{identifier_id}'
        return list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RESOURCE_IDENTIFIER, filter_resource))
