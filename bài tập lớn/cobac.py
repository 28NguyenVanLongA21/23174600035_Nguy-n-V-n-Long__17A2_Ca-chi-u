import random
import csv

# 1. Tạo tập hợp các lá bài với xác suất xuất hiện
cards_prob = {
    'A': 0.1,
    'B': 0.1,
    'C': 0.1,
    'D': 0.1,
    'E': 0.1,
    'F': 0.1,
    'G': 0.1,
    'H': 0.1,
    'I': 0.1,
    'J': 0.1,
}

# Tạo danh sách các lá bài dựa trên xác suất xuất hiện
card_list = []
for card, prob in cards_prob.items():
    count = int(prob * 100)
    card_list.extend([card] * count)

# Lấy một nửa số lá bài và tạo thành các cặp
half_deck = card_list[:len(card_list)//2]
card_pairs = half_deck * 2
random.shuffle(card_pairs)

# 2. Mô phỏng trò chơi
board_size = len(card_pairs)
flipped_positions = set()
score = 0
results = []

# Hàm kiểm tra nếu hai lá bài giống nhau
def check_match(pos1, pos2):
    return card_pairs[pos1] == card_pairs[pos2]

# Vòng lặp lật các lá bài
while len(flipped_positions) < board_size:
    # Chọn ngẫu nhiên hai vị trí chưa lật
    pos1, pos2 = random.sample([i for i in range(board_size) if i not in flipped_positions], 2)
    
    # Kiểm tra nếu hai lá bài giống nhau
    is_match = check_match(pos1, pos2)
    if is_match:
        score += 1
        flipped_positions.add(pos1)
        flipped_positions.add(pos2)
    
    # Lưu kết quả vào danh sách
    results.append((pos1, card_pairs[pos1], cards_prob[card_pairs[pos1]], is_match))
    results.append((pos2, card_pairs[pos2], cards_prob[card_pairs[pos2]], is_match))

# 3. Tính toán xác suất tìm được cặp lá bài giống nhau
probability_of_finding_pair = score / (board_size // 2)

# 4. Lưu kết quả vào file CSV
csv_filename = 'card_game_results.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Vị trí lá bài', 'Mã lá bài', 'Xác suất xuất hiện', 'Tìm được cặp (True/False)'])
    for result in results:
        writer.writerow(result)

# 5. Hiển thị kết quả
print(f"Số điểm người chơi đạt được: {score}")
print(f"Xác suất tìm được cặp lá bài giống nhau: {probability_of_finding_pair:.2f}")
