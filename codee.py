def calculator():
    
    text="Welcome to the Python Calculator"
    width=80
    fillchar=' '
    first_line=text.center(width,fillchar)
    print (first_line)
    print("-" * 80) ; print()
    while True:
        expression = input("Please enter a mathematical expression (or 'quit' to exit): ") ; print()
        print("-" * 80) ; print() 
        if expression.lower() == "quit":
            print("Thanks for using the Python Calculator!")
            break
        try:
            result = eval(expression)
            if isinstance(result, int):
                print(f"The result is: {result}\n")
                print("-" * 80) ; print()
            else:
                print(f"The result is: {result:.3f}\n")
                print("-" * 80) ; print()
        except:
            print("Invalid input. Please try again.\n")
            print("-" * 80) ; print()

calculator()
