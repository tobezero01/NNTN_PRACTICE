import sumy

import nltk
nltk.download("punkt_tab")

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

def read_sentence_from_file(filename):
    """Đọc câu từ file văn bản."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()  # Loại bỏ khoảng trắng thừa
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return ""




filename = 'text'
text = read_sentence_from_file(filename)
# Khởi tạo parser và tokenizer với ngôn ngữ 'english'
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# LEX_RANK
# Tạo summarizer sử dụng LexRank
summarizerLEX = LexRankSummarizer()

# Tóm tắt văn bản (lấy 2 câu)
summaryLEX = summarizerLEX(parser.document, 2)

# In ra các câu tóm tắt
print("LEX_RANK : ")
for sentence in summaryLEX:
    print(sentence)

print()

# TEXT RANK
summarizerTEXT = TextRankSummarizer()

summaryTEXT = summarizerTEXT(parser.document, 2)
print("TEXT_RANK : ")
for sentence in summaryTEXT:
    print(sentence)

print()



#LSA (Latent Semantic Analysis)
summarizerLSA = LsaSummarizer()
summaryLSA = summarizerLSA(parser.document, 2)
print("LSA (Latent Semantic Analysis)")
for sentence in summaryLSA:
    print(sentence)

print()


#KL-Sum (Kullback-Leibler Divergence)
summarizerKL = KLSummarizer()
summaryKL = summarizerKL(parser.document, 2)
print("KL-Sum (Kullback-Leibler Divergence)")
for sentence in summaryKL:
    print(sentence)

print()


#Luhn
summarizerLuhn = LuhnSummarizer()
summaryLuhn = summarizerLuhn(parser.document, 2)
print("Luhn")
for sentence in summaryLuhn:
    print(sentence)
