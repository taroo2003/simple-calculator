operation_history = []

#functions for arithmatic operations 
def add(a,b):
    return f"{a} + {b} = {a + b}"
    
def subtract(a,b):
    return f"{a} - {b} = {a - b}"
    
def multiply(a,b):
    return f"{a} * {b} = {a * b}"
    
def divide(a,b):  
    return f"{a} / {b} = {a / b}"

def power(a,b):
    return f"{a} ^ {b} = {a ** b}"
    
def remainder(a,b):
    return f"{a} % {b} = {a % b}"



def history(operation):
    operation_history.append(operation)


def get_operands():
    a = input("Enter first number: ")
    print(a)
           
    if '$' in a : 
        return 0
    elif '#' in a:
        return '#','#'
     
    try:
        float(a) 
        
        b = input("Enter second number: ")
        print(b)

        if '$' in b:
            return 0
        elif '#' in b:
            return '#','#'
        
        try:
            float(b)
            return float(a),float(b)
        except:
            print("Not a valid number, please enter again")
            return get_operands()
    except:
        print("Not a valid number, please enter again")
        return get_operands()
    
  


def select_op(choice):
    if choice == '#':
        return -1
    
    elif choice == '$':
        return None
    
    elif choice == '?':
        if len(operation_history) == 0:
            print("No past calculations to show")
        
        for operation in operation_history:
            print(operation)
        return None
    
    elif choice not in ('+','-','*','/','^','%'):
        print("Unrecognized operation")
        return None
    
    try:
        a,b = get_operands()
        if a == '#' and b == '#':
            return -1
    except: 
        return None
    
    if choice == "+":
        print(add(a,b))
        history(add(a,b))

    elif choice == "-":
        print(subtract(a,b))
        history(subtract(a,b))

    elif choice == "*":
        print(multiply(a,b))
        history(multiply(a,b))
        
    elif choice == "/":
        try:
            print(divide(a,b))
            history(divide(a,b))
        except:
            print("float division by zero")
            print(f"{a} / {b} = {None}")
            history(f"{a} / {b} = {None}")
        
    elif choice == "^":
        print(power(a,b))
        history(power(a,b))
        
    elif choice == "%":
        print(remainder(a,b))
        history(remainder(a,b))



#This is the main loop. 
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()