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
    HOSPITALPATIENTNUMBER,
    SSN,
    BIRTHORDER,
    IDENTIFIER_SYSTEM,
    MR_CODE,
    MR_DISPLAY,
    MR_SYSTEM,
    SSN_SYSTEM,
    SSN_CODE,
    SSN_DISPLAY,
    SSN_TERMINOLOGY_SYSTEM,
    HOSPITAL_PATIENT_SYSTEM,
    PATIENT_INTERNAL_CODE,
    PATIENT_INTERNAL_DISPLAY,
    PATIENT_INTERNAL_SYSTEM,
    MARITALSTATUS_CODE,
    MARITALSTATUS_DISPLAY,
    MARITALSTATUS_SYSTEM,

    N_MRN,
    N_LASTNAME,
    N_FIRSTNAME,
    N_MIDDLENAME,
    N_DOB,
    N_GENDER,
    N_ADDRESS1,
    N_ADDRESS2,
    N_CITY,
    N_STATE,
    N_ZIP,
    N_COUNTRY,
    N_ADDRESSTYPE,
    N_HOMEPHONE,
    N_HOMEPHONETYPE,
    N_HOMEEMAIL,
    N_WORKPHONE,
    N_WORKPHONETYPE,
    N_WORKEMAIL,
    N_MARITALSTATUS,
    N_HOSPITALPATIENTNUMBER,
    N_SSN,
    N_BIRTHORDER,
    N_IDENTIFIER_SYSTEM,
    N_MR_CODE,
    N_MR_DISPLAY,
    N_MR_SYSTEM,
    N_SSN_SYSTEM,
    N_SSN_CODE,
    N_SSN_DISPLAY,
    N_SSN_TERMINOLOGY_SYSTEM,
    N_HOSPITAL_PATIENT_SYSTEM,
    N_PATIENT_INTERNAL_CODE,
    N_PATIENT_INTERNAL_DISPLAY,
    N_PATIENT_INTERNAL_SYSTEM,
    N_MARITALSTATUS_CODE,
    N_MARITALSTATUS_DISPLAY,
    N_MARITALSTATUS_SYSTEM,
)

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ORGANIZATION_FULL_URL,
    N_PATIENT_FULL_URL,
    N_ORGANIZATION_FULL_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
    N_REQUEST_TYPE
)

