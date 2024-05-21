def check_if_FHIR_resource_element_exists(data, index, path, subpath):
    try:
        data[index][path][subpath]
        return False
    except KeyError:
        return "FHIR resource element not found"

