from stack import Stack

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