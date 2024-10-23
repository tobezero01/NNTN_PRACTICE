from collections import Counter, defaultdict

def read_sentence_from_file(filename):
    """Đọc câu từ file văn bản."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()  # Loại bỏ khoảng trắng thừa
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return ""

def generate_ngrams(words, n):
    """Tạo n-gram từ danh sách từ đã cho."""
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
    """Tính xác suất của cả câu dựa trên bi-gram."""
    total_probability = 1.0
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        total_probability *= bigram_probabilities.get(bigram, 0)  # Nếu không tồn tại, xác suất = 0
    return total_probability

# Đọc câu từ file
filename = 'input_gram'
sentence = read_sentence_from_file(filename)

if sentence:
    words = sentence.split()  # Chỉ gọi .split() một lần

    # Sinh và hiển thị các n-grams
    bigrams = generate_ngrams(words, 2)
    trigrams = generate_ngrams(words, 3)

    print("Bi-grams:")
    for bg in bigrams:
        print(bg)

    print("\nTri-grams:")
    for tg in trigrams:
        print(tg)

    # Tính xác suất bi-gram và tri-gram
    bigram_probabilities = calculate_ngram_probabilities(words, 2)
    trigram_probabilities = calculate_ngram_probabilities(words, 3)

    # Hiển thị xác suất bi-gram và tri-gram
    print("\nXác suất các bi-gram:")
    for bg, prob in bigram_probabilities.items():
        print(f"{bg}: {prob:.2f}")

    print("\nXác suất các tri-gram:")
    for tg, prob in trigram_probabilities.items():
        print(f"{tg}: {prob:.2f}")

    # Tính xác suất của cả câu
    sentence_probability = calculate_sentence_probability(words, bigram_probabilities)
    print(f"\nXác suất của cả câu: {sentence_probability:.6f}")
else:
    print("Không thể tính toán vì câu trống hoặc file không tồn tại.")
