from validation import validate_name,validate_phone,validate_address
def get_customer_details():
    customer_name = validate_name()
    customer_phone = validate_phone()
    customer_address = validate_address()
    return customer_name,customer_phone,customer_address
