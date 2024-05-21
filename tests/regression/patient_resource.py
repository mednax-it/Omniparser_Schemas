from .reg_globals.patient_reg_global import (
    MRN,
    LASTNAME,
    FIRSTNAME,
    MIDDLENAME,
    DOB,
    DOD,
    GENDER,
    ADDRESS1,
    ADDRESS2,
    CITY,
    STATE,
    ZIP,
    COUNTRY,
    ADDRESSTYPE,
    ADDRESSUSE,
    HOMEPHONE,
    HOMEEMAIL,
    WORKPHONE,
    WORKEMAIL,
    PHONETYPE,
    HOSPITALPATIENTNUMBER,
    SSN,
    BIRTHORDER,
    MR_CODE,
    MR_DISPLAY,
    MR_SYSTEM,
    SSN_SYSTEM,
    SSN_CODE,
    SSN_DISPLAY,
    SSN_TERMINOLOGY_SYSTEM,
    PATIENT_INTERNAL_CODE,
    PATIENT_INTERNAL_DISPLAY,
    PATIENT_INTERNAL_SYSTEM,
    MARITALSTATUS_CODE,
    MARITALSTATUS_DISPLAY,
    MARITALSTATUS_SYSTEM
)

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ORGANIZATION_FULL_URL
)

from .reg_globals.request_type import(
    REQUEST_TYPE
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from omniparser_schemas.parser.filter import filter_resource

def patient_test(resource_name, testfile, identifier_url, identifier_id):
    if(testfile == "1"):
        pat = filter_resource(resource_name, testfile, identifier_url, identifier_id)
        assert pat[0]["fullUrl"] == PATIENT_FULL_URL, "did not match patient's full url"
        assert pat[0]["request"]["method"] == REQUEST_TYPE[0], "did not match request method"
        assert pat[0]["resource"]["identifier"][0]["value"] == MRN, "did not match MRN"
        assert pat[0]["resource"]["name"][0]["family"] == LASTNAME, "did not match lastname"""
        assert pat[0]["resource"]["name"][0]["given"][0] == FIRSTNAME, "did not match firstname"
        assert pat[0]["resource"]["name"][0]["given"][1] == MIDDLENAME, "did not match middlename"
        assert pat[0]["resource"]["birthDate"] == DOB, "did not match dob"
        assert pat[0]["resource"]["deceasedDateTime"] == DOD, "did not match dod"
        assert pat[0]["resource"]["gender"] == GENDER[0], "did not match gender"
        assert pat[0]["resource"]["address"][0]["line"][0] == ADDRESS1, "did not match address1"
        assert pat[0]["resource"]["address"][0]["line"][1] == ADDRESS2, "did not match address2"
        assert pat[0]["resource"]["address"][0]["city"] == CITY, "did not match city"
        assert pat[0]["resource"]["address"][0]["state"] == STATE, "did not match state"
        assert pat[0]["resource"]["address"][0]["postalCode"] == ZIP, "did not match zip"
        assert pat[0]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
        assert pat[0]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match addresstype"
        assert pat[0]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match addressuse"
        assert pat[0]["resource"]["telecom"][0]["value"] == HOMEPHONE, "did not match homephone"
        assert pat[0]["resource"]["telecom"][0]["use"] == PHONETYPE[0], "did not match homephonetype"
        assert pat[0]["resource"]["telecom"][2]["value"] == HOMEEMAIL, "did not match homeemail"
        assert pat[0]["resource"]["telecom"][1]["value"] == WORKPHONE, "did not match workphone"
        assert pat[0]["resource"]["telecom"][3]["use"] == PHONETYPE[2], "did not match workphonetype"
        assert pat[0]["resource"]["telecom"][3]["value"] == WORKEMAIL, "did not match workemail"
        assert pat[0]["resource"]["telecom"][2]["use"] == PHONETYPE[0], "did not match phone type"
        assert pat[0]["resource"]["identifier"][2]["value"] == HOSPITALPATIENTNUMBER, "did not match hospital patient number"
        assert pat[0]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"
        assert pat[0]["resource"]["multipleBirthInteger"] == BIRTHORDER, "did not match birthorder"

        assert pat[0]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[5]}', "did not match identifier system"
        assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == MR_CODE, "did not match MR code"
        assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["display"] == MR_DISPLAY, "did not match MR display"
        assert pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == MR_SYSTEM, "did not match MR system"
        assert pat[0]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match SSN system"
        assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == SSN_CODE, "did not match SSN code"
        assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == SSN_DISPLAY, "did not match SSN display"
        assert pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_TERMINOLOGY_SYSTEM, "did not match SSN terminology system"
        assert pat[0]["resource"]["identifier"][2]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[9]}', "did not match hospital patient system"
        assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["code"] == PATIENT_INTERNAL_CODE, "did not match patient internal code"
        assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["display"] == PATIENT_INTERNAL_DISPLAY, "did not match patient internal display"
        assert pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["system"] == PATIENT_INTERNAL_SYSTEM, "did not match patient internal system"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_CODE[0], "did not match marital status code"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] ==  MARITALSTATUS_DISPLAY[0], "did not match marital status display"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["system"] == MARITALSTATUS_SYSTEM, "did not match marital status system"
        assert pat[0]["request"]["url"] == f'{RESOURCE_NAME[5]}?identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[5]}|{MRN}&mrn-assigner={ORGANIZATION_FULL_URL}'
        assert pat[0]["resource"]["identifier"][0]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient MRN reference did not match with organization reference URL"
        assert pat[0]["resource"]["identifier"][2]["assigner"]["reference"] == ORGANIZATION_FULL_URL, "patient account reference did not match with organization reference URL"

        #Negative test cases
        assert not pat[0]["resource"]["identifier"][0]["value"] == MR_CODE, "negative test case failed"
        assert not pat[0]["resource"]["name"][0]["family"] == MIDDLENAME, "negative test case failed"
        assert not pat[0]["resource"]["name"][0]["given"][0] == LASTNAME, "negative test case failed"
        assert not pat[0]["resource"]["name"][0]["given"][1] == FIRSTNAME, "negative test case failed"
        assert not pat[0]["resource"]["birthDate"] == DOD, "negative test case failed"
        assert not pat[0]["resource"]["deceasedDateTime"] == DOB, "negative test case failed"
        assert not pat[0]["resource"]["gender"] == CITY, "negative test case failedr"
        assert not pat[0]["resource"]["address"][0]["line"][0] == ADDRESS2, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["line"][1] == ADDRESS1, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["city"] == GENDER, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["state"] == COUNTRY, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["postalCode"] == SSN, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["country"] == ADDRESSTYPE, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["type"] == COUNTRY, "negative test case failed"
        assert not pat[0]["resource"]["address"][0]["use"] == HOMEEMAIL, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][0]["value"] == WORKEMAIL, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][0]["use"] == WORKPHONE, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][2]["value"] == HOMEPHONE, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][1]["value"] == WORKEMAIL, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][3]["use"] == PHONETYPE, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][2]["use"] == ADDRESSTYPE, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][3]["value"] == HOMEEMAIL, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == ADDRESSUSE, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["value"] == SSN, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][1]["value"] == HOSPITALPATIENTNUMBER, "negative test case failed"
        assert not pat[0]["resource"]["multipleBirthInteger"] == HOMEPHONE, "negative test case failed"

        assert not pat[0]["resource"]["identifier"][0]["system"] == MR_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["code"] == MR_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["display"] == MR_CODE, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][0]["type"]["coding"][0]["system"] == MR_DISPLAY, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][1]["system"] == SSN_CODE, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == SSN_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == SSN_TERMINOLOGY_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_DISPLAY, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["system"] == PATIENT_INTERNAL_CODE, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["code"] == HOSPITALPATIENTNUMBER, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["display"] == PATIENT_INTERNAL_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["type"]["coding"][0]["system"] == PATIENT_INTERNAL_DISPLAY, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_SYSTEM, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS_CODE, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["system"] == MARITALSTATUS_DISPLAY, "negative test case failed"
        assert not pat[0]["fullUrl"] == ORGANIZATION_FULL_URL, "negative test case failed"
        assert not pat[0]["request"]["method"] == REQUEST_TYPE[1], "negative test case failed"

        assert not pat[0]["request"]["url"] == {MRN}

        assert not pat[0]["resource"]["identifier"][0]["assigner"]["reference"] == PATIENT_FULL_URL, "negative test case failed"
        assert not pat[0]["resource"]["identifier"][2]["assigner"]["reference"] == PATIENT_FULL_URL, "negative test case failed"

        print("FHIR bundle patient resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        pat=filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert pat[0]["resource"]["gender"] == GENDER[1], "did not match gender"
        assert pat[0]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match addressuse"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_CODE[1], "did not match marital status code"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] ==  MARITALSTATUS_DISPLAY[1], "did not match marital status display"
        assert pat[0]["resource"]["telecom"][0]["use"] == PHONETYPE[1], "did not match phone type"

        #negative test cases

        assert not pat[0]["resource"]["gender"] == ADDRESSUSE, "negative test case failedr"
        assert not pat[0]["resource"]["address"][0]["use"] == GENDER, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_DISPLAY, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS_CODE, "negative test case failed"
        assert not pat[0]["resource"]["telecom"][2]["use"] == WORKPHONE, "negative test case failed"
        print("FHIR bundle patient resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        pat=filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert pat[0]["resource"]["gender"] == GENDER[2], "did not match gender"
        assert pat[0]["resource"]["address"][0]["use"] == ADDRESSUSE[1], "did not match addressuse"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_CODE[2], "did not match marital status code"
        assert pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] ==  MARITALSTATUS_DISPLAY[2], "did not match marital status display"

        #negative test cases
        assert not pat[0]["resource"]["gender"] == ADDRESSUSE, "negative test case failedr"
        assert not pat[0]["resource"]["address"][0]["use"] == GENDER, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["code"] == MARITALSTATUS_DISPLAY, "negative test case failed"
        assert not pat[0]["resource"]["maritalStatus"]["coding"][0]["display"] == MARITALSTATUS_CODE, "negative test case failed"

        print("FHIR bundle patient resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "4"):
        pat=filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert pat[0]["resource"]["address"][0]["use"] == ADDRESSUSE[2], "did not match addressuse"
        assert pat[0]["resource"]["birthDate"] == DOB, "did not match dob"

        #negative test cases
        assert not pat[0]["resource"]["address"][0]["use"] == ADDRESSTYPE, "negative test case failed"

        print("FHIR bundle patient resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "5"):
        pat=filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert pat[0]["resource"]["birthDate"] == DOB, "did not match dob"

