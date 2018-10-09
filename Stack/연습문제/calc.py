from stack import ArrayStack

def split_tokens(expr):
    """
    문자열로 들어온 수식을 list로 분할
    :param expr:
    :return: 수식을 피연산자,연산자로 분할한 list
    """
    tokens = []
    val = 0
    val_processing = False

    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            val_processing = True
        else:
            if val_processing:
                tokens.append(val)
                val = 0
            val_processing = False
            tokens.append(c)

    if val_processing:
        tokens.append(val)

    return tokens

def infix_to_potfix(token_list):
    """
    들어온 중위 표현식을 후위 표현식으로 변경
    :param token_list:
    :return: 후위 표현식
    """
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    opStack = ArrayStack()
    result = []

    for token in token_list:
        if isinstance(token, int):
            result.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                result.append(opStack.pop())
            opStack.pop()
        else:
            if not opStack.isEmpty():
                if prec[opStack.peek()] >= prec[token]:
                    result.append(opStack.pop())
                    opStack.push(token)
                else:
                    opStack.push(token)
            else:
                opStack.push(token)

    while not opStack.isEmpty():
        result.append(opStack.pop())

    print(result)
    return result

def post_fix_eval(expr):
    """
    후위 표현식으로 된 식을 계산
    :param expr:
    :return:
    """
    val_stack = ArrayStack()

    for token in expr:
        if isinstance(token, int):
            val_stack.push(token)
        elif token == '+':
            num1 = val_stack.pop()
            num2 = val_stack.pop()
            val_stack.push(num2+num1)
        elif token == '-':
            num1 = val_stack.pop()
            num2 = val_stack.pop()
            val_stack.push(num2-num1)
        elif token == '/':
            num1 = val_stack.pop()
            num2 = val_stack.pop()
            val_stack.push(num2/num1)
        elif token == '*':
            num1 = val_stack.pop()
            num2 = val_stack.pop()
            val_stack.push(num2*num1)

    return val_stack.pop()


print(post_fix_eval(infix_to_potfix(split_tokens("1*((1+2)*(3+4))"))))