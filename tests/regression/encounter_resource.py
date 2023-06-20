import json
import sys

from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ENCOUNTER_FULL_URL,
    ACCOUNT_FULL_URL,
    ATTENDING_PRACTIONER_FULL_URL,
    REFERRING_PRACTIONER_FULL_URL,
    ORGANIZATION_DEPARTMENT_FULL_URL,
    REFERENCE_TYPE,
    URL,
    N_PATIENT_FULL_URL,
    N_ENCOUNTER_FULL_URL,
    N_ACCOUNT_FULL_URL,
    N_ATTENDING_PRACTIONER_FULL_URL,
    N_REFERRING_PRACTIONER_FULL_URL,
    N_ORGANIZATION_DEPARTMENT_FULL_URL,
    N_REFERENCE_TYPE,
    N_URL
)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
    N_REQUEST_TYPE

)

from .reg_globals.enocunter_reg_globals import(
    PACID,
    ADMIT_DATETIME,
    DISCHARGE_DATETIME,
    PATIENT_TYPE,
    ADMIT_TYPE,
    FINANCIAL_CLASS,
    CLASS_DISPLAY,
    CLASS_CODE,
    CLASS_SYSTEM,
    IDENTIFIER_SYSTEM,
    PRACTITIONER_CODE,
    PRACTITIONER_DISPLAY,
    PRACTITIONER_SYSTEM,
    ENCOUNTER_STATUS,
    N_PACID,
    N_ADMIT_DATETIME,
    N_DISCHARGE_DATETIME,
    N_PATIENT_TYPE,
    N_ADMIT_TYPE,
    N_FINANCIAL_CLASS,
    N_CLASS_DISPLAY,
    N_CLASS_CODE,
    N_CLASS_SYSTEM,
    N_IDENTIFIER_SYSTEM,
    N_PRACTITIONER_CODE,
    N_PRACTITIONER_DISPLAY,
    N_PRACTITIONER_SYSTEM,
    N_ENCOUNTER_STATUS
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
    assert enc[0]["fullUrl"] == ENCOUNTER_FULL_URL, "did not match encounter URL"
    assert enc[0]["request"]["ifNoneExist"] == f"identifier=https://pediatrix.com/fhir/NamingSystem/patient-demographics-update-id|{MRN}-{FacilityId}-{admitdate}", "identifier did not match"
    assert enc[0]["request"]["url"] == URL[2], "did not match request url"
    assert enc[0]["request"]["method"] == REQUEST_TYPE[1], "did not match request type"
    assert enc[0]["resource"]["account"][0]["reference"] == ACCOUNT_FULL_URL, "did not match account URL"
    assert enc[0]["resource"]["account"][0]["type"] == REFERENCE_TYPE[3], "did not match reference type"
    assert enc[0]["resource"]["class"]["code"] == CLASS_CODE, "did not match class code"
    assert enc[0]["resource"]["class"]["display"] == CLASS_DISPLAY, "did not match class display"
    assert enc[0]["resource"]["class"]["system"] == CLASS_SYSTEM, " did not match class system"
    assert enc[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_SYSTEM[0], "did not match identifier system"
    assert enc[0]["resource"]["identifier"][0]["value"] == f"{MRN}-{FacilityId}-{admitdate}", "did match identifier value"
    assert enc[0]["resource"]["identifier"][1]["system"] == IDENTIFIER_SYSTEM[1], "did not match identifier system"
    assert enc[0]["resource"]["identifier"][1]["value"] == PACID, "did not match pacid"
    assert enc[0]["resource"]["participant"][0]["individual"]["reference"] == ATTENDING_PRACTIONER_FULL_URL, "did not match attending practioner full url"
    assert enc[0]["resource"]["participant"][0]["individual"]["type"] == REFERENCE_TYPE[4], "did not match reference type"
    assert enc[0]["resource"]["participant"][1]["individual"]["reference"] == REFERRING_PRACTIONER_FULL_URL, "did not match referring practioner full url"
    assert enc[0]["resource"]["participant"][1]["individual"]["type"] == REFERENCE_TYPE[4], "did not match reference type"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["code"] == PRACTITIONER_CODE[0], "did not match practitioner code"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[0], "did not match practitioner display"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["system"] == PRACTITIONER_SYSTEM, "did not match practitioner system"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["code"] == PRACTITIONER_CODE[1], "did not match practitioner code"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[1], "did not match practitioner display"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["system"] == PRACTITIONER_SYSTEM, "did not match practitioner system"
    assert enc[0]["resource"]["period"]["start"] == ADMIT_DATETIME, "did not match admit date"
    assert enc[0]["resource"]["period"]["end"] == DISCHARGE_DATETIME, "did not match discharge date"
    assert enc[0]["resource"]["resourceType"] == URL[2], "did not match resource type"
    assert enc[0]["resource"]["serviceProvider"]["reference"] == ORGANIZATION_DEPARTMENT_FULL_URL, "did not match organization department full url"
    assert enc[0]["resource"]["status"] == ENCOUNTER_STATUS, "did not match encounter status"
    assert enc[0]["resource"]["subject"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
    assert enc[0]["resource"]["type"][0]["text"] == (ADMIT_TYPE+"|"+PATIENT_TYPE+"|"+FINANCIAL_CLASS), "did not match admit type or patient type or financial class"

    #Negative tests#
    assert not enc[0]["fullUrl"] == N_ENCOUNTER_FULL_URL, "negative test case failed"
    assert not enc[0]["request"]["ifNoneExist"] == f"identifier=https://pediatrix.com/fhir/NamingSystem/patient-demographics-update-id|{MRN}-{FacilityId}-{DISCHARGE_DATETIME}", "negative test case failed"
    assert not enc[0]["request"]["url"] == N_URL[2], "negative test case failed"
    assert not enc[0]["request"]["method"] == N_REQUEST_TYPE[1], "negative test case failed"
    assert not enc[0]["resource"]["account"][0]["reference"] == N_ACCOUNT_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["account"][0]["type"] == N_REFERENCE_TYPE[3], "negative test case failed"
    assert not enc[0]["resource"]["class"]["code"] == N_CLASS_CODE, "negative test case failed"
    assert not enc[0]["resource"]["class"]["display"] == N_CLASS_DISPLAY, "negative test case failed"
    assert not enc[0]["resource"]["class"]["system"] == N_CLASS_SYSTEM, "negative test case failed"
    assert not enc[0]["resource"]["identifier"][0]["system"] == N_IDENTIFIER_SYSTEM[0], "negative test case failed"
    assert not enc[0]["resource"]["identifier"][0]["value"] == f"{MRN}-{FacilityId}-{admitdate}-12345", "negative test case failed"
    assert not enc[0]["resource"]["identifier"][1]["system"] == N_IDENTIFIER_SYSTEM[1], "negative test case failed"
    assert not enc[0]["resource"]["identifier"][1]["value"] == N_PACID, "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["individual"]["reference"] == N_ATTENDING_PRACTIONER_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["individual"]["type"] == N_REFERENCE_TYPE[4], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["individual"]["reference"] == N_REFERRING_PRACTIONER_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["individual"]["type"] == N_REFERENCE_TYPE[4], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["code"] == N_PRACTITIONER_CODE[0], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["display"] == N_PRACTITIONER_DISPLAY[0], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["system"] == N_PRACTITIONER_SYSTEM, "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["code"] == N_PRACTITIONER_CODE[1], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["display"] == N_PRACTITIONER_DISPLAY[1], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["system"] == N_PRACTITIONER_SYSTEM, "negative test case failed"
    assert not enc[0]["resource"]["period"]["start"] == N_ADMIT_DATETIME, "negative test case failed"
    assert not enc[0]["resource"]["period"]["end"] == N_DISCHARGE_DATETIME, "negative test case failed"
    assert not enc[0]["resource"]["resourceType"] == N_URL[2], "negative test case failed"
    assert not enc[0]["resource"]["serviceProvider"]["reference"] == N_ORGANIZATION_DEPARTMENT_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["status"] == N_ENCOUNTER_STATUS, "negative test case failed"
    assert not enc[0]["resource"]["subject"]["reference"] == N_PATIENT_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["type"][0]["text"] == (N_ADMIT_TYPE+"|"+N_PATIENT_TYPE+"|"+N_FINANCIAL_CLASS)+"12345", "negative test case failed"

    print("FHIR bundle encounter resource tests were successful")