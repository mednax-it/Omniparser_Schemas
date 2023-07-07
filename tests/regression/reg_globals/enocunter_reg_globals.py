ADMIT_TYPE="NB"
PATIENT_TYPE="CONF"
FINANCIAL_CLASS="COMM C"
ADMIT_DATETIME="2023-04-11"
DISCHARGE_DATETIME="2023-05-11"
PACID="pacid123"

CLASS_CODE="IMP"
CLASS_DISPLAY="inpatient encounter"
CLASS_SYSTEM="http://terminology.hl7.org/CodeSystem/v3-ActCode"
IDENTIFIER_SYSTEM=["https://pediatrix.com/fhir/NamingSystem/patient-demographics-update-id", "https://pediatrix.com/fhir/NamingSystem/pac-id"]

PRACTITIONER_CODE=["ATND","REF"]
PRACTITIONER_DISPLAY=["Attending","Referring"]
PRACTITIONER_SYSTEM="http://terminology.hl7.org/CodeSystem/v3-ParticipationType"

ENCOUNTER_STATUS="planned"

#Negative test cases data
N_ADMIT_TYPE="1"
N_PATIENT_TYPE="CONF123"
N_FINANCIAL_CLASS="123"
N_ADMIT_DATETIME="2023:04:11"
N_DISCHARGE_DATETIME="2023-05-11:11"
N_PACID="pacid:123"

N_CLASS_CODE="IMP:123"
N_CLASS_DISPLAY="patient encounter"
N_CLASS_SYSTEM="http://terminology.hl7.org/CodeSystem1/v4-ActCode"
N_IDENTIFIER_SYSTEM=["https://pediatrix.com/fhir/NamingSystem/patient-demographics-updates-id", "https://pediatrix.com/fhir/NamingSystem/pacs-id"]

N_PRACTITIONER_CODE=["ATNDING","REFE"]
N_PRACTITIONER_DISPLAY=["Attendee","Refer"]
N_PRACTITIONER_SYSTEM="http://terminology.hl7.org/CodeSystem/v4-ParticipationTypes"

N_ENCOUNTER_STATUS=1