from products import products
def search_products():
    search_running = True
    while search_running:
        # making the input only take y and n and ask to enter again if user enters the 
        # wrong input
    
        take = True
        while take:
            search_choice = input("Do you want to search any id (y/n)").lower()
            if(search_choice =="y" or search_choice  =="n"):
                take = False
                continue
            else:
              print("invalid input try again")
            take =  True

            

        if(search_choice == "y"):

         product_id_valid = True

         while product_id_valid:
            search_product_id = input("Enter the product id : ")

            try:
                search_product_id = int(search_product_id)

                product_id_exist = False

                for product in products:
                    if product["id"] == search_product_id:
                        product_id_exist = True
                        print("product found")
                        print(product)
                        break

                if product_id_exist:
                    product_id_valid = False
                else:
                    print("product not found")
                    print("please enter the valid id")
    
            except ValueError:
               print("please enter a numeric product id")
            # again = input(" do you want to search another product (y/n)?")
            
            product_search_valid = True
            while product_search_valid:
                search_again = input(" do you want to search another product (y/n)?").lower()
                if( search_again == "y" or  search_again == "n"):
                    product_search_valid = False
                    continue
                else :
                    print("enter the valid input")
                                    
                    
        
            if ( search_again == "y"):
              search_running = True
            else:
              search_running = False
            break  
        else:
            search_running = False
            break      
