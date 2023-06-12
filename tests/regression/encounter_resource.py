import json
import sys

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ENCOUNTER_FULL_URL,
    ACCOUNT_FULL_URL,
    ATTENDING_PRACTIONER_FULL_URL,
    REFERRING_PRACTIONER_FULL_URL,
    ORGANIZATION_DEPARTMENT_FULL_URL

)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.request_type import(
    REQUEST_TYPE
)

from .reg_globals.enocunter_reg_globals import(
    PACID,
    ADMIT_DATETIME,
    DISCHARGE_DATETIME,
    PATIENT_TYPE,
    ADMIT_TYPE,
    FINANCIAL_CLASS
)

def enc_test():
    with open('src/omniparser_schemas/parser/hl7_regression.json', 'r') as json_file:
        fhir_bundle = json.load(json_file)
        TARGET_RESOURCE_TYPE = "Encounter"
        entries = fhir_bundle["entry"]
        enc = list(filter(lambda e: e["resource"]["resourceType"] == TARGET_RESOURCE_TYPE, entries))

    FacilityId = "{{FacilityId}}"
    admitdate = ADMIT_DATETIME
    admitdate = admitdate.replace("-", "")
    assert enc[0]["fullUrl"] == ENCOUNTER_FULL_URL, "encounter URL did not match"
    assert enc[0]["request"]["ifNoneExist"] == f"identifier=https://pediatrix.com/fhir/NamingSystem/patient-demographics-update-id|{MRN}-{FacilityId}-{admitdate}", "identifier did not match"
    assert enc[0]["request"]["method"] == REQUEST_TYPE[1], "did not match request type"
    assert enc[0]["resource"]["account"][0]["reference"] == ACCOUNT_FULL_URL, "did not match account URL"
    assert enc[0]["resource"]["identifier"][0]["value"] == f"{MRN}-{FacilityId}-{admitdate}", "did match identifier value"
    assert enc[0]["resource"]["identifier"][1]["value"] == PACID, "did not match pacid"
    assert enc[0]["resource"]["participant"][0]["individual"]["reference"] == ATTENDING_PRACTIONER_FULL_URL, "did not match attending practioner full url"
    assert enc[0]["resource"]["participant"][1]["individual"]["reference"] == REFERRING_PRACTIONER_FULL_URL, "did not match referring practioner full url"
    assert enc[0]["resource"]["period"]["start"] == ADMIT_DATETIME, "did not match admit date"
    assert enc[0]["resource"]["period"]["end"] == DISCHARGE_DATETIME, "did not match discharge date"
    assert enc[0]["resource"]["serviceProvider"]["reference"] == ORGANIZATION_DEPARTMENT_FULL_URL, "did not match organization department full url"
    assert enc[0]["resource"]["subject"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
    assert enc[0]["resource"]["type"][0]["text"] == (ADMIT_TYPE+"|"+PATIENT_TYPE+"|"+FINANCIAL_CLASS), "did not match admit type or patient type or financial class"
    print("FHIR bundle encounter resource tests were successful")