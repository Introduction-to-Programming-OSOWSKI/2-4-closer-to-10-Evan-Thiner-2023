#WRITE YOUR CODE IN THIS FILE
def close10(x,y):
    if x-y>0:
        return x
    elif y-x>0:
        return y
    else:
        return 0
print(close10(5,13))