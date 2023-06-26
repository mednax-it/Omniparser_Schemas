import importlib
import json
import sys
import os

from omniparser_schemas.parser.universal_etl_parser import fetch_parsed_text

def validate_ETL_parser(resource, file):
   with importlib.resources.path("tests.regression.regression_test_data." + str(resource), str(resource) + "_test_data_" + str(file) + ".txt") as f:
      hl7content = f.read_text()
   # The universal parser need to have carriage return
   hl7content = hl7content.replace('\\r', '\r')

   # call universal utl parser
   fhir_bundle_from_hl7 = fetch_parsed_text(hl7content)
      # Remove first and last character of fhir bundle

   fhir_bundle = fhir_bundle_from_hl7[1:-1]

   json_data = json.loads(fhir_bundle)

   OUTPUT_ROOT_PATH = "tests/regression/regression_output/"
   PATH = OUTPUT_ROOT_PATH + str(resource)
   if not os.path.exists(PATH):
    os.makedirs(PATH)

   with open(OUTPUT_ROOT_PATH + str(resource) + "/hl7_regression_" + str(resource) + "_" + str(file) + ".json", "w") as f:
       json.dump(json_data, f)

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    validate_ETL_parser()

