from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from underthesea import sent_tokenize

# Văn bản tiếng Việt mẫu
text = """
Trí tuệ nhân tạo đang trở thành một trong những công nghệ quan trọng nhất trong thời đại 4.0.
Các ứng dụng của AI xuất hiện trong hầu hết các lĩnh vực, từ y tế, giáo dục, đến tài chính và vận tải.
AI giúp tăng cường năng suất lao động, tự động hóa nhiều quy trình và hỗ trợ ra quyết định nhanh chóng.
Tuy nhiên, sự phát triển của AI cũng đặt ra nhiều thách thức, đặc biệt là về mặt đạo đức và an toàn dữ liệu.
"""

# Sử dụng underthesea để chia câu
sentences = sent_tokenize(text)
preprocessed_text = "\n".join(sentences)

# Khởi tạo parser với văn bản đã chia câu
parser = PlaintextParser.from_string(preprocessed_text, None)

# Số câu cần tóm tắt
summary_sentences = 2

def summarize_with(summarizer, parser, sentences):
    summarizer_instance = summarizer()
    summary = summarizer_instance(parser.document, sentences)
    return " ".join(str(sentence) for sentence in summary)

# 1. LexRank
print("LexRank Summary:")
print(summarize_with(LexRankSummarizer, parser, summary_sentences))

# 2. TextRank
print("\nTextRank Summary:")
print(summarize_with(TextRankSummarizer, parser, summary_sentences))

# 3. LSA
print("\nLSA Summary:")
print(summarize_with(LsaSummarizer, parser, summary_sentences))

# 4. KL-Sum
print("\nKL-Sum Summary:")
print(summarize_with(KLSummarizer, parser, summary_sentences))

# 5. Luhn
print("\nLuhn Summary:")
print(summarize_with(LuhnSummarizer, parser, summary_sentences))
