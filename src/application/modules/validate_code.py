def validate_code(code, school_name):
    # Split the code into components
    code_components = code.split("_")

    # Check if the code has the expected number of components
    if len(code_components) != 2:
        return False

    # Extract the code components
    extracted_school_name, extracted_code = code_components

    # Validate the code
    if extracted_school_name.lower() == school_name.lower() and extracted_code.isdigit() and len(extracted_code) == 2:
        return True
    else:
        return False