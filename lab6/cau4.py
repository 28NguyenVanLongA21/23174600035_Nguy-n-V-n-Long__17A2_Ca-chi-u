def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# a) Tạo danh sách n số Fibonacci đầu tiên
def fibonacci_sequence(n):
    fibonacci = [0, 1]
    [fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, n)]
    return fibonacci[:n]

# b) Tạo danh sách các số nguyên tố nhỏ hơn 100
def prime_numbers_less_than_100():
    return [num for num in range(2, 100) if is_prime(num)]

def main():
    n = int(input("Nhập số Fibonacci cần tạo: "))
    fibonacci_list = fibonacci_sequence(n)
    print("Danh sách Fibonacci:", fibonacci_list)

    prime_list = prime_numbers_less_than_100()
    print("Danh sách số nguyên tố nhỏ hơn 100:", prime_list)

main()
