print("Hello")


def merofunction(a):
    print(a)

# print("CALLING THE MEROFUNCTION")
# merofunction(66)


def squarefuction(a):
    for i in range(0,10):
        print('THi is for loop count {}'.format(i))

        print(i*100)
    return a*a , a*2

# square_result , multiply_by_two = squarefuction(5)
print("Function called")
# print(square_result)
# print(multiply_by_two)

num = int(input("enter the number: "))

def multiply_by_two():
    print(num*2)

def add_by_two():
    print(num + 2)

def divide_by_two():
    print(num / 2)

condition = int(input("enter condition: "))
if condition == 1:

    multiply_by_two()
elif condition == 2:

    add_by_two()
elif condition == 3:
    divide_by_two()
else:
    print("Invalid Choice")



# 9868250580
# https://github.com/aaravcreator




