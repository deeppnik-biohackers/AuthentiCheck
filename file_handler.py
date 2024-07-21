from PyPDF2 import PdfReader
from collections import Counter
import string
import re


def remove_punctuation_and_whitespace(text):
    # Remove characters like ellipsis
    text = re.sub(r'[\u2026\uFEFF\u200B]', ' ', text)
    # Replace punctuation with spaces
    text = re.sub(r'[' + re.escape(string.punctuation) + ']', ' ', text)
    # Remove extra whitespace characters
    return re.sub(r'\s+', ' ', text).strip()


def merge_hyphenated_words(text):
    # Merge hyphenated words that are split across lines
    return re.sub(r'(\w)-\n(\w)', r'\1\2', text)


def remove_numbers(text):
    # Replace superscript numbers and special Unicode characters with spaces
    return re.sub(r'(\w+)[\u00B2-\u00B9\u2070-\u209F]+', r'\1 ', text)


def preprocess_text(text):
    text = merge_hyphenated_words(text)
    text = remove_numbers(text)
    text = remove_punctuation_and_whitespace(text)
    return text


def analyze_text(text):
    words = text.split()
    total_word_count = len(words)
    word_length_count = Counter(len(word) for word in words)

    # Sort word lengths in ascending order
    sorted_word_length_count = sorted(word_length_count .items())

    return total_word_count, sorted_word_length_count


def calculate_word_length_percentages(length_counts, total_word_count):
    percentages = {}
    for length, count in length_counts:
        percentages[length] = round((count / total_word_count) * 100, 2)
    return percentages


def format_length_counts(length_counts):
    formatted_counts = []
    for length, count in length_counts:
        if length == 1:
            formatted_counts.append(f"{count} 1-letter word")
        else:
            formatted_counts.append(f"{count} {length}-letter words")
    return "\n".join(formatted_counts)


def open_file(file_path):
    """
    if file_path.endswith('.pdf'):
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ""

                for page in pdf_reader.pages:
                    text = page.extract_text()
                    text += text + " "

                processed_text = preprocess_text(text)
                total_word_count, word_length_count = analyze_text(processed_text)
                frequency = calculate_word_length_percentages(word_length_count, total_word_count)
                formatted_counts = format_length_counts(word_length_count)

                #print("Zawartość pliku PDF:")
                #print(text)
                return total_word_count, word_length_count, frequency, formatted_counts

        except Exception as e:
            print(f"Błąd: {e}")
    """
    if file_path.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                processed_text = preprocess_text(text)
                total_word_count, word_length_count = analyze_text(processed_text)
                frequency = calculate_word_length_percentages(word_length_count, total_word_count)
                formatted_counts = format_length_counts(word_length_count)

                #print("Zawartość pliku TXT:")
                #print(text)
                return total_word_count, word_length_count, frequency, formatted_counts
        except Exception as e:
            print(f"Błąd: {e}")

    else:
        print("Nieobsługiowany format. Wprowadź plik w formacie PDF lub TXT.")


# Example usage
"""
file_path = "D:\\sienkiewicz.txt"
result = open_file(file_path)

if result is not None:
    total_word_count, word_length_count, frequency, formatted_counts = result
    print("Total Word Count:", total_word_count)
    print("Word Length Counts:", word_length_count)
    print("Word Length Percentages:", frequency)
    print("Formatted Length Counts:\n", formatted_counts)
else:
    print("No result returned.")
"""