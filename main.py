
    # calculating

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


    # print(int(division(4,2)))
calculation = {"+": add,
                   "-": subtract,
                   "*": mult,
                   "/": division
                   }


def calculator():
    should_acumulate = True
    first_no = (int(input("Enter your 1st number: ")))
        # answer=calculation["+"](first_no,second_no)
    while should_acumulate:
        for symbol in calculation:
            print(symbol)
        math_type = input("Pick an operation\n")
        second_no = (int(input("Enter your second number: ")))
        answer = calculation[math_type](first_no, second_no)
        print(f"{first_no} {math_type} {second_no} = {answer}")

        next_operation = input(f"Type 'y' for continue calculation with {answer} type 'n for star new operation: ")

        if next_operation == "y":
            first_no = answer
        elif next_operation == "n":
            should_acumulate = False
            print("\n" * 20)
            calculator()


calculator()
