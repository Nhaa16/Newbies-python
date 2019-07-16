def factorial():
    
    number = int(input("Enter a number\n"))
    
    fact = 1
    
    for i in range(1, number + 1):
        fact = fact * i
        print(fact)
        
        
        
factorial()