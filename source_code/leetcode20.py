def isValid(s):
    stack=list()
    flag=True
    brackets={'(':')','[':']','{':'}'}
    for ch in s:
        if ch in brackets:
            stack.append(brackets[ch])
        else:
            if not stack:
                flag=False
                break
            temp=stack.pop()
            if ch != temp:
                flag=False
                break
    if stack:
        flag=False
    return flag
