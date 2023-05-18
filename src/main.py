from stack import Stack
from termcolor import colored

# Check Parentheses Correctness
def isCorrect(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == "(":
            stack.push("(")
        elif p == ")":
            if stack.size() == 0:
                return False
            else:
                stack.pop()
        else:
            continue
    if stack.size() > 0:
        return False
    else:
        return True
    
# Main function
def main():
    # Welcome Messages
    print(colored("===> Hello, Welcome To Parenthesis Correctness <=== \n", "blue", attrs=["dark"]))

    # Get Parentheses From User
    parentheses = input(colored("Please Enter Parentheses: ", "light_green"))

    # Run Until User Enter 0
    while parentheses != "0":
        if isCorrect(parentheses):
            print(colored("\n    Nice", "magenta", attrs=["dark"]))
        else:
            print(colored("\nWhat The Hell", "magenta", attrs=["dark"]))
        print(colored("~.~.~.~.~.~.~", "yellow", attrs=["dark"]))

        # Get Parentheses From User
        parentheses = input("Enter The Parentheses (Enter 0 If You Want To End This!) : ")

    # Developers
    print(colored("\nThank You For Choosing Us :)\n>>>Developed By Maryam Fakhraei & Amirhossein Naseri<<<", "cyan"))

if __name__ == "__main__":
    main()