from collections import deque

mystr="We will conquere COVID-19"
stack=deque()
for c in mystr:
    stack.append(c)
newstr=""
for _ in mystr:
    newstr += stack.pop()
print(newstr)    

def is_balanced(txt):
    stack=deque()
    result=True
    for c in txt:
        if c in "[{(":
            stack.append(c)
        elif c == ')':
            if len(stack)==0: return False
            result = result and (stack.pop()=='(')
        elif c == ']':
            if len(stack)==0: return False
            result = result and (stack.pop()=='[')
        elif c == '}':
            if len(stack)==0: return False
            result = result and (stack.pop()=='{')
    return result 

print(is_balanced("({a+b})"))            
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))