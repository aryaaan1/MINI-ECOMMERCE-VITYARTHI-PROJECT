
from products import products
from search import search_products
from cart import shopping
from orders import load_orders,get_next_order_id,save_order
from customer import get_customer_details
order_history = load_orders()    


take = True
while take:
    for product in products:
        print(f"{product["id"]:<4}{product["name"]:<25}")

    # for searching the product 
    search_products()



    # for adding the items in the cart
    cart,Check_out = shopping()
    if(Check_out =="y"):

                    if not cart:
                        print("your cart is empty ")
                        print("please add a product before checkout")

                
                    else:
                        final_Total = 0

                        for items in cart:
                            Sub_total = 0
                            for product in products:
                                if product["id"] == items["id"]:
                                    Sub_total += product["price"] * items["quantity"]
                                    final_Total += Sub_total
    # for error handling the inputs 
                    
                        customer_name,customer_phone,customer_address = get_customer_details()
                        order_id = get_next_order_id(order_history)
                        order = {"name":customer_name,"order_id":order_id,"phone number":customer_phone,"address":customer_address,"items":cart,"Total":final_Total}
                        save_order(order_history,order)
                    

                        print("proceeding to checkout ")
                        print("CUSTOMER NAME :",order["name"])
                        print("PHONE NUMBER : ",order["phone number"])
                        print("ADDRESS : ",order["address"])
                        print("ITEMS : ",order["items"])
                        print()
                        print("ORDER ID : ",order_id    )
                        print("TOTAL : ",order["Total"])
                        print("ORDER HISTORY",order_history)  

    another_order_choice = input("Do you eant to add another order(y/n)").lower()
    while another_order_choice!="y" and another_order_choice!= "n":
        print("please enter only y or n")
        another_order_choice = input( "Do you want to add another order(y/n): ").lower()
    if another_order_choice== "n":
            take = False
                                                                  
                        
   




            
        


     
    
   



