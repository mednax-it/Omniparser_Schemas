import sys

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

def run_tests():
    patient_test("patient", "1")
    patient_test("patient", "2")
    patient_test("patient", "3")
    patient_test("patient", "4")
    patient_test("patient", "5")

    org_test("organization", "1")

    enc_test("encounter", "1")

    acc_test("account", "1")

    insurancecoverage_1_test("insurancecoverage", "1")
    insurancecoverage_1_test("insurancecoverage", "2")
    insurancecoverage_1_test("insurancecoverage", "3")

    insurancecoverage_2_test("insurancecoverage", "1")
    insurancecoverage_2_test("insurancecoverage", "2")
    insurancecoverage_2_test("insurancecoverage", "3")

    insurancecoverage_3_test("insurancecoverage", "1")
    # If added insurancecoverage_3_test("insurancecoverage", "2"), insurancecoverage_3_test("insurancecoverage", "3"), it will be repetitive
    # The test cases were covered in insurancecoverage_2_test("insurancecoverage", "2"), insurancecoverage_2_test("insurancecoverage", "3")

    relatedperson_test("relatedperson", "1")
    relatedperson_test("relatedperson", "2")
    relatedperson_test("relatedperson", "3")
    relatedperson_test("relatedperson", "4")

    relatedperson_insurance_1_test("relatedperson", "1")
    relatedperson_insurance_1_test("relatedperson", "2")
    relatedperson_insurance_1_test("relatedperson", "3")
    relatedperson_insurance_1_test("relatedperson", "4")

    relatedperson_insurance_2_test("relatedperson", "1")
    relatedperson_insurance_2_test("relatedperson", "2")
    relatedperson_insurance_2_test("relatedperson", "3")
    relatedperson_insurance_2_test("relatedperson", "4")

    relatedperson_insurance_3_test("relatedperson", "1")
    relatedperson_insurance_3_test("relatedperson", "2")
    relatedperson_insurance_3_test("relatedperson", "3")
    relatedperson_insurance_3_test("relatedperson", "4")

    practitioner_attending_test("practitioner", "1")
    #practitioner referring tests also use same test file that is being used by practitioner attending tests
    practitioner_referring_test("practitioner", "1")

    claim_1_test("claim", "1")
    claim_2_test("claim", "1")


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    run_tests()