# what will be the output for the following

def f(x, l = []):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3, [3,2,1])
f(3)

# output:
# [0,1]
# [3,2,1,0,1,4]
# [0,1,0,1,4]
# Because, the third time the function is called,
# it uses the list from the list from the first function call.
