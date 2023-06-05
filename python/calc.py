def add(num1,num2)
    total = num1+num2
    return total
def subtract(num1,num2):
    total = num1-num2
    return total
def multiply(num1,num2):
    total = num1*num2
    return total
def divide(num1,num2):
    total = num1+num2
    return total


def input_handler():
    try:
        print('1. ADD')
        print('2. SUBTRACT')
        print('3. MULTIPLY')
        print('4. DIVIDE')

        operation = input('selection')

        perform_calc(operation)

    except TypeError:
        print('enter a number')
    except ValueError:
        print('enter within 2-4')
    except:
        print('something went wrong')

def perform_calc(chosen_opp):
    try:
        if(chosen_opp == "1"):
            num1 = int(input("enter first number"))
            num2 = int(input("enter second number"))
            add(num1,num2)
        elif(chosen_opp == "2"):
            num1 = int(input("enter first number"))
            num2 = int(input("enter second number"))
            subtract(num1,num2)
        elif(chosen_opp == "3"):
            num1 = int(input("enter first number"))
            num2 = int(input("enter second number"))
            multiply(num1,num2)
        elif(chosen_opp == "4"):
            num1 = int(input("enter first number"))
            num2 = int(input("enter second number"))
            divide(num1,num2)
    except ValueError:
        print("invalid input")

    except TypeError:
        print("enter a number")
    
    except:
        print("error")




input_handler()