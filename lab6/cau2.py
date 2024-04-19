def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    if num <= 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Hàm chính
def main():
    # Nhập mảng từ người dùng
    n = int(input("Nhập số lượng phần tử trong mảng: "))
    arr = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

    # Tìm số nguyên tố và số hoàn hảo trong mảng
    prime_numbers = [num for num in arr if is_prime(num)]
    perfect_numbers = [num for num in arr if is_perfect(num)]

    # In kết quả
    print("Các số nguyên tố trong mảng là:", prime_numbers)
    print("Các số hoàn hảo trong mảng là:", perfect_numbers)

# Gọi hàm chính
main()
