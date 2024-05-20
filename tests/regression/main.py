import sys

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME,
    UNUSED_RES_NAME
)

from tests.regression.patient_resource import patient_test
from tests.regression.organization_resource import org_test
from tests.regression.encounter_resource import enc_test
from tests.regression.account_resource import acc_test
from tests.regression.coverage_1_resource import insurancecoverage_1_test
from tests.regression.coverage_2_resource import insurancecoverage_2_test
from tests.regression.coverage_3_resource import insurancecoverage_3_test
from tests.regression.relatedperson_resource import relatedperson_test
from tests.regression.relatedperson_insurance_1_resource import relatedperson_insurance_1_test
from tests.regression.relatedperson_insurance_2_resource import relatedperson_insurance_2_test
from tests.regression.relatedperson_insurance_3_resource import relatedperson_insurance_3_test
from tests.regression.practitioner_attending_resource import practitioner_attending_test
from tests.regression.practitioner_referring_resource import practitioner_referring_test
from tests.regression.claim_1_resource import claim_1_test
from tests.regression.claim_2_resource import claim_2_test
from tests.regression.claim_3_resource import claim_3_test
from tests.regression.unused import unused_test


def run_tests():
    acc_test(RESOURCE_NAME[0], "1", IDENTIFIER_URL, IDENTIFIER_ID[0])
    claim_1_test(RESOURCE_NAME[1], "1", IDENTIFIER_URL, IDENTIFIER_ID[1])
    claim_1_test(RESOURCE_NAME[1], "2", IDENTIFIER_URL, IDENTIFIER_ID[1])
    claim_2_test(RESOURCE_NAME[1], "1", IDENTIFIER_URL, IDENTIFIER_ID[1])
    claim_3_test(RESOURCE_NAME[1], "1", IDENTIFIER_URL, IDENTIFIER_ID[1])
    insurancecoverage_1_test(RESOURCE_NAME[2], "1", IDENTIFIER_URL, IDENTIFIER_ID[2])
    insurancecoverage_1_test(RESOURCE_NAME[2], "2", IDENTIFIER_URL, IDENTIFIER_ID[2])
    insurancecoverage_1_test(RESOURCE_NAME[2], "3", IDENTIFIER_URL, IDENTIFIER_ID[2])
    insurancecoverage_2_test(RESOURCE_NAME[2], "1", IDENTIFIER_URL, IDENTIFIER_ID[2])
    insurancecoverage_2_test(RESOURCE_NAME[2], "2", IDENTIFIER_URL, IDENTIFIER_ID[2])
    insurancecoverage_2_test(RESOURCE_NAME[2], "3", IDENTIFIER_URL, IDENTIFIER_ID[2])
    # If added insurancecoverage_3_test("insurancecoverage", "2"), insurancecoverage_3_test("insurancecoverage", "3"), it will be repetitive
    # The test cases were covered in insurancecoverage_2_test("insurancecoverage", "2"), insurancecoverage_2_test("insurancecoverage", "3")
    insurancecoverage_3_test(RESOURCE_NAME[2], "1", IDENTIFIER_URL, IDENTIFIER_ID[2])
    enc_test(RESOURCE_NAME[3], "1", IDENTIFIER_URL, IDENTIFIER_ID[6])
    org_test(RESOURCE_NAME[4], "1", IDENTIFIER_URL, IDENTIFIER_ID[8])
    patient_test(RESOURCE_NAME[5], "1", IDENTIFIER_URL, IDENTIFIER_ID[5])
    patient_test(RESOURCE_NAME[5], "2", IDENTIFIER_URL, IDENTIFIER_ID[5])
    patient_test(RESOURCE_NAME[5], "3", IDENTIFIER_URL, IDENTIFIER_ID[5])
    patient_test(RESOURCE_NAME[5], "4", IDENTIFIER_URL, IDENTIFIER_ID[5])
    patient_test(RESOURCE_NAME[5], "5", IDENTIFIER_URL, IDENTIFIER_ID[5])
    practitioner_attending_test(RESOURCE_NAME[6], "1", IDENTIFIER_URL, IDENTIFIER_ID[10])
    #practitioner referring tests use same test file that is being used by practitioner attending tests
    practitioner_referring_test(RESOURCE_NAME[6], "1", IDENTIFIER_URL, IDENTIFIER_ID[10])
    relatedperson_test(RESOURCE_NAME[7], "1", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_test(RESOURCE_NAME[7], "2", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_test(RESOURCE_NAME[7], "3", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_test(RESOURCE_NAME[7], "4", IDENTIFIER_URL, IDENTIFIER_ID[4])

    relatedperson_insurance_1_test(RESOURCE_NAME[7], "1", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "2", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "3", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "4", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "5", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "6", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_1_test(RESOURCE_NAME[7], "7", IDENTIFIER_URL, IDENTIFIER_ID[4])

    relatedperson_insurance_2_test(RESOURCE_NAME[7], "1", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_2_test(RESOURCE_NAME[7], "2", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_2_test(RESOURCE_NAME[7], "3", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_2_test(RESOURCE_NAME[7], "4", IDENTIFIER_URL, IDENTIFIER_ID[4])

    relatedperson_insurance_3_test(RESOURCE_NAME[7], "1", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_3_test(RESOURCE_NAME[7], "2", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_3_test(RESOURCE_NAME[7], "3", IDENTIFIER_URL, IDENTIFIER_ID[4])
    relatedperson_insurance_3_test(RESOURCE_NAME[7], "4", IDENTIFIER_URL, IDENTIFIER_ID[4])

    ##Tests for segments with no elements
    unused_test(UNUSED_RES_NAME, "1")

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    run_tests()