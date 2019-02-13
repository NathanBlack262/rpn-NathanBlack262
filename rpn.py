from stack import Stack


def evaluate(str):
    stack = Stack()
    opList = str.split()
    for i in opList:
        if i == "+":
            x = stack.pop()
            y = stack.pop()
            stack.push(y + x)
        elif i == "-":
            x = stack.pop()
            y = stack.pop()
            stack.push(y - x)
        elif i == "*":
            x = stack.pop()
            y = stack.pop()
            stack.push(y * x)
        elif i == "/":
            x = stack.pop()
            y = stack.pop()
            stack.push(y / x)
        elif i == "^":
            x = stack.pop()
            y = stack.pop()
            stack.push(y ** x)
        else:
            stack.push(int(i))
    return stack.peek()

def convert(str):
    postfix = []
    operatorStrings = ["+", "-", "*", "/", "^"]
    operators = Stack()
    for char in str:
        if char == "(":
            operators.push(char)
        elif char == ")":
            while not operators.empty():
                x = operators.pop()
                if x != "(":
                    postfix.append(x)
                else:
                    break
        elif char in operatorStrings:
            while not operators.empty():
                if operators.peek() == "(":
                    operators.pop()
                    break
                else:
                    if char == "+" or char == "-":
                        if operators.peek() in operatorStrings:
                            postfix.append(operators.pop())
                        else:
                            break
                    elif char == "*" or char == "/":
                        if operators.peek() == "/" or operators.peek() == "*" or operators.peek() == "^":
                            postfix.append(operators.pop())
                        else:
                            break
                    else:
                        if operators.peek() == "^":
                            postfix.append(operators.pop())
                        else:
                            break
            operators.push(char)
        else:
            postfix.append(char)
    while not operators.empty():
        postfix.append(operators.pop())
    postfixNotation = ''.join(postfix)
    lastSpace = False
    for i in range(3):
        for j in range(1, len(postfixNotation)):
            if postfixNotation[j] != " ":
                if postfixNotation[j-1] != " ":
                    postfixNotation = postfixNotation[:j] + " " + postfixNotation[j:]
                lastSpace = False
            else:
                if postfixNotation[j-1] == " ":
                    postfixNotation = postfixNotation[:j]  + postfixNotation[j+1:]
                lastSpace = True
    return postfixNotation
            
def rpnCalculator():
    stack = Stack()
    while True:
        if stack.empty():
            print("Stack: Empty")
        else:
            x = stack.pop()
            if stack.empty():
                print("Stack: " + str(x))
                stack.push(x)
            else:
                y = stack.pop()
                print("Stack: " + str(y))
                print("Stack: " + str(x))
                stack.push(y)
                stack.push(x)
        i = input(">>> (Type 'stop' at any time to stop calculator) ")
        if i == "+":
            x = stack.pop()
            y = stack.pop()
            stack.push(y + x)
        elif i == "-":
            x = stack.pop()
            y = stack.pop()
            stack.push(y - x)
        elif i == "*":
            x = stack.pop()
            y = stack.pop()
            stack.push(y * x)
        elif i == "/":
            x = stack.pop()
            y = stack.pop()
            stack.push(y / x)
        elif i == "^":
            x = stack.pop()
            y = stack.pop()
            stack.push(y ** x)
        elif i == "stop":
            print("Thanks for using!")
            break
        else:
            stack.push(int(i))
    

def main():
    rpnCalculator()
#    useLoop = True
#    againLoop = True
#    while useLoop:
#        function = input("Would you like to evaluate an (R)PN or (I)nfix expression? ")
#        if function.lower() != "r" and function.lower() != "i" :
#            print("Invalid input.")
#        else:
#            insert = input("Enter the expression here: ")
#            if insert == "":
#                insert = "0"
#            if function.lower() == "r":
#                print(evaluate(insert))
#            else:
#                print(evaluate(convert(insert)))
#            again = input("Use again? ")
#            if again.lower() == "n" or again.lower() == "no":
#                print("Thanks for using!")
#                break
            
                
    


if __name__ == "__main__":
    main()
            
            
    
    