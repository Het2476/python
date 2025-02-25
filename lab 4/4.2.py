def mul(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter a num: "))
mul(num)