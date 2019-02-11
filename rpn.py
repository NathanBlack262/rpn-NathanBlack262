from stack import Stack


def evaluate(str):
    '''
    >>> evaluate("5 2 +")
    7
    >>> evaluate("7 3 -")
    4
    >>> evaluate("3 8 2 * +")
    19
    >>> evaluate("3 6 2 - *")
    12
    >>> evaluate("4 7 + 6 2 - *")
    44
    >>> evaluate("5 7 - 8 1 2 + * -")
    -26

    '''
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

def main():
    import doctest
    doctest.testfile('rpn_tester.txt')
    


if __name__ == "__main__":
    main()
            
            
    
    