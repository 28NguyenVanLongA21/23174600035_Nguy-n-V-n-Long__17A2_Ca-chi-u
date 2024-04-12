def shortest_common_substring(str1, str2):
    common_substring = ""
    min_length = min(len(str1), len(str2))
    
    for i in range(min_length):
        if str1[i] == str2[i]:
            common_substring += str1[i]
        else:
            break
    
    return common_substring

str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

common_substring = shortest_common_substring(str1, str2)

if len(common_substring) == 0:
    print("Không có chuỗi ký tự con chung.")
else:
    print("Chuỗi ký tự con chung ngắn nhất là:", common_substring)