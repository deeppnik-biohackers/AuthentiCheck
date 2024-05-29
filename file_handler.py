from PyPDF2 import PdfReader
from collections import Counter
import string
import re


def remove_punctuation(text):
    remover = str.maketrans("", "", string.punctuation)
    return text.translate(remover)


def merge_hyphenated_words(text):
    return re.sub(r'(\w)-\n(\w)', r'\1\2', text)


def preprocess_text(text):
    text = text.lower()
    text = merge_hyphenated_words(text)
    text = remove_punctuation(text)
    return text


def open_file(file_path):
    if file_path.endswith('.pdf'):
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ""
                total_counter = Counter()

                for page in pdf_reader.pages:
                    text = page.extract_text()
                    text += text + " "
                    processed_text = preprocess_text(text)
                    page_counter = Counter(processed_text.split())
                    total_counter.update(page_counter)

                print("Zawartość pliku PDF:")
                print(text)
                return text, total_counter

        except Exception as e:
            print(f"Błąd: {e}")

    elif file_path.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                total_counter = Counter()
                total_counter.update(text.split())

                print("Zawartość pliku TXT:")
                print(text)
                return text, total_counter
        except Exception as e:
            print(f"Błąd: {e}")

    else:
        print("Nieobsługiowany format. Wprowadź plik w formacie PDF lub TXT.")
