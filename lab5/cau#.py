def find_word_positions(text, word):
    positions = [i for i in range(len(text)) if text.startswith(word, i)]
    return positions

text = input("Nhập chuỗi văn bản: ")
word_to_find = input("Nhập từ cần tìm kiếm: ")

positions = find_word_positions(text, word_to_find)
if positions:
    print(f"Vị trí (index) của từ '{word_to_find}' trong chuỗi là:", positions)
else:
    print(f"Từ '{word_to_find}' không xuất hiện trong chuỗi.")

word_counts = text.split().count
most_frequent_word = max(set(text.split()), key=word_counts)
print("Từ xuất hiện nhiều nhất trong chuỗi là:", most_frequent_word)
