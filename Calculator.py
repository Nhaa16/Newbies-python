def calculate():
    
    
    operation = str(input("Add, Subtract, Divide, Multiply: ")).capitalize()
    number_1 = int(input("Please enter your first number "))
    number_2 = int(input("Please enter your second number "))
    
    if operation == "Add":
        result = number_1 + number_2
        print(result)
        
    elif operation == "Subtract":
        result = number_1 - number_2
        print(result)
        
    elif operation == "Divide":
        result = number_1 / number_2
        print(result)
    
    elif operation == "Multiply":
        result = number_1 * number_2
        print(result)
        
    else:
        print('This is an invalid operation')
        
        
calculate()
        
        