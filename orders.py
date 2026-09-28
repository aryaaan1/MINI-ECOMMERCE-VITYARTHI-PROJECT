import json
def load_orders():
    try:
        with open("orders.json","r")as file:
           order_history = json.load(file)
    except (json.JSONDecodeError,FileNotFoundError):
       order_history = []    
    return order_history   
def get_next_order_id(order_history):
    if order_history:
      try:
        last_order_id = order_history[-1]["order_id"]
        order_count = int(last_order_id[3:])
      except (KeyError,ValueError,TypeError):
        order_count = 1000

    else:
       order_count = 1000    
    order_count += 1
    order_id = "ORD"+str(order_count)   
    return order_id

def save_order(order_history,order):
   order_history.append(order)
   with open("orders.json","w")as file:
            json.dump(order_history,file)

