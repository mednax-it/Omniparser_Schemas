import os
import importlib
import json
from omniparser_schemas.parser.universal_etl_parser import fetch_parsed_text



def missing_segment_test():

    # Get the segments to be tested
    segments = "MissingSegments"

    missing_segment_test_data_dir = f"tests/regression/regression_test_data/{segments}"

    filenames = os.listdir(missing_segment_test_data_dir)

    for filename in filenames:
        with importlib.resources.path("tests.regression.regression_test_data." + str(segments), str(filename)) as f:
            hl7content = f.read_text()

            # The universal parser need to have carriage return
            hl7content = hl7content.replace('\\r', '\r')

            # call universal etl parser
            fhir_bundle_from_hl7=fetch_parsed_text(hl7content)
            fhir_bundle = fhir_bundle_from_hl7[1:-1]

            json_data = json.loads(fhir_bundle)

            OUTPUT_ROOT_PATH = "tests/regression/regression_output/"
            PATH = OUTPUT_ROOT_PATH + str(segments)
            if not os.path.exists(PATH):
              os.makedirs(PATH)

            with open(PATH + "/regression_" + str(segments) + "_" + str(filename) + ".json", "w") as f:
              json.dump(json_data, f)


    print("FHIR bundle with missing segments tests were successful")