from collections import Counter, defaultdict
import re

def read_text_from_file(filename):
    """Đọc nội dung từ file văn bản."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()  # Loại bỏ khoảng trắng thừa
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return ""

def split_sentences(text):
    """Tách đoạn văn thành các câu dựa trên dấu chấm câu."""
    sentences = re.split(r'[.!?]\s*', text.strip())
    return [sentence for sentence in sentences if sentence]  # Loại bỏ câu trống

def normalize_text(text):
    """Chuẩn hóa văn bản thành chữ thường."""
    return text.lower()

def generate_ngrams(words, n):
    """Tạo n-grams từ danh sách từ."""
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]

def calculate_ngram_probabilities(words, n):
    """Tính xác suất của các n-grams."""
    ngrams = generate_ngrams(words, n)
    prefix_counts = Counter(generate_ngrams(words, n - 1))
    ngram_counts = Counter(ngrams)

    probabilities = defaultdict(float)
    for ngram, count in ngram_counts.items():
        prefix = ngram[:-1]  # Lấy tiền tố của n-gram
        probabilities[ngram] = count / prefix_counts[prefix]

    return probabilities

def calculate_sentence_probability(words, bigram_probabilities):
    """Tính xác suất của cả câu dựa trên bi-grams."""
    total_probability = 1.0
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        total_probability *= bigram_probabilities.get(bigram, 0)  # Nếu không tồn tại, xác suất = 0
    return total_probability

def show_menu():
    """Hiển thị menu và lấy lựa chọn của người dùng."""
    print("\nMenu:")
    print("1. Chọn câu khác")
    print("2. Dừng chương trình")
    choice = input("Nhập lựa chọn của bạn (1 hoặc 2): ").strip()
    return choice

# Đọc đoạn văn từ file
filename = 'input_gram'
text = read_text_from_file(filename)

if text:
    # Chuẩn hóa đoạn văn thành chữ thường
    normalized_text = normalize_text(text)

    # Tách đoạn thành danh sách các câu
    sentences = split_sentences(normalized_text)

    # Tính bi-grams cho toàn bộ đoạn văn
    all_words = normalized_text.split()
    bigram_probabilities_text = calculate_ngram_probabilities(all_words, 2)

    while True:
        # Hiển thị các câu và cho phép người dùng chọn
        print("\nCác câu trong đoạn văn:")
        for i, sentence in enumerate(sentences):
            print(f"{i + 1}: {sentence}")

        try:
            # Nhập chỉ số câu từ người dùng
            choice = int(input("Chọn số thứ tự câu bạn muốn tính (ví dụ: 1, 2,...): ")) - 1
            if choice < 0 or choice >= len(sentences):
                raise ValueError("Chỉ số câu không hợp lệ.")

            chosen_sentence = sentences[choice]
            print(f"\nCâu được chọn: {chosen_sentence}")

            # Tách câu đã chọn thành danh sách từ
            chosen_words = chosen_sentence.split()

            # Tính bi-gram và tri-gram cho câu đã chọn
            bigram_probabilities_sentence = calculate_ngram_probabilities(chosen_words, 2)
            trigram_probabilities_sentence = calculate_ngram_probabilities(chosen_words, 3)

            # Tính xác suất của câu đã chọn dựa trên bi-grams của toàn đoạn
            sentence_probability = calculate_sentence_probability(
                chosen_words, bigram_probabilities_text
            )

            # Hiển thị kết quả
            print("\nBi-grams của câu đã chọn:")
            for bg, prob in bigram_probabilities_sentence.items():
                print(f"{bg}: {prob:.2f}")

            print("\nTri-grams của câu đã chọn:")
            for tg, prob in trigram_probabilities_sentence.items():
                print(f"{tg}: {prob:.2f}")

            print(f"\nXác suất của câu '{chosen_sentence}' so với cả đoạn: {sentence_probability:.6f}")

        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập một số hợp lệ.")

        # Hiển thị menu và kiểm tra lựa chọn của người dùng
        menu_choice = show_menu()
        if menu_choice == '2':
            print("\nChương trình đã kết thúc.")
            break
else:
    print("Không thể đọc đoạn văn vì file không tồn tại hoặc rỗng.")
