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
    RELATED_PERSON_INSURANCE_FULL_URL_1,
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
from omniparser_schemas.custom.check_FHIR_resource_element import check_if_FHIR_resource_element_exists

def relatedperson_insurance_1_test(resource_name, testfile, identifier_url, identifier_id):
    if(testfile == "1"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)
        assert rel[0]["fullUrl"] == RELATED_PERSON_INSURANCE_FULL_URL_1, "did not match related person resource full url"
        assert rel[0]["request"]["method"] == REQUEST_TYPE[0], "did not match put request type"
        assert rel[0]["request"]["url"] == f'{RESOURCE_NAME[7]}?identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[4]}|{MRN}-{FACILITY_ID}-{RELATEDPERSON_INSURANCE_ID[0]}', "did not match request url"
        assert rel[0]["resource"]["address"][0]["city"] == CITY[0], "did not match city"
        assert rel[0]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
        assert rel[0]["resource"]["address"][0]["line"][0] == ADDRESS1[0], "did not match address1"
        assert rel[0]["resource"]["address"][0]["line"][1] == ADDRESS2[0], "did not match address2"
        assert rel[0]["resource"]["address"][0]["postalCode"] == ZIP[0], "did not match postal code"
        assert rel[0]["resource"]["address"][0]["state"] == STATE[0], "did not match state"
        assert rel[0]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match address type"
        assert rel[0]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"
        assert rel[0]["resource"]["birthDate"] == DOB[0], "did not match DOB"
        assert rel[0]["resource"]["gender"] == GENDER[0], "did not match gender"
        assert rel[0]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[4]}', "did not match identifier system"
        assert rel[0]["resource"]["identifier"][0]["value"] == f'{MRN}-{FACILITY_ID}-{RELATEDPERSON_INSURANCE_ID[0]}', "did not match related person id value"
        assert rel[0]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match ssn system"
        assert rel[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_CODING_SYSTEM, "did not match SSN coding system"
        assert rel[0]["resource"]["identifier"][1]["value"] == SSN[0], "did not match SSN"
        assert rel[0]["resource"]["name"][0]["family"] == LASTNAME[0], "did not match lastname"
        assert rel[0]["resource"]["name"][0]["given"][0] == FIRSTNAME[0], "did not match firstname"
        assert rel[0]["resource"]["name"][0]["given"][1] == MIDDLENAME[0], "did not match middlename"
        assert rel[0]["resource"]["patient"]["reference"] == PATIENT_FULL_URL, "did not match full url"
        assert rel[0]["resource"]["patient"]["type"] == RESOURCE_NAME[5], "did not match type"
        assert rel[0]["resource"]["telecom"][0]["system"] == TELECOM_SYSTEM[0], "did not match telecom system"
        assert rel[0]["resource"]["telecom"][0]["use"] == PHONETYPE[0], "did not match telecom use"
        assert rel[0]["resource"]["telecom"][0]["value"] == HOMEPHONE[0], "did not match homephone"
        assert rel[0]["resource"]["telecom"][1]["system"] == TELECOM_SYSTEM[0], "did not match telecom system"
        assert rel[0]["resource"]["telecom"][1]["use"] == PHONETYPE[2], "did not match telecom use"
        assert rel[0]["resource"]["telecom"][1]["value"] == WORKPHONE[0], "did not match workphone"
        assert rel[0]["resource"]["telecom"][2]["system"] == TELECOM_SYSTEM[1], "did not match email system"
        assert rel[0]["resource"]["telecom"][2]["use"] == PHONETYPE[0], "did not match email use"
        assert rel[0]["resource"]["telecom"][2]["value"] == HOMEEMAIL[0], "did not match homeemail"
        assert rel[0]["resource"]["telecom"][3]["system"] == TELECOM_SYSTEM[1], "did not match email system"
        assert rel[0]["resource"]["telecom"][3]["use"] == PHONETYPE[2], "did not match email use"
        assert rel[0]["resource"]["telecom"][3]["value"] == WORKEMAIL[0], "did not match homeemail"

        ##Negative test cases
        assert not rel[0]["fullUrl"] == PATIENT_FULL_URL, "negative test case failed"
        assert not rel[0]["request"]["method"] == FACILITY_ID, "negative test case failed"
        assert not rel[0]["request"]["url"] == RELATEDPERSON_INSURANCE_ID[0], "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["city"] == ADDRESSUSE, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["country"] == ADDRESSTYPE, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["line"][0] == ADDRESS2, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["line"][1] == ADDRESS1, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["postalCode"] == STATE, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["state"] == ZIP, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["type"] == COUNTRY, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["use"] == CITY, "negative test case failed"
        assert not rel[0]["resource"]["birthDate"] == GENDER, "negative test case failed"
        assert not rel[0]["resource"]["gender"] == DOB, "negative test case failed"
        assert not rel[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_URL, "negative test case failed"
        assert not rel[0]["resource"]["identifier"][0]["value"] == RELATED_PERSON_INSURANCE_FULL_URL_1[0], "negative test case failed"
        assert not rel[0]["resource"]["identifier"][1]["system"] == SSN_CODING_SYSTEM, "negative test case failed"
        assert not rel[0]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN, "negative test case failed"
        assert not rel[0]["resource"]["identifier"][1]["value"] == SSN_SYSTEM, "negative test case failed"
        assert not rel[0]["resource"]["name"][0]["family"] == MIDDLENAME, "negative test case failed"
        assert not rel[0]["resource"]["name"][0]["given"][0] == LASTNAME, "negative test case failed"
        assert not rel[0]["resource"]["name"][0]["given"][1] == FIRSTNAME, "negative test case failed"
        assert not rel[0]["resource"]["patient"]["reference"] == RELATED_PERSON_INSURANCE_FULL_URL_1, "negative test case failed"
        assert not rel[0]["resource"]["patient"]["type"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][0]["system"] == RESOURCE_NAME[0], "negative test case failed"
        assert not rel[0]["resource"]["telecom"][0]["use"] == HOMEPHONE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][0]["value"] == ADDRESSUSE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][1]["system"] == PHONETYPE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][1]["use"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][1]["value"] == TELECOM_SYSTEM, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][2]["system"] == WORKPHONE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][2]["use"] == HOMEEMAIL, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][2]["value"] == PHONETYPE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][3]["system"] == WORKEMAIL, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][3]["use"] == WORKPHONE, "negative test case failed"
        assert not rel[0]["resource"]["telecom"][3]["value"] == TELECOM_SYSTEM, "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[0]["resource"]["gender"] == GENDER[1], "did not match gender"
        assert rel[0]["resource"]["telecom"][0]["use"] == PHONETYPE[1], "did not match telecom use"
        assert rel[0]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"

        #Negative test cases
        assert not rel[0]["resource"]["gender"] == GENDER[0], "negative test case failed"
        assert not rel[0]["resource"]["telecom"][0]["use"] == ADDRESSUSE, "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["use"] == PHONETYPE, "negative test case failed"
        ##Check improper year https://mednax1500.atlassian.net/browse/SMILECDR-882
        # assert check_if_FHIR_resource_element_exists(rel, 0, "resource", "birthDate") == "FHIR resource element not found", "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for "  + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[0]["resource"]["gender"] == GENDER[2], "did not match gender"
        assert rel[0]["resource"]["address"][0]["use"] == ADDRESSUSE[1], "did not match address use"

        #Negative test cases
        assert not rel[0]["resource"]["gender"] == GENDER[1], "negative test case failed"
        assert not rel[0]["resource"]["address"][0]["use"] == PHONETYPE, "negative test case failed"
        ##Check improper months https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert check_if_FHIR_resource_element_exists(rel, 0, "resource", "birthDate") == "FHIR resource element not found", "negative test case failed"
        assert check_if_FHIR_resource_element_exists(rel, 1, "resource", "birthDate") == "FHIR resource element not found", "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "4"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert rel[0]["resource"]["address"][0]["use"] == ADDRESSUSE[2], "did not match address use"

        #Negative test cases
        assert not rel[0]["resource"]["address"][0]["use"] == PHONETYPE, "negative test case failed"
        ##Check improper dates https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert check_if_FHIR_resource_element_exists(rel, 0, "resource", "birthDate") == "FHIR resource element not found", "negative test case failed"
        assert check_if_FHIR_resource_element_exists(rel, 1, "resource", "birthDate") == "FHIR resource element not found", "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "5"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)
       
        #Negative test cases
        ##Check improper HH https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[0]["resource"]["birthDate"] == DOB[0], "did not match DOB"
         ##Check improper MM https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[1]["resource"]["birthDate"] == DOB[1], "did not match DOB"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")


    elif(testfile == "6"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        #Negative test cases
        ##Check improper SS https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[0]["resource"]["birthDate"] == DOB[0], "did not match DOB"
        ##Check improper Fractional seconds https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[1]["resource"]["birthDate"] == DOB[1], "did not match DOB"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")


    elif(testfile == "7"):
        rel = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        #Negative test cases
        ##Check improper TimeZone https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[0]["resource"]["birthDate"] == DOB[0], "did not match DOB"
        ##Check improper Precision https://mednax1500.atlassian.net/browse/SMILECDR-882
        assert rel[1]["resource"]["birthDate"] == DOB[1], "did not match DOB"

        print("FHIR bundle " + str(resource_name) + " subscriber 1 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")
