def is_arithmetic_sequence(numbers):
    return all(numbers[i + 1] - numbers[i] == numbers[1] - numbers[0] for i in range(len(numbers) - 1))

def main():
    numbers = [int(num) for num in input("Nhập dãy số, cách nhau bằng dấu cách: ").split()]
    print("Dãy số", numbers, "là một cấp số cộng." if is_arithmetic_sequence(numbers) else "Dãy số", numbers, "không tạo thành một cấp số cộng.")

main()
