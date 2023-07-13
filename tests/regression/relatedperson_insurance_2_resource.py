import json
from omniparser_schemas.parser.main import validate_ETL_parser

from.reg_globals.relatedperson_insurance_reg_global import (
    RELATEDPERSON_ID,
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
    PHONETYPE,
    IDENTIFIER_SYSTEM,
    N_ADDRESS1,
    N_ADDRESS2,
    N_CITY,
    N_STATE,
    N_ZIP,
    N_COUNTRY,
    N_ADDRESSUSE,
    N_DOB,
    N_GENDER,
    N_HOMEPHONE,
    N_SSN,
    N_SSN_CODING_SYSTEM,
    N_LASTNAME,
    N_FIRSTNAME,
    N_MIDDLENAME,
    N_TELECOM_SYSTEM,
    N_ADDRESSTYPE,
    N_HOMEPHONE,
    N_HOMEEMAIL,
    N_WORKPHONE,
    N_WORKEMAIL,
    N_PHONETYPE,
    N_IDENTIFIER_SYSTEM
)

from tests.regression.reg_globals.request_type import (
    REQUEST_TYPE,
    N_REQUEST_TYPE
)

from tests.regression.reg_globals.reference_urls import (
    RELATED_PERSON_INSURANCE_FULL_URL_2,
    PATIENT_FULL_URL,
    REFERENCE_TYPE,
    N_RELATED_PERSON_INSURANCE_FULL_URL,
    N_PATIENT_FULL_URL,
    N_REFERENCE_TYPE
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

from .reg_globals.patient_reg_global import(
    MRN,
    SSN_SYSTEM,
    N_MRN,
    N_SSN_SYSTEM
)

## Note, we are not using ETL parser in these tests, we are re utilizing the files that were already ran for the test "relatedperson_resource.py"
## Also these tests are performed on independent segments(additional subscriber segments can also be added, for example we can see 3 IN1 segments) that's why these test files can be resused for all related person resources(guarantor & subscriber)

def relatedperson_insurance_2_test(resource_name, testfile):
    if(testfile == "1"):
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "RelatedPerson"
            entries = fhir_bundle["entry"]
            filter_relper = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            RELPER_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/relatedPerson-id"
            rel = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RELPER_IDENTIFIER, filter_relper))

            assert rel[1]["fullUrl"] == RELATED_PERSON_INSURANCE_FULL_URL_2, "did not match related person resource full url"
            assert rel[1]["request"]["method"] == REQUEST_TYPE[0], "did not match put request type"
            assert rel[1]["request"]["url"] == f'RelatedPerson?identifier=https://pediatrix.com/fhir/NamingSystem/relatedPerson-id|{MRN}-{VALUE}-{RELATEDPERSON_ID[1]}', "did not match request url"
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
            assert rel[1]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM, "did not match identifier system"
            assert rel[1]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}-{RELATEDPERSON_ID[1]}', "did not match related person id value"
            assert rel[1]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match ssn system"
            assert rel[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == SSN_CODING_SYSTEM, "did not match SSN coding system"
            assert rel[1]["resource"]["identifier"][1]["value"] == SSN[1], "did not match SSN"
            assert rel[1]["resource"]["name"][0]["family"] == LASTNAME[1], "did not match lastname"
            assert rel[1]["resource"]["name"][0]["given"][0] == FIRSTNAME[1], "did not match firstname"
            assert rel[1]["resource"]["name"][0]["given"][1] == MIDDLENAME[1], "did not match middlename"
            assert rel[1]["resource"]["patient"]["reference"] == PATIENT_FULL_URL, "did not match full url"
            assert rel[1]["resource"]["patient"]["type"] == REFERENCE_TYPE[0], "did not match type"
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

            ##Negative test cases
            assert not rel[1]["fullUrl"] == N_RELATED_PERSON_INSURANCE_FULL_URL, "negative test case failed"
            assert not rel[1]["request"]["method"] == N_REQUEST_TYPE, "negative test case failed"
            assert not rel[1]["request"]["url"] == f'RelatedPerson?identifier=https://pediatrix.com/fhir/NamingSystem/relatedPerson-id|{N_MRN}-{VALUE}-{RELATEDPERSON_ID[0]}', "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["city"] == N_CITY, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["country"] == N_COUNTRY, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["line"][0] == N_ADDRESS1, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["line"][1] == N_ADDRESS2, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["postalCode"] == N_ZIP, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["state"] == N_STATE, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["type"] == N_ADDRESSTYPE, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["use"] == N_ADDRESSUSE, "negative test case failed"
            assert not rel[1]["resource"]["birthDate"] == N_DOB, "negative test case failed"
            assert not rel[1]["resource"]["gender"] == N_GENDER, "negative test case failed"
            assert not rel[1]["resource"]["identifier"][0]["system"] == N_IDENTIFIER_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["identifier"][0]["value"] == f'{N_MRN}-{VALUE}-{RELATEDPERSON_ID[0]}', "negative test case failed"
            assert not rel[1]["resource"]["identifier"][1]["system"] == N_SSN_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == N_SSN_CODING_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["identifier"][1]["value"] == N_SSN, "negative test case failed"
            assert not rel[1]["resource"]["name"][0]["family"] == N_LASTNAME, "negative test case failed"
            assert not rel[1]["resource"]["name"][0]["given"][0] == N_FIRSTNAME, "negative test case failed"
            assert not rel[1]["resource"]["name"][0]["given"][1] == N_MIDDLENAME, "negative test case failed"
            assert not rel[1]["resource"]["patient"]["reference"] == N_PATIENT_FULL_URL, "negative test case failed"
            assert not rel[1]["resource"]["patient"]["type"] == N_REFERENCE_TYPE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][0]["system"] == N_TELECOM_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][0]["use"] == N_PHONETYPE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][0]["value"] == N_HOMEPHONE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][1]["system"] == N_TELECOM_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][1]["use"] == N_PHONETYPE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][1]["value"] == N_WORKPHONE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][2]["system"] == N_TELECOM_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][2]["use"] == N_PHONETYPE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][2]["value"] == N_HOMEEMAIL, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][3]["system"] == N_TELECOM_SYSTEM, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][3]["use"] == N_PHONETYPE, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][3]["value"] == N_WORKEMAIL, "negative test case failed"

        print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "RelatedPerson"
            entries = fhir_bundle["entry"]
            filter_relper = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            RELPER_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/relatedPerson-id"
            rel = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RELPER_IDENTIFIER, filter_relper))

            assert rel[1]["resource"]["gender"] == GENDER[1], "did not match gender"
            assert rel[1]["resource"]["telecom"][0]["use"] == PHONETYPE[1], "did not match telecom use"
            assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"

            #Negative test cases
            assert not rel[1]["resource"]["gender"] == N_GENDER, "negative test case failed"
            assert not rel[1]["resource"]["telecom"][0]["use"] == N_PHONETYPE, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["use"] == N_ADDRESSUSE, "negative test case failed"

            print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for "  + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "RelatedPerson"
            entries = fhir_bundle["entry"]
            filter_relper = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            RELPER_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/relatedPerson-id"
            rel = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RELPER_IDENTIFIER, filter_relper))

            assert rel[1]["resource"]["gender"] == GENDER[2], "did not match gender"
            assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[1], "did not match address use"

            #Negative test cases
            assert not rel[1]["resource"]["gender"] == N_GENDER, "negative test case failed"
            assert not rel[1]["resource"]["address"][0]["use"] == N_ADDRESSUSE, "negative test case failed"

            print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")


    elif(testfile == "4"):
        validate_ETL_parser(resource_name, testfile)
        with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
            fhir_bundle = json.load(json_file)
            TARGET_RESOURCE_TYPE = "RelatedPerson"
            entries = fhir_bundle["entry"]
            filter_relper = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
            RELPER_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/relatedPerson-id"
            rel = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RELPER_IDENTIFIER, filter_relper))

            assert rel[1]["resource"]["address"][0]["use"] == ADDRESSUSE[2], "did not match address use"

            #Negative test cases
            assert not rel[1]["resource"]["address"][0]["use"] == N_ADDRESSUSE, "negative test case failed"

            print("FHIR bundle " + str(resource_name) + " subscriber 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")
