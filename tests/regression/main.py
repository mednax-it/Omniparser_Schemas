import sys

from tests.regression.patient_resource import patient_test
from tests.regression.organization_resource import org_test

def run_tests():
    patient_test()
    org_test()

def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    run_tests()