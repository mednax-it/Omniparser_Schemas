from .reg_globals.coverage_reg_globals import(
    BENEFICIARY_DISPLAY,
    CODING,
    CODING_VALUE,
    COVERAGE_ID,
    COVERAGE_NETWORK,
    COVERAGE_ORDER,
    COVERAGE_PERIOD_START_DATE,
    COVERAGE_PERIOD_END_DATE,
    COVERAGE_STATUS,
    COVERAGE_SUBSCRIBER_DISPLAY,
    COVERAGE_SUBSCRIBER_VALUE,
    RELATIONSHIP_CODE,
    RELATIONSHIP_DISPLAY
)

from .reg_globals.reference_urls import(
    COVERAGE_FULL_URL_2,
    RELATED_PERSON_INSURANCE_FULL_URL_1,
    PATIENT_FULL_URL,
    ORGANIZATION_PAYOR_FULL_URL_2,
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
)

from .reg_globals.organization_reg_globals import(
    FACILITY_ID
)

from .reg_globals.patient_reg_global import(
    MRN
)

from omniparser_schemas.parser.filter import filter_resource

def insurancecoverage_2_test(resource_name, testfile, identifier_url, identifier_id):
    if(testfile == "1"):
        cov = filter_resource(resource_name, testfile, identifier_url, identifier_id)
        assert cov[1]["fullUrl"] == COVERAGE_FULL_URL_2, "did not match full url"
        assert cov[1]["request"]["method"] == REQUEST_TYPE[0], "did not match request type"
        assert cov[1]["request"]["url"] ==  f'{RESOURCE_NAME[2]}?identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[2]}|{MRN}-{FACILITY_ID}-{CODING_VALUE[1]}', "did not match request url"
        assert cov[1]["resource"]["beneficiary"]["display"] == BENEFICIARY_DISPLAY, "did not match beneficiary display"
        assert cov[1]["resource"]["beneficiary"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
        assert cov[1]["resource"]["beneficiary"]["type"] == RESOURCE_NAME[5], "did not match beneficiary type"
        assert cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == CODING[0], "did not match codiing"
        assert cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == CODING[1], "did not match coding display"
        assert cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == CODING[2], "did not match coding system"
        assert cov[1]["resource"]["identifier"][0]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[2]}', "did not match identifier system"
        assert cov[1]["resource"]["identifier"][0]["value"] == f'{MRN}-{FACILITY_ID}-{COVERAGE_ID[1]}', "did not match identifier value"
        assert cov[1]["resource"]["identifier"][1]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[3]}', "did not match identifier system"
        assert cov[1]["resource"]["identifier"][1]["value"] == CODING_VALUE[1], "did not match coding value"
        assert cov[1]["resource"]["network"] == COVERAGE_NETWORK[1], "did not match coverage network"
        assert cov[1]["resource"]["order"] == COVERAGE_ORDER[1], "did not match coverage order"
        assert cov[1]["resource"]["payor"][0]["reference"] == ORGANIZATION_PAYOR_FULL_URL_2, "did not match coverage full url"
        assert cov[1]["resource"]["period"]["end"] == COVERAGE_PERIOD_END_DATE[1], "did not match coverage end date"
        assert cov[1]["resource"]["period"]["start"] == COVERAGE_PERIOD_START_DATE[1], "did not match coverage start date"
        assert cov[1]["resource"]["policyHolder"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
        assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[3], "did not match relationship code"
        assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[3], "did not match relationship display"
        assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[5]}', "did not match subscriber system"
        assert cov[1]["resource"]["status"] == COVERAGE_STATUS[0], "did not match coverage status"
        assert cov[1]["resource"]["subscriber"]["display"] == COVERAGE_SUBSCRIBER_DISPLAY[1], "did not match coverage subscriber display"
        assert cov[1]["resource"]["subscriber"]["identifier"]["value"] == f'{MRN}-{FACILITY_ID}', "did not match subscriber identifier value"
        assert cov[1]["resource"]["subscriber"]["reference"] == PATIENT_FULL_URL, "did not match subscriber reference"
        assert cov[1]["resource"]["subscriber"]["type"] == RESOURCE_NAME[5], "did not match subscriber type"

        #Negative test cases
        assert not cov[1]["fullUrl"] == PATIENT_FULL_URL, "negative test case failed"
        assert not cov[1]["request"]["method"] == REQUEST_TYPE[1], "negative test case failed"
        assert not cov[1]["request"]["url"] ==  CODING, "negative test case failed"
        assert not cov[1]["resource"]["beneficiary"]["display"] == RELATIONSHIP_CODE[1], "negative test case failed"
        assert not cov[1]["resource"]["beneficiary"]["reference"] == COVERAGE_FULL_URL_2, "negative test case failed"
        assert not cov[1]["resource"]["beneficiary"]["type"] == BENEFICIARY_DISPLAY, "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["code"] == CODING_VALUE[0], "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["display"] == CODING[2], "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["type"]["coding"][0]["system"] == CODING[1], "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["value"] == CODING_VALUE[2], "negative test case failed"
        assert not cov[1]["resource"]["identifier"][0]["system"] == IDENTIFIER_URL, "negative test case failed"
        assert not cov[1]["resource"]["identifier"][0]["value"] == FACILITY_ID, "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["system"] == IDENTIFIER_URL, "negative test case failed"
        assert not cov[1]["resource"]["identifier"][1]["value"] == RELATIONSHIP_DISPLAY, "negative test case failed"
        assert not cov[1]["resource"]["network"] == COVERAGE_ORDER[1], "negative test case failed"
        assert not cov[1]["resource"]["order"] == COVERAGE_PERIOD_END_DATE[0], "negative test case failed"
        assert not cov[1]["resource"]["payor"][0]["reference"] == COVERAGE_PERIOD_START_DATE, "negative test case failed"
        assert not cov[1]["resource"]["period"]["end"] == COVERAGE_PERIOD_START_DATE[0], "negative test case failede"
        assert not cov[1]["resource"]["period"]["start"] == COVERAGE_PERIOD_END_DATE[0], "negative test case failed"
        assert not cov[1]["resource"]["policyHolder"]["reference"] == COVERAGE_FULL_URL_2, "negative test case failed"
        assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_DISPLAY[2], "negative test case failed"
        assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_CODE[2], "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == IDENTIFIER_URL, "negative test case failed"
        assert not cov[1]["resource"]["status"] == COVERAGE_ORDER[0], "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["display"] == COVERAGE_NETWORK, "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["identifier"]["value"] == COVERAGE_SUBSCRIBER_VALUE, "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["reference"] == RELATIONSHIP_DISPLAY, "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["type"] == RELATED_PERSON_INSURANCE_FULL_URL_1, "negative test case failed"
        print("FHIR bundle coverage 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "2"):
        cov = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[1], "did not match relationship code"
        assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[1], "did not match relationship display"
        assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[4]}', "did not match subscriber system"

        #Negative test cases
        assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[2], "negative test case failed"
        assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[2], "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == IDENTIFIER_URL, "negative test case failed"

        print("FHIR bundle coverage 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")

    elif(testfile == "3"):
        cov = filter_resource(resource_name, testfile, identifier_url, identifier_id)

        assert cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[3]
        assert cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[3]
        assert cov[1]["resource"]["subscriber"]["identifier"]["system"] == f'{IDENTIFIER_URL}/{IDENTIFIER_ID[5]}'

        #Negative test cases
        assert not cov[1]["resource"]["relationship"]["coding"][0]["code"] == RELATIONSHIP_CODE[0], "negative test case failed"
        assert not cov[1]["resource"]["relationship"]["coding"][0]["display"] == RELATIONSHIP_DISPLAY[0], "negative test case failed"
        assert not cov[1]["resource"]["subscriber"]["identifier"]["system"] == IDENTIFIER_URL, "negative test case failed"

        print("FHIR bundle coverage 2 resource tests for " + str(resource_name) + " testfile " + str(testfile) + " were successful")
