import sys

from patient_resource import pat_cli
from organization_resource import org_cli

def run_tests():
    pat_cli()
    org_cli()

def run_cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    run_tests()