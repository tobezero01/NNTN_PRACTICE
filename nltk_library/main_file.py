import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk

# Đảm bảo đã tải các gói cần thiết (bỏ comment nếu chưa tải)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

def read_text_from_file(filename):
    """Đọc nội dung văn bản từ file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return ""

def tokenize_text(paragraph):
    sentences = sent_tokenize(paragraph)  # Tách câu
    words = word_tokenize(paragraph)      # Tách từ
    return sentences, words

def pos_tagging(paragraph):
    words = word_tokenize(paragraph)
    pos_tags = pos_tag(words)  # Gán nhãn từ loại
    return pos_tags

def named_entity_recognition(paragraph):
    words = word_tokenize(paragraph)
    pos_tags = pos_tag(words)
    named_entities = ne_chunk(pos_tags, binary=True)  # Nhận diện thực thể đơn giản
    return named_entities

def menu():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    print("\nChọn một trong các thuật toán sau:")
    print("1. Tokenization (Tách từ và câu)")
    print("2. POS Tagging (Gán nhãn từ loại)")
    print("3. Named Entity Recognition (Nhận diện thực thể)")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ")
    return choice

def main():
    filename = 'input_nltk'  # File chứa đoạn văn cần phân tích
    paragraph = read_text_from_file(filename)

    if not paragraph:
        print("Không thể đọc dữ liệu từ file. Kết thúc chương trình.")
        return

    while True:
        choice = menu()

        if choice == '1':
            sentences, words = tokenize_text(paragraph)
            print("\nKết quả Tokenization:")
            print("Sentences:", sentences)
            print("Words:", words)

        elif choice == '2':
            tags = pos_tagging(paragraph)
            print("\nKết quả POS Tagging:")
            print("POS Tags:", tags)

        elif choice == '3':
            entities = named_entity_recognition(paragraph)
            print("\nKết quả Named Entity Recognition:")
            print("Named Entities:", entities)

        elif choice == '4':
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

        # Hỏi người dùng có muốn tiếp tục hay không
        cont = input("\nBạn có muốn tiếp tục? (y/n): ").strip().lower()
        if cont != 'y':
            print("Đã thoát chương trình.")
            break

# Chạy chương trình
if __name__ == "__main__":
    main()
