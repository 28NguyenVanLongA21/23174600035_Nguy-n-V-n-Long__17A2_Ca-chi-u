def input_matrix(m, n):
    matrix = []
    print("Nhập các phần tử của ma trận:")
    for i in range(m):
        row = []
        for j in range(n):
            element = float(input(f"Nhập phần tử [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    print("Ma trận:")
    for row in matrix:
        print(row)

def sum_matrix(matrix):
    total = sum(sum(row) for row in matrix)
    print("Tổng của các phần tử trong ma trận là:", total)

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Không thể nhân hai ma trận với kích thước này.")
        return
    result = [[sum(a*b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    print("Kết quả của phép nhân hai ma trận là:")
    print_matrix(result)

def transpose_matrix(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Ma trận chuyển vị của ma trận ban đầu là:")
    print_matrix(result)

def main():
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    # Nhập ma trận
    matrix1 = input_matrix(m, n)

    # Tính tổng của ma trận
    sum_matrix(matrix1)

    # Nhập ma trận thứ hai để tính tích (nếu cần)
    choice = input("Bạn có muốn nhập ma trận thứ hai để tính tích không? (y/n): ")
    if choice.lower() == 'y':
        p = int(input("Nhập số hàng của ma trận thứ hai: "))
        q = int(input("Nhập số cột của ma trận thứ hai: "))
        matrix2 = input_matrix(p, q)
        multiply_matrices(matrix1, matrix2)

    # Tạo và in ra ma trận chuyển vị của ma trận ban đầu
    transpose_matrix(matrix1)
main()