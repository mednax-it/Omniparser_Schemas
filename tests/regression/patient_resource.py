import json
import sys

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
    SSN,
    BIRTHORDER
)

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ORGANIZATION_FULL_URL
)

from .reg_globals.request_type import(
    PUT_REQUEST
)

def patient_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)

    assert fhir_bundle["entry"][10]["resource"]["identifier"][0]["value"] == MRN, "did not match MRN"
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["family"] == LASTNAME, "did not match lastname"""
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["given"][0] == FIRSTNAME, "did not match firstname"
    assert fhir_bundle["entry"][10]["resource"]["name"][0]["given"][1] == MIDDLENAME, "did not match middlename"
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
    assert fhir_bundle["entry"][10]["resource"]["telecom"][0]["use"] == HOMEPHONETYPE, "did not match homephonetype"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][2]["value"] == HOMEEMAIL, "did not match homeemail"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][1]["value"] == WORKPHONE, "did not match workphone"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][3]["use"] == WORKPHONETYPE, "did not match workphonetype"
    assert fhir_bundle["entry"][10]["resource"]["telecom"][3]["value"] == WORKEMAIL, "did not match workemail"
    assert fhir_bundle["entry"][10]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS, "did not match maritalstatus"
    assert fhir_bundle["entry"][10]["resource"]["identifier"][2]["value"] == HOSPITALPATIENTNUMBER, "did not match hospital patient number"
    assert fhir_bundle["entry"][10]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"
    assert fhir_bundle["entry"][10]["resource"]["multipleBirthInteger"] == BIRTHORDER, "did not match birthorder"

    assert fhir_bundle["entry"][10]["fullUrl"] == PATIENT_FULL_URL, "did not match patient's full url"
    assert fhir_bundle["entry"][10]["request"]["method"] == PUT_REQUEST, "did not match request method"

    assert fhir_bundle["entry"][10]["request"]["url"] == f"Patient?identifier=https://pediatrix.com/fhir/NamingSystem/mrn-id|{MRN}&mrn-assigner={ORGANIZATION_FULL_URL}"

    assert fhir_bundle["entry"][10]["resource"]["identifier"][0]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient MRN reference did not match with organization reference URL"
    assert fhir_bundle["entry"][10]["resource"]["identifier"][2]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient account reference did not match with organization reference URL"

    print("FHIR bundle patient resource tests were successful")


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    patient_test()