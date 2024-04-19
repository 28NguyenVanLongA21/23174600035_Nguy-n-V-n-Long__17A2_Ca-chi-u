def input_square_matrix(n):
    matrix = []
    print("Nhập các phần tử của ma trận vuông:")
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Nhập phần tử [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

def matrix_inverse(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        print("Ma trận không có ma trận nghịch đảo.")
        return
    inverse = [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
               [-matrix[1][0] / determinant, matrix[0][0] / determinant]]
    print("Ma trận nghịch đảo của ma trận đã nhập là:")
    print_matrix(inverse)

def main():
    n = int(input("Nhập kích thước của ma trận vuông: "))
    
    # Nhập ma trận vuông
    matrix = input_square_matrix(n)
    
    # Kiểm tra xem ma trận đã cho có phải là ma trận đối xứng hay không
    if is_symmetric(matrix):
        print("Ma trận đã nhập là ma trận đối xứng.")
    else:
        print("Ma trận đã nhập không phải là ma trận đối xứng.")
    
    # Tìm ma trận nghịch đảo (nếu có)
    matrix_inverse(matrix)
main()