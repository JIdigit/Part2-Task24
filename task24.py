def polidrom():
    x=list(input())
    inverse_x=x[::-1]
    if x==inverse_x:
        return True
    return False
print(polidrom())