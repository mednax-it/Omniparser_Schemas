from.reg_globals.relatedperson_insurance_reg_global import (
    RELATEDPERSON_INSURANCE_ID,
    ADDRESS1,
    ADDRESS2,
    CITY,
    STATE,
    ZIP,
    COUNTRY,
    ADDRESSUSE,
    DOB,
    GENDER,
    HOMEPHONE,
    SSN,
    SSN_CODING_SYSTEM,
    LASTNAME,
    FIRSTNAME,
    MIDDLENAME,
    TELECOM_SYSTEM,
    ADDRESSTYPE,
    HOMEPHONE,
    HOMEEMAIL,
    WORKPHONE,
    WORKEMAIL,
    PHONETYPE
)

from tests.regression.reg_globals.request_type import (
    REQUEST_TYPE
)

from tests.regression.reg_globals.reference_urls import (
    RELATED_PERSON_INSURANCE_FULL_URL_2,
    PATIENT_FULL_URL
)

from .reg_globals.organization_reg_globals import(
    FACILITY_ID
)

from .reg_globals.patient_reg_global import(
    MRN,
    SSN_SYSTEM
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from omniparser_schemas.parser.filter import filter_resource

## Note, we are not using ETL parser in these tests, we are re utilizing the files that were already ran for the test "relatedperson_resource.py"
## Also these tests are performed on independent segments(additional subscriber segments can also be added, for example we can see 3 IN1 segments) that's why these test files can be resused for all related person resources(guarantor & subscriber)

def relatedperson_insurance_2_test(resource_name, testfile, identifier_url, identifier_id):
    if(testfile == "1"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[1]["fullUrl"] == RELATED_PERSON_INSURANCE_FULL_URL_2, "did not match related person resource full url"
        assert rel[1]["request"]["method"] == REQUEST_TYPE[0], "did not match put request type"
        assert rel[1]["request"]["url"] == f'{RESOURCE_NAME[7]}?identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[4]}|{MRN}-{FACILITY_ID}-{RELATEDPERSON_INSURANCE_ID[1]}', "did not match request url"
        assert rel[1]["resource"]["address"][0]["city"] == CITY[1], "did not match city"
        assert rel[1]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
        assert rel[1]["resource"]["address"][0]["line"][0] == ADDRESS1[1], "did not match address1"
        assert rel[1]["resource"]["address"][0]["line"][1] == ADDRESS2[1], "did not match address2"
        assert rel[1]["resource"]["address"][0]["postalCode"] == ZIP[1], "did not match postal code"
        assert rel[1]["resource"]["address"][0]["state"] == STATE[1], "did not match state"
        assert rel[1]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match address type"
        assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"
        assert rel[1]["resource"]["birthDate"] == DOB[1], "did not match DOB"
        assert rel[1]["resource"]["gender"] == GENDER[0], "did not match gender"
        assert rel[1]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[4]}', "did not match identifier system"
        assert rel[1]["resource"]["identifier"][0]["value"] == f'{MRN}-{FACILITY_ID}-{RELATEDPERSON_INSURANCE_ID[1]}', "did not match related person id value"
        assert rel[1]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match ssn system"
        assert rel[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_CODING_SYSTEM, "did not match SSN coding system"
        assert rel[1]["resource"]["identifier"][1]["value"] == SSN[1], "did not match SSN"
        assert rel[1]["resource"]["name"][0]["family"] == LASTNAME[1], "did not match lastname"
        assert rel[1]["resource"]["name"][0]["given"][0] == FIRSTNAME[1], "did not match firstname"
        assert rel[1]["resource"]["name"][0]["given"][1] == MIDDLENAME[1], "did not match middlename"
        assert rel[1]["resource"]["patient"]["reference"] == PATIENT_FULL_URL, "did not match full url"
        assert rel[1]["resource"]["patient"]["type"] == RESOURCE_NAME[5], "did not match type"
        assert rel[1]["resource"]["telecom"][0]["system"] == TELECOM_SYSTEM[0], "did not match telecom system"
        assert rel[1]["resource"]["telecom"][0]["use"] == PHONETYPE[0], "did not match telecom use"
        assert rel[1]["resource"]["telecom"][0]["value"] == HOMEPHONE[1], "did not match homephone"
        assert rel[1]["resource"]["telecom"][1]["system"] == TELECOM_SYSTEM[0], "did not match telecom system"
        assert rel[1]["resource"]["telecom"][1]["use"] == PHONETYPE[2], "did not match telecom use"
        assert rel[1]["resource"]["telecom"][1]["value"] == WORKPHONE[1], "did not match workphone"
        assert rel[1]["resource"]["telecom"][2]["system"] == TELECOM_SYSTEM[1], "did not match email system"
        assert rel[1]["resource"]["telecom"][2]["use"] == PHONETYPE[0], "did not match email use"
        assert rel[1]["resource"]["telecom"][2]["value"] == HOMEEMAIL[1], "did not match homeemail"
        assert rel[1]["resource"]["telecom"][3]["system"] == TELECOM_SYSTEM[1], "did not match email system"
        assert rel[1]["resource"]["telecom"][3]["use"] == PHONETYPE[2], "did not match email use"
        assert rel[1]["resource"]["telecom"][3]["value"] == WORKEMAIL[1], "did not match homeemail"

        #Negative test cases
        assert not rel[1]["fullUrl"] == PATIENT_FULL_URL, "negative test case failed"
        assert not rel[1]["request"]["method"] == FACILITY_ID, "negative test case failed"
        assert not rel[1]["request"]["url"] == RELATEDPERSON_INSURANCE_ID[0], "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["city"] == ADDRESSUSE, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["country"] == ADDRESSTYPE, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["line"][0] == ADDRESS2, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["line"][1] == ADDRESS1, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["postalCode"] == STATE, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["state"] == ZIP, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["type"] == COUNTRY, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["use"] == CITY, "negative test case failed"
        assert not rel[1]["resource"]["birthDate"] == GENDER, "negative test case failed"
        assert not rel[1]["resource"]["gender"] == DOB, "negative test case failed"
        assert not rel[1]["resource"]["identifier"][0]["system"] == IDENTIFIER_URL, "negative test case failed"
        assert not rel[1]["resource"]["identifier"][0]["value"] == RELATED_PERSON_INSURANCE_FULL_URL_2[0], "negative test case failed"
        assert not rel[1]["resource"]["identifier"][1]["system"] == SSN_CODING_SYSTEM, "negative test case failed"
        assert not rel[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN, "negative test case failed"
        assert not rel[1]["resource"]["identifier"][1]["value"] == SSN_SYSTEM, "negative test case failed"
        assert not rel[1]["resource"]["name"][0]["family"] == MIDDLENAME, "negative test case failed"
        assert not rel[1]["resource"]["name"][0]["given"][0] == LASTNAME, "negative test case failed"
        assert not rel[1]["resource"]["name"][0]["given"][1] == FIRSTNAME, "negative test case failed"
        assert not rel[1]["resource"]["patient"]["reference"] == RELATED_PERSON_INSURANCE_FULL_URL_2, "negative test case failed"
        assert not rel[1]["resource"]["patient"]["type"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][0]["system"] == RESOURCE_NAME[0], "negative test case failed"
        assert not rel[1]["resource"]["telecom"][0]["use"] == HOMEPHONE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][0]["value"] == ADDRESSUSE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][1]["system"] == PHONETYPE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][1]["use"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][1]["value"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][2]["system"] == WORKPHONE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][2]["use"] == HOMEEMAIL, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][2]["value"] == PHONETYPE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][3]["system"] == WORKEMAIL, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][3]["use"] == WORKPHONE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][3]["value"] == TELECOM_SYSTEM, "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[1]["resource"]["gender"] == GENDER[1], "did not match gender"
        assert rel[1]["resource"]["telecom"][0]["use"] == PHONETYPE[1], "did not match telecom use"
        assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"

        #Negative test cases
        assert not rel[1]["resource"]["gender"] == ADDRESSUSE, "negative test case failed"
        assert not rel[1]["resource"]["telecom"][0]["use"] == GENDER, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["use"] == PHONETYPE, "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for "  + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[1]["resource"]["gender"] == GENDER[2], "did not match gender"
        assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[1], "did not match address use"

        #Negative test cases
        assert not rel[1]["resource"]["gender"] == ADDRESSUSE, "negative test case failed"
        assert not rel[1]["resource"]["address"][0]["use"] == GENDER, "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")


    elif(testfile == "4"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[2], "did not match address use"

        #Negative test cases
        assert not rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[1], "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")
