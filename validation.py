def validate_name():
    valid_customer_name = True
    while valid_customer_name:
                            customer_name = input("ENTER YOUR NAME : ").strip()
    
                            if customer_name == "":
                                print("Name cannot be empty")
                            elif not customer_name.replace(" ", "").isalpha():
                                print("Name should contain only letters")
                            else:
                                return customer_name
def validate_phone():
        
                            valid_customer_phone = True
        
                            while valid_customer_phone:
                                customer_phone = input("ENTER YOUR PHONE NUMBER : ").strip()
        
                                if not customer_phone.isdigit():
                                    print("Phone number should contain only digits")
                                elif len(customer_phone) != 10:
                                    print("Phone number must contain exactly 10 digits")
                                else:
                                    return customer_phone
def validate_address():  
                            valid_customer_address = True
        
                            while valid_customer_address:
                                customer_address = input("ENTER YOUR ADDRESS : ").strip()
        
                                if customer_address == "":
                                    print("Address cannot be empty")
                                elif len(customer_address) < 5:
                                    print("Please enter a valid address")
                                else:
                                    return customer_address                            
                                        
