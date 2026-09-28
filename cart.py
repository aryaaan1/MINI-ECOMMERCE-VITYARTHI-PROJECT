from products import products

def shopping():
    cart = []

    shopping_running = True
    while shopping_running:
            cart_item ={}
            valid_product_id = True
            while valid_product_id:
                product_id = input("enter the product id you want to add to the cart : ")

                try:
                    product_id  = int( product_id )

                    product_exists = False

                    for product in products:
                        if product["id"] ==  product_id :
                            product_exists = True
                            print("product found")
                            print(product)
                            break

                    if product_exists:
                        valid_product_id = False
                    else:
                        print("product not found")
                        print("please enter a valid product id")

                except ValueError:
                    print("enter a numeric product id")
                    # for quantity 
            valid_quantity = True
            while valid_quantity:
                        quantity =(input("enter the quantity of product : "))
                        try:
                            quantity = int( quantity)
                            if( quantity<=0):
                                print("invalid")   
                            
                            else:
                                print("valid")    
                                valid_quantity = False
                            
                        except ValueError:
                            print("enter a numeric number")  
            cart_item = {"id":product_id,"quantity": quantity}
            item_already_in_cart = False

            for item in cart:
                if item["id"] == product_id:
                    item["quantity"] += quantity
                    item_already_in_cart = True
                    break

            if not item_already_in_cart:
                cart.append(cart_item)
                
            print("YOUR CART IS : ")    
            print('''PRODUCT           PRICE QUANTITY''')
            # for adding total price
            Total = 0
            for items in cart:
                Sub_Total = 0
                for product in products:
                    if(product["id"]==items["id"]):
                        print(f"{product["name"]:<20}{product["price"]:<5}{items["quantity"]:<3}")
                        Sub_Total +=( product["price"]*items['quantity'])
                        print("YOUR TOTAL IS : ",Sub_Total)
                        Total +=Sub_Total
            print("YOUR OVER ALL TOTAL IS :",Total) 
             # for removing items from the cart
            valid_input = True
            while valid_input:
                remove_choice = input("DO YOU WANT TO REMOVE ANY PRODUCT(y/n)").lower()
                if (remove_choice == "y" or remove_choice == "n"):
                    valid_input = False
                else:
                     print("please enter only y and n ")    
                if(remove_choice=="y"):
                        # item_remove = int(input("enter the id of the product you want to remove : "))
                        # validate product id for removal
                        valid_remove_id = True
            
                        while valid_remove_id:
                            remove_product_id = input("enter the id of the product you want to remove : ")
            
                            try:
                                remove_product_id= int(remove_product_id)
            
                                # check whether product exists in cart
                                product_in_cart = False
            
                                for item in cart:
                                    if item["id"] == remove_product_id:
                                        product_in_cart = True
                                        break
            
                                if product_in_cart:
                                    valid_remove_id = False
                                else:
                                    print("product is not present in the cart")
            
                            except ValueError:
                                print("please enter a numeric product id")
                        # remove the item from cart
            
                        for item in cart:
                            if remove_product_id == item["id"]:
                                cart.remove(item)
                                print("product removed successfully")
                                break
            
            
                        # display updated cart and calculate total
            
                        Total_after_removal = 0
            
                        print("YOUR CART IS : ")
                        print('''PRODUCT           PRICE QUANTITY''')
            
                        for item in cart:
            
                            for product in products:
            
                                if product["id"] == item["id"]:
            
                                    Sub_total_after_removal = product["price"] * item["quantity"]
            
                                    print(f"{product["name"]:<20}{product["price"]:<5}{item["quantity"]:<3}")
            
                                    Total_after_removal += Sub_total_after_removal
            
                        print("YOUR OVER ALL TOTAL IS :", Total_after_removal)
            
            if cart:            
                valid_input = True
                while valid_input:
                    update_choice = input("DO YOU WANT TO CHANGE THE PRODUCT QUANTITY(y/n)").lower()
                    if  update_choice == "y" or update_choice  == "n":
                        valid_input =  False
                    else:
                        print("please enter only y and n")    
                if(  update_choice =="y"):
                    # item_update_id = int(input("enter the id of the product you want to update : "))
                    # quantity_update = int(input("enter the quantity you want to change : ")) 
                    # validate product id
                    valid_update_id = True

                    while valid_update_id:
                        update_product_id = input("enter the id of the product you want to update : ")

                        try:
                            update_product_id = int(  update_product_id)

                            # check whether product exists in cart
                            product_in_cart = False

                            for item in cart:
                                if item["id"] ==   update_product_id:
                                    product_in_cart = True
                                    break

                            if product_in_cart:
                                valid_update_id = False
                            else:
                                print("product is not present in the cart")

                        except ValueError:
                            print("please enter a numeric product id")


                # validate quantity
                    valid_update_quantity = True
                
            
                    while valid_update_quantity:
                        new_quantity = input("enter the quantity you want to change : ")
                    
                        try:
                            new_quantity = int(new_quantity)

                            if new_quantity <= 0:
                                print("quantity must be greater than 0")
                            else:
                                valid_update_quantity = False

                        except ValueError:
                                print("please enter a numeric quantity")
                    updated_total = 0 
                    for item in cart:
                        if(update_product_id == item["id"]):
                            item["quantity"] = new_quantity
                            break
                    print("YOUR CART IS : ")    
                    print('''PRODUCT           PRICE QUANTITY''')    
                    for item in cart:
                        Sub_total = 0
                        for product in products:
                            if(product["id"]==item["id"]):
                                
                                    print(f"{product["name"]:<20}{product["price"]:<5}{item["quantity"]:<3}")
                                    Sub_total +=(product["price"]*item["quantity"])
                                    print("YOUR TOTAL IS : ",Sub_total)
                                    updated_total += Sub_total                         
                    print("YOUR OVER ALL TOTAL IS :", updated_total) 
             # add another product
         # add another product
            valid_input = True
            while valid_input:
                add_another_product = input(" do you want to add another product (y/n)?").lower()
                if add_another_product == "y"or add_another_product == "n":
                    valid_input = False
                else:
                    print("plese enter only y or n ")    
            if (add_another_product  == "y"):
                    shopping_running = True
            else:
                    valid_input= True
                    while valid_input:
                                Check_out = input("enter do you want to checkout (y/n)").lower()
                                if Check_out == "y" or Check_out =="n":
                                    valid_input = False
                                else:
                                    print("Please enter only y or n")    
                    return cart,Check_out                
                                  