
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True
print("Các số nguyên tố nhỏ hơn 100:")
num = 0
while num < 100:
    if is_prime(num):
        print(num, end=" ")
    num += 1
print()
print("Các số chính phương nhỏ hơn 100:")
num = 0
while num < 100:
    if (int(num * 0.5)) * 2 == num:
        print(num, end=" ")
    num += 1
print()
print("Các số Fibonacci nhỏ hơn 1000:")
a, b = 0, 1
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
print()