import sys

from tests.regression.patient_resource import patient_test
from tests.regression.organization_resource import org_test
from tests.regression.encounter_resource import enc_test
from tests.regression.account_resource import acc_test
from tests.regression.coverage_resource import insurancecoverage_test

def run_tests():
    patient_test("patient", "1")
    patient_test("patient", "2")
    patient_test("patient", "3")
    patient_test("patient", "4")
    patient_test("patient", "5")


    org_test("organization", "1")
    enc_test("encounter", "1")
    acc_test("account", "1")
    insurancecoverage_test("insurancecoverage", "1")
    insurancecoverage_test("insurancecoverage", "2")
    insurancecoverage_test("insurancecoverage", "3")

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    run_tests()