import json
import sys

from collections import Counter
from .reg_globals.patient_reg_global import (
    MRN,
    LASTNAME,
    FIRSTNAME,
    MIDDLENAME,
    DOB,
    GENDER,
    ADDRESS1,
    ADDRESS2,
    CITY,
    STATE,
    ZIP,
    COUNTRY,
    ADDRESSTYPE,
    HOMEPHONE,
    HOMEPHONETYPE,
    HOMEEMAIL,
    WORKPHONE,
    WORKPHONETYPE,
    WORKEMAIL,
    MARITALSTATUS,
    HOSPITALPATIENTNUMBER,
    SSN

)

def patient_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)

    assert fhir_bundle["entry"][10]["resource"]["identifier"][0]["value"] == MRN, "did not match MRN"
    assert fhir_bundle["entry"][10]["resource"]["name"][0] == LASTNAME, "did not match lastname"
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["given"][0] == FIRSTNAME, "did not match firstname"
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["given"][1] == MIDDLENAME, "did not match firstname"
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["given"][0] == FIRSTNAME, "did not match middlename"
    assert fhir_bundle["entry"][10]["resource"]["birthDate"] == DOB, "did not match dob"
    assert fhir_bundle["entry"][10]["resource"]["gender"] == GENDER, "did not match gender"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["line"][0] == ADDRESS1, "did not match address1"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["line"][1] == ADDRESS2, "did not match address2"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["city"] == CITY, "did not match city"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["state"] == STATE, "did not match state"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["postalCode"] == ZIP, "did not match zip"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
    assert fhir_bundle["entry"][10]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match addresstype"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][0]["value"] == HOMEPHONE, "did not match homephone"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][0]["value"] == HOMEPHONETYPE, "did not match homephonetype"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][2]["value"] == HOMEEMAIL, "did not match homeemail"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][1]["value"] == WORKPHONE, "did not match workphone"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][0]["value"] == WORKPHONETYPE, "did not match workphonetype"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][3]["value"] == WORKEMAIL, "did not match workemail"
    assert fhir_bundle["entry"][10]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS, "did not match maritalstatus"
    assert fhir_bundle["entry"][10]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"

    print("Patient MRN is found in FHIR bundle. Still lot more to go, will update shortly, stay tuned!!!!!")

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    patient_test()