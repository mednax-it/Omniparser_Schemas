import importlib
import json
import sys

from omniparser_schemas.smilecdr.universal_etl_parser import fetch_parsed_text

def validate_ETL_parser():
   with importlib.resources.path("omniparser_schemas.smilecdr", "RegressionTestData.txt") as f:
      hl7content = f.read_text()
   # The universal parser need to have carriage return
   hl7content = hl7content.replace('\\r', '\r')

   # call universal utl parser
   fhir_bundle_from_hl7 = fetch_parsed_text(hl7content)
      # Remove first and last character of fhir bundle
   fhir_bundle = fhir_bundle_from_hl7[1:-1]

   json_data = json.loads(fhir_bundle)

   with open("src/omniparser_schemas/smilecdr/hl7_regression.json", "w") as f:
       json.dump(json_data, f)

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    validate_ETL_parser()

