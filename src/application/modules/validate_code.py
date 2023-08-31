def validate_code(sent_code, entered_code):

    if sent_code.lower() == entered_code.lower():
        return True
    else:
        return False

def old_validate_code(sent_code, entered_code):
    # Split the sent enteredcode into components
    sent_code_components = sent_code.split("_")

    # Split the user enteredcode into components
    entered_code_components = entered_code.split("_")

    # Check if the code has the expected number of components
    if len(sent_code_components) != 2:
        return False
    
    # Check if the code has the expected number of components
    if len(entered_code_components) != 2:
        return False

    # Extract the sent code components
    sent_code_school_name, sent_code_digit = sent_code_components
   
   # Extract the user entered code components
    entered_code_school_name, entered_code_digit = entered_code_components

    # Validate the code
    if entered_code_school_name.lower() == sent_code_school_name.lower() and entered_code_digit.isdigit() == sent_code_digit.isdigit() and len(entered_code_digit) == 2:
        return True
    else:
        return False
    

def split_names(name_and_surname):
    # Split the name_and_surname into components using space
    name_components = name_and_surname.split()

    # Ensure there are at least two components (first name and last name)
    if len(name_components) >= 2:
        looked_first_name = name_components[0]
        looked_name = ' '.join(name_components[1:])
    else:
        looked_first_name = ""
        looked_name = ""

    return looked_name, looked_first_name
