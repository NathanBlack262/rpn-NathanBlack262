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
        else:
            stack.push(int(i))
    return stack.peek()

def convert(str):
    postfix = []
    operatorStrings = ["+", "-", "*", "/"]
    operators = Stack()
    for char in str:
        if char == "(":
            operators.push(char)
        elif char == ")":
            while True:
                x = operators.pop()
                if x != "(":
                    postfix.append(x)
                else:
                    postfix.append(x)
                    break
        elif char in operatorStrings:
            while not operators.empty():
                if operators.peek() == "(":
                    postfix.append(operators.push())
                    break
                else:
                    if char == "+":
                        if char == "/" or char == "*":
                            postfix.append(operators.pop())
                        else:
                            break
        else:
            postfix.append(char)
    while not operators.empty():
        postfix.append(operators.pop())
    return ' '.join(postfix)
            
        

def main():
    print(convert("1 * 2 + 3 * 4 + 5 * 6 + 7 * 8"))
#    import doctest
#    doctest.testfile('rpn_tester.txt')
    


if __name__ == "__main__":
    main()
            
            
    
    