import json
import sys

from .reg_globals.patient_reg_global import (
    MRN,
    LASTNAME,
    FIRSTNAME,
    MIDDLENAME
)

def patient_test():
    with open('src/omniparser_schemas/smilecdr/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)
    assert fhir_bundle["entry"][10]["resource"]["identifier"][0]["value"] == MRN, "did not match MRN"
    print("Patient Resource Regression Tests got PASS")

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    patient_test()