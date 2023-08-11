from .reg_globals.reference_urls import(
    PATIENT_FULL_URL,
    ENCOUNTER_FULL_URL,
    ACCOUNT_FULL_URL,
    ATTENDING_PRACTIONER_FULL_URL,
    REFERRING_PRACTIONER_FULL_URL,
    ORGANIZATION_DEPARTMENT_FULL_URL,
)

from .reg_globals.patient_reg_global import(
    MRN
)

from .reg_globals.organization_reg_globals import(
    FACILITY_ID
)

from .reg_globals.request_type import(
    REQUEST_TYPE,
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
    PRACTITIONER_CODE,
    PRACTITIONER_DISPLAY,
    PRACTITIONER_SYSTEM,
    ENCOUNTER_STATUS
)

from .reg_globals.identifier_urls import(
    IDENTIFIER_URL,
    IDENTIFIER_ID,
    RESOURCE_NAME
)

from omniparser_schemas.parser.filter import filter_resource

def enc_test(resource_name, testfile, identifier_url, identifier_id):
    enc = filter_resource(resource_name, testfile, identifier_url, identifier_id)
    admitdate = ADMIT_DATETIME
    admitdate = admitdate.replace("-", "")
    assert enc[0]["fullUrl"] == ENCOUNTER_FULL_URL, "did not match encounter URL"
    assert enc[0]["request"]["ifNoneExist"] == f"identifier={IDENTIFIER_URL}/{IDENTIFIER_ID[6]}|{MRN}-{FACILITY_ID}-{admitdate}", "identifier did not match"
    assert enc[0]["request"]["url"] == RESOURCE_NAME[3], "did not match request url"
    assert enc[0]["request"]["method"] == REQUEST_TYPE[1], "did not match request type"
    assert enc[0]["resource"]["account"][0]["reference"] == ACCOUNT_FULL_URL, "did not match account URL"
    assert enc[0]["resource"]["account"][0]["type"] == RESOURCE_NAME[0], "did not match reference type"
    assert enc[0]["resource"]["class"]["code"] == CLASS_CODE, "did not match class code"
    assert enc[0]["resource"]["class"]["display"] == CLASS_DISPLAY, "did not match class display"
    assert enc[0]["resource"]["class"]["system"] == CLASS_SYSTEM, " did not match class system"
    assert enc[0]["resource"]["identifier"][0]["system"] ==  f'{IDENTIFIER_URL}/{IDENTIFIER_ID[6]}', "did not match identifier system"
    assert enc[0]["resource"]["identifier"][0]["value"] == f"{MRN}-{FACILITY_ID}-{admitdate}", "did match identifier value"
    assert enc[0]["resource"]["identifier"][1]["system"] ==f'{IDENTIFIER_URL}/{IDENTIFIER_ID[7]}', "did not match identifier system"
    assert enc[0]["resource"]["identifier"][1]["value"] == PACID, "did not match pacid"
    assert enc[0]["resource"]["participant"][0]["individual"]["reference"] == ATTENDING_PRACTIONER_FULL_URL, "did not match attending practioner full url"
    assert enc[0]["resource"]["participant"][0]["individual"]["type"] == RESOURCE_NAME[6], "did not match reference type"
    assert enc[0]["resource"]["participant"][1]["individual"]["reference"] == REFERRING_PRACTIONER_FULL_URL, "did not match referring practioner full url"
    assert enc[0]["resource"]["participant"][1]["individual"]["type"] == RESOURCE_NAME[6], "did not match reference type"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["code"] == PRACTITIONER_CODE[0], "did not match practitioner code"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[0], "did not match practitioner display"
    assert enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["system"] == PRACTITIONER_SYSTEM, "did not match practitioner system"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["code"] == PRACTITIONER_CODE[1], "did not match practitioner code"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[1], "did not match practitioner display"
    assert enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["system"] == PRACTITIONER_SYSTEM, "did not match practitioner system"
    assert enc[0]["resource"]["period"]["start"] == ADMIT_DATETIME, "did not match admit date"
    assert enc[0]["resource"]["period"]["end"] == DISCHARGE_DATETIME, "did not match discharge date"
    assert enc[0]["resource"]["resourceType"] == RESOURCE_NAME[3], "did not match resource type"
    assert enc[0]["resource"]["serviceProvider"]["reference"] == ORGANIZATION_DEPARTMENT_FULL_URL, "did not match organization department full url"
    assert enc[0]["resource"]["status"] == ENCOUNTER_STATUS, "did not match encounter status"
    assert enc[0]["resource"]["subject"]["reference"] == PATIENT_FULL_URL, "did not match patient full url"
    assert enc[0]["resource"]["type"][0]["text"] == (ADMIT_TYPE+"|"+PATIENT_TYPE+"|"+FINANCIAL_CLASS), "did not match admit type or patient type or financial class"

    #Negative tests#
    assert not enc[0]["fullUrl"] == PATIENT_FULL_URL, "negative test case failed"
    assert not enc[0]["request"]["ifNoneExist"] == DISCHARGE_DATETIME, "negative test case failed"
    assert not enc[0]["request"]["url"] == RESOURCE_NAME[2], "negative test case failed"
    assert not enc[0]["request"]["method"] == REQUEST_TYPE[0], "negative test case failed"
    assert not enc[0]["resource"]["account"][0]["reference"] == ENCOUNTER_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["account"][0]["type"] == RESOURCE_NAME[3], "negative test case failed"
    assert not enc[0]["resource"]["class"]["code"] == CLASS_SYSTEM, "negative test case failed"
    assert not enc[0]["resource"]["class"]["display"] == CLASS_CODE, "negative test case failed"
    assert not enc[0]["resource"]["class"]["system"] == CLASS_DISPLAY, "negative test case failed"
    assert not enc[0]["resource"]["identifier"][0]["system"] == IDENTIFIER_URL[0], "negative test case failed"
    assert not enc[0]["resource"]["identifier"][0]["value"] == admitdate, "negative test case failed"
    assert not enc[0]["resource"]["identifier"][1]["system"] == IDENTIFIER_ID[1], "negative test case failed"
    assert not enc[0]["resource"]["identifier"][1]["value"] == IDENTIFIER_ID, "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["individual"]["reference"] == REFERRING_PRACTIONER_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["individual"]["type"] == RESOURCE_NAME[1], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["individual"]["reference"] == ATTENDING_PRACTIONER_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["individual"]["type"] == RESOURCE_NAME[2], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["code"] == PRACTITIONER_SYSTEM[0], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[1], "negative test case failed"
    assert not enc[0]["resource"]["participant"][0]["type"][0]["coding"][0]["system"] == PRACTITIONER_CODE, "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["code"] == PRACTITIONER_SYSTEM[1], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["display"] == PRACTITIONER_DISPLAY[0], "negative test case failed"
    assert not enc[0]["resource"]["participant"][1]["type"][0]["coding"][0]["system"] == PRACTITIONER_CODE, "negative test case failed"
    assert not enc[0]["resource"]["period"]["start"] == DISCHARGE_DATETIME, "negative test case failed"
    assert not enc[0]["resource"]["period"]["end"] == ADMIT_DATETIME, "negative test case failed"
    assert not enc[0]["resource"]["resourceType"] == RESOURCE_NAME[2], "negative test case failed"
    assert not enc[0]["resource"]["serviceProvider"]["reference"] == PATIENT_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["status"] == 1, "negative test case failed"
    assert not enc[0]["resource"]["subject"]["reference"] == ACCOUNT_FULL_URL, "negative test case failed"
    assert not enc[0]["resource"]["type"][0]["text"] == "failed", "negative test case failed"

    print("FHIR bundle encounter resource tests were successful")