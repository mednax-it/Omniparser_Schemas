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
    REQUEST_TYPE
)

def patient_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Patient"
        entries = fhir_bundle["entry"]
        pat = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))

    assert pat[0]["resource"]["identifier"][0]["value"] == MRN, "did not match MRN"
    assert pat[0]["resource"]["name"][0]["family"] == LASTNAME, "did not match lastname"""
    assert pat[0]["resource"]["name"][0]["given"][0] == FIRSTNAME, "did not match firstname"
    assert pat[0]["resource"]["name"][0]["given"][1] == MIDDLENAME, "did not match middlename"
    assert pat[0]["resource"]["birthDate"] == DOB, "did not match dob"
    assert pat[0]["resource"]["gender"] == GENDER, "did not match gender"
    assert pat[0]["resource"]["address"][0]["line"][0] == ADDRESS1, "did not match address1"
    assert pat[0]["resource"]["address"][0]["line"][1] == ADDRESS2, "did not match address2"
    assert pat[0]["resource"]["address"][0]["city"] == CITY, "did not match city"
    assert pat[0]["resource"]["address"][0]["state"] == STATE, "did not match state"
    assert pat[0]["resource"]["address"][0]["postalCode"] == ZIP, "did not match zip"
    assert pat[0]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
    assert pat[0]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match addresstype"
    assert pat[0]["resource"]["telecom"][0]["value"] == HOMEPHONE, "did not match homephone"
    assert pat[0]["resource"]["telecom"][0]["use"] == HOMEPHONETYPE, "did not match homephonetype"
    assert pat[0]["resource"]["telecom"][2]["value"] == HOMEEMAIL, "did not match homeemail"
    assert pat[0]["resource"]["telecom"][1]["value"] == WORKPHONE, "did not match workphone"
    assert pat[0]["resource"]["telecom"][3]["use"] == WORKPHONETYPE, "did not match workphonetype"
    assert pat[0]["resource"]["telecom"][3]["value"] == WORKEMAIL, "did not match workemail"
    assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS, "did not match maritalstatus"
    assert pat[0]["resource"]["identifier"][2]["value"] == HOSPITALPATIENTNUMBER, "did not match hospital patient number"
    assert pat[0]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"
    assert pat[0]["resource"]["multipleBirthInteger"] == BIRTHORDER, "did not match birthorder"

    assert pat[0]["fullUrl"] == PATIENT_FULL_URL, "did not match patient's full url"
    assert pat[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request method"

    assert pat[0]["request"]["url"] == f"Patient?identifier=https://pediatrix.com/fhir/NamingSystem/mrn-id|{MRN}&mrn-assigner={ORGANIZATION_FULL_URL}"

    assert pat[0]["resource"]["identifier"][0]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient MRN reference did not match with organization reference URL"
    assert pat[0]["resource"]["identifier"][2]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient account reference did not match with organization reference URL"

    print("FHIR bundle patient resource tests were successful")
