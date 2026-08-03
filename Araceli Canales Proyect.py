
# Online Python - IDE, Editor, Compiler, Interpreter

#Defining the functin that contains the pizza order program
def pizza_order():
    
    # created two variables size (string) and price (int)
    size =input("What size pizza?")
    price=int(input("How much is it?"))
    
    #didplay the information stored in the variables

    print("Your order",size,"pizza",price)
    
    #use a conditional statement to make a desision based on price
    
    if price > 20: 
       print("Is too expensive")
    
    else:
       print("Good price!!!")  
       
       #calling the function to execute
    
pizza_order ()    

