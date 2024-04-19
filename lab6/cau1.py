def main():
    # Nhập mảng từ người dùng
    n = int(input("Nhập số lượng phần tử trong mảng: "))
    arr = []
    for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(num)

    # Tính tổng số chẵn và số lẻ
    sum_even = sum(num for num in arr if num % 2 == 0)
    sum_odd = sum(num for num in arr if num % 2 != 0)

    # Xuất kết quả
    print("Tổng các số chẵn trong mảng là:", sum_even)
    print("Tổng các số lẻ trong mảng là:", sum_odd)

main()  # Gọi hàm main()
