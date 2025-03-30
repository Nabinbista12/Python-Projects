# Basic Calculator** → Perform basic arithmetic operations.

def calculator(x, n, y):
    if n == '+':
        add_num(x, y)
    if n == '-':
        sub_num(x, y)
    if n == '*':
        mult_num(x, y)
    if n == '/':
        div_num(x, y)
         
def add_num(x, y):
    print('Addition:', x + y)

def sub_num(x, y):
    print('Subtraction:', x - y)
 
def mult_num(x, y):
    print('Multiplication:', x * y)

def div_num(x, y):
    try:
        print("Divide:", x / y)
    except Exception as e:
        print("err occured:", e)



def main():
    print("Enter 'q' to quit the program")
    print("---------------------------'q' to quit the program----------------------------")
    print()
    while True:
        first_num = input("Enter a first number: ")
        if first_num == 'q':
            break
        try:
            first_num = int(first_num)
        except:
            print("Enter a correct number: ")
            continue

        print()
        active = True        
        while active:
            operand = input("Enter '/', '*', '-', '+' for the operation you want: ")
        
            if operand == 'q':
                active = False
            
            if operand == '+' or operand == '-' or operand == '/' or operand == '*':
                break
        
        print()
        while True:
            second_num = input("Enter a second number: ")
            if second_num == 'q':
                break
            try:
                second_num = int(second_num)
                break
            except:
                print("Enter a interger")
                 
        print()     
        try:
            calculator(first_num, operand, second_num)
        except:
            print("Enter the correct option")
        print()


if __name__ == "__main__":
    main()
