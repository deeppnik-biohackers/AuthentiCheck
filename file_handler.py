from PyPDF2 import PdfReader

def open_file(file_path):
    if file_path.endswith('.pdf'):
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() if page.extract_text() else ""
                print("Zawartość pliku PDF:")
                print(text)
                return text
        except Exception as e:
            print(f"Błąd: {e}")
    elif file_path.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                print("Zawartość pliku TXT:")
                print(text)
                return text
        except Exception as e:
            print(f"Błąd: {e}")
    else:
        print("Nieobsługiowany format. Wprowadź plik w formacie PDF lub TXT.")
