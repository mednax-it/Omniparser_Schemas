import json
import sys
from omniparser_schemas.parser.main import validate_ETL_parser

from.reg_globals.relatedperson_reg_global import (
    RELATED_PERSON_ID,
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
    RELATEDPERSON_ID
)
from tests.regression.reg_globals.request_type import (
    REQUEST_TYPE
)

from tests.regression.reg_globals.reference_urls import (
    RELATED_PERSON_GUARANTOR_FULL_URL,
    PATIENT_FULL_URL
)

from .reg_globals.organization_reg_globals import(
    VALUE
)

from .reg_globals.patient_reg_global import(
    MRN,
    SSN_SYSTEM
)

def related_person_test(resource_name, testfile):
    validate_ETL_parser(resource_name, testfile)
    with open("tests/regression/regression_output/" + str(resource_name) + "/regression_" + str(resource_name) + "_" + str(testfile) + ".json",  'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "RelatedPerson"
        entries = fhir_bundle["entry"]
        filter_relper = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))
        RELPER_IDENTIFIER = "https://pediatrix.com/fhir/NamingSystem/relatedPerson-id"
        rel = list(filter(lambda e: e["resource"]["identifier"][0]["system"] == RELPER_IDENTIFIER, filter_relper))

        assert rel[3]["fullUrl"] == RELATED_PERSON_GUARANTOR_FULL_URL, "did not match related person resource full url"
        assert rel[3]["request"]["method"] == REQUEST_TYPE[0], "did not match put request type"
        assert rel[3]["request"]["url"] == f'RelatedPerson?identifier=https://pediatrix.com/fhir/NamingSystem/relatedPerson-id|{MRN}-{VALUE}-{RELATED_PERSON_ID[0]}', "did not match request url"
        assert rel[3]["resource"]["address"][0]["city"] == CITY, "did not match city"
        assert rel[3]["resource"]["address"][0]["country"] == COUNTRY, "did not match country"
        assert rel[3]["resource"]["address"][0]["line"][0] == ADDRESS1[0], "did not match address1"
        assert rel[3]["resource"]["address"][0]["line"][1] == ADDRESS2[0], "did not match address2"
        assert rel[3]["resource"]["address"][0]["postalCode"] == ZIP, "did not match postal code"
        assert rel[3]["resource"]["address"][0]["state"] == STATE, "did not match state"
        assert rel[3]["resource"]["address"][0]["type"] == ADDRESSTYPE, "did not match address type"
        assert rel[3]["resource"]["address"][0]["use"] == ADDRESSUSE[0], "did not match address use"
        assert rel[3]["resource"]["birthDate"] == DOB, "did not match DOB"
        assert rel[3]["resource"]["gender"] == GENDER, "did not match gender"
        assert rel[3]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM, "did not match identifier system"
        assert rel[3]["resource"]["identifier"][0]["value"] == f'{MRN}-{VALUE}-{RELATED_PERSON_ID[0]}', "did not match related person id value"
        assert rel[3]["resource"]["identifier"][1]["system"] == SSN_SYSTEM, "did not match ssn system"
        assert rel[3]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == "https://terminology.hl7.org/5.0.0/CodeSystem-v2-0203", "did not match SSN coding system"
        assert rel[3]["resource"]["identifier"][1]["value"] == SSN, "did not match SSN"
        assert rel[3]["resource"]["name"][0]["family"] == LASTNAME[0], "did not match lastname"
        assert rel[3]["resource"]["name"][0]["given"][0] == FIRSTNAME[0], "did not match firstname"
        assert rel[3]["resource"]["name"][0]["given"][1] == MIDDLENAME[0], "did not match middlename"
        assert rel[3]["resource"]["patient"]["reference"] == PATIENT_FULL_URL, "did not match full url"
        assert rel[3]["resource"]["patient"]["type"] == "Patient", "did not match type"
        

    print("FHIR bundle related person resource tests were successful")





