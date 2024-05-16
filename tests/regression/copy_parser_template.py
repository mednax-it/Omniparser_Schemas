import json

def copy_jspn_file(source_file, destination_file):

    with open(source_file, "r") as f:
        data = json.load(f)

    with open(destination_file, "w") as f:
        json.dump(data, f, indent=4)

source_file = "hl7v2_default.json"
destination_file = "tests/regression/parser_template.json"