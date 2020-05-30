import random
def randInt(min=0 , max=200):
    if(max < min):
        min, max = max, min
    newmax = max-min
    num = round(random.random() * newmax + min )
    return num
print(randInt(0,-500))
print(randInt())