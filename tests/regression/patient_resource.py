import json

from reg_globals.patient_reg_global import (
    LASTNAME,
    FIRSTNAME,
    MIDDLENAME
)

with open('output_regression.json') as data_file:
    data = json.load(data_file)

if (data["entry"][0]["resource"]["resourceType"]) == "Patient":
    patient_data = data["entry"][0]["resource"]

else:
    print("patient resource not found")
    exit(1)


assert data["entry"][0]["resource"]["name"][0]["family"] == LASTNAME, "Last name did not match"
assert data["entry"][0]["resource"]["name"][0]["given"][0] == FIRSTNAME, "First name did not match"
assert data["entry"][0]["resource"]["name"][0]["given"][1] == MIDDLENAME, "First name did not match"

print("Patient Resource Regression Tests got PASS")

