# 수식의 괄호가 올바르게 열리고 닫혔는지 확인.
from stack import ArrayStack

def is_brackets(expr):
    match = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    S = ArrayStack()

    for c in expr:
        if c in '({[':
            S.push(c)
        else:
            if S.isEmpty():
                return False
            else:
                bracket = S.pop()
                if bracket != match[c]:
                    return False

    return S.isEmpty() # 스택이 비어있지 않으면 괄호가 안맞음.

print(is_brackets('()()()(){]}{{}}'))
print(is_brackets('(){}{}[]{}[]'))