def patient_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Patient"
        entries = fhir_bundle["entry"]
        pat = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))

    assert pat[0]["fullUrl"] == PATIENT_FULL_URL, "did not match patient's full url"
    assert pat[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request method"

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
    assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS_DISPLAY, "did not match maritalstatus"
    assert pat[0]["resource"]["identifier"][2]["value"] == HOSPITALPATIENTNUMBER, "did not match hospital patient number"
    assert pat[0]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"
    assert pat[0]["resource"]["multipleBirthInteger"] == BIRTHORDER, "did not match birthorder"

    assert pat[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM, "did not match identifier system"
    assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == MR_CODE, "did not match MR code"
    assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["display"] == MR_DISPLAY, "did not match MR display"
    assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == MR_SYSTEM, "did not match MR system"
    assert pat[0]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match SSN system"
    assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == SSN_CODE, "did not match SSN code"
    assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == SSN_DISPLAY, "did not match SSN display"
    assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_TERMINOLOGY_SYSTEM, "did not match SSN terminology system"
    assert pat[0]["resource"]["identifier"][2]["system"] == HOSPITAL_PATIENT_SYSTEM, "did not match hospital patient system"
    assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["code"] == PATIENT_INTERNAL_CODE, "did not match patient internal code"
    assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["display"] == PATIENT_INTERNAL_DISPLAY, "did not match patient internal display"
    assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["system"] == PATIENT_INTERNAL_SYSTEM, "did not match patient internal system"
    assert pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_CODE, "did not match marital status code"
    assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] ==  MARITALSTATUS_DISPLAY, "did not match marital status display"
    assert pat[0]["resource"]["maritalStatus"]["coding"][0]["system"] == MARITALSTATUS_SYSTEM, "did not match marital status system"

    assert pat[0]["request"]["url"] == f"Patient?identifier=https://pediatrix.com/fhir/NamingSystem/mrn-id|{MRN}&mrn-assigner={ORGANIZATION_FULL_URL}"

    assert pat[0]["resource"]["identifier"][0]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient MRN reference did not match with organization reference URL"
    assert pat[0]["resource"]["identifier"][2]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient account reference did not match with organization reference URL"

    #Negative test cases
    assert not pat[0]["resource"]["identifier"][0]["value"] == N_MRN, "negative test case failed"
    assert not pat[0]["resource"]["name"][0]["family"] == N_LASTNAME, "negative test case failed"
    assert not pat[0]["resource"]["name"][0]["given"][0] == N_FIRSTNAME, "negative test case failed"
    assert not pat[0]["resource"]["name"][0]["given"][1] == N_MIDDLENAME, "negative test case failed"
    assert not pat[0]["resource"]["birthDate"] == N_DOB, "negative test case failed"
    assert not pat[0]["resource"]["gender"] == N_GENDER, "negative test case failedr"
    assert not pat[0]["resource"]["address"][0]["line"][0] == N_ADDRESS1, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["line"][1] == N_ADDRESS2, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["city"] == N_CITY, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["state"] == N_STATE, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["postalCode"] == N_ZIP, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["country"] == N_COUNTRY, "negative test case failed"
    assert not pat[0]["resource"]["address"][0]["type"] == N_ADDRESSTYPE, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][0]["value"] == N_HOMEPHONE, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][0]["use"] == N_HOMEPHONETYPE, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][2]["value"] == N_HOMEEMAIL, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][1]["value"] == N_WORKPHONE, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][3]["use"] == N_WORKPHONETYPE, "negative test case failed"
    assert not pat[0]["resource"]["telecom"][3]["value"] == N_WORKEMAIL, "negative test case failed"
    assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == N_MARITALSTATUS, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["value"] == N_HOSPITALPATIENTNUMBER, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][1]["value"] == N_SSN, "negative test case failed"
    assert not pat[0]["resource"]["multipleBirthInteger"] == N_BIRTHORDER, "negative test case failed"

    assert not pat[0]["resource"]["identifier"][0]["system"] == N_IDENTIFIER_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == N_MR_CODE, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["display"] == N_MR_DISPLAY, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == N_MR_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][1]["system"] == N_SSN_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == N_SSN_CODE, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == N_SSN_DISPLAY, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == N_SSN_TERMINOLOGY_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["system"] == N_HOSPITAL_PATIENT_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["code"] == N_PATIENT_INTERNAL_CODE, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["display"] == N_PATIENT_INTERNAL_DISPLAY, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["system"] == N_PATIENT_INTERNAL_SYSTEM, "negative test case failed"
    assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == N_MARITALSTATUS_CODE, "negative test case failed"
    assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == N_MARITALSTATUS_DISPLAY, "negative test case failed"
    assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["system"] == N_MARITALSTATUS_SYSTEM, "negative test case failed"
    assert not pat[0]["fullUrl"] == N_PATIENT_FULL_URL, "negative test case failed"
    assert not pat[0]["request"]["method"] == N_REQUEST_TYPE[0], "negative test case failed"

    assert not pat[0]["request"]["url"] == f"Patient?identifier=https://pediatrix.com/fhir/NamingSystem/mrn-id|{N_MRN}&mrn-assigner={N_ORGANIZATION_FULL_URL}"

    assert not pat[0]["resource"]["identifier"][0]["assigner"]["reference"] == N_ORGANIZATION_FULL_URL, "negative test case failed"
    assert not pat[0]["resource"]["identifier"][2]["assigner"]["reference"] == N_ORGANIZATION_FULL_URL, "negative test case failed"

    print("FHIR bundle patient resource tests were successful")