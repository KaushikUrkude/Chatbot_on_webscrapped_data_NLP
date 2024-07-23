import re

def clean_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    clean_text = re.sub(r'[^\x00-\x7F]+', '', text)

    clean_text = clean_text.replace('�', '')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(clean_text)

    print(f"Non-printable and replacement characters removed from '{file_path}'.")

# Example usage:
file_path = 'cleaned_text.txt'
clean_text_file(file_path)
