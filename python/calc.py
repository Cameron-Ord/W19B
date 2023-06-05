#functions for performing math opperations

def add(num1,num2):
    result = num1+num2
    print(result)
    return result
def subtract(num1,num2):
    result = num1-num2
    print(result)
    return result
def multiply(num1,num2):
    result = num1*num2
    print(result)
    return result
def divide(num1,num2):
    result = num1/num2
    print(result)
    return result



#function called on script execute, takes user input based on the options given.
def input_handler():
    try:
        print('1. ADD')
        print('2. SUBTRACT')
        print('3. MULTIPLY')
        print('4. DIVIDE')
            #takes the user input and calls the next function using the user input as the arguement for perform_calc()
        operation = input('selection')

        perform_calc(operation)

    except TypeError:
        print('enter a number')
    except ValueError:
        print('enter within 2-4')
    except:
        print('something went wrong')



def perform_calc(chosen_opp):
    #calls respective function, takes user input, then calls the respective function passing off the users input as arguements
    #since it does not convert the users initial choice into an integer, i used strings here
    try:
        if(chosen_opp == '1'):
            num1 = int(input('enter first number'))
            num2 = int(input('enter second number'))
            add(num1,num2)
        elif(chosen_opp == '2'):
            num1 = int(input('enter first number'))
            num2 = int(input('enter second number'))
            subtract(num1,num2)
        elif(chosen_opp == '3'):
            num1 = int(input('enter first number'))
            num2 = int(input('enter second number'))
            multiply(num1,num2)
        elif(chosen_opp == '4'):
            num1 = int(input('enter first number'))
            num2 = int(input('enter second number'))
            divide(num1,num2)
    except ValueError:
        print('invalid input')

    except TypeError:
        print('enter a number')
    
    except:
        print('error')


#calls this function on execute

input_handler()