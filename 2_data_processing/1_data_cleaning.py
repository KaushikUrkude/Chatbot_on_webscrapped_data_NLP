import re
from tqdm import tqdm

#Removes Headings and serial numbers
def remove_extra_newlines(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Replace multiple newlines with a single newline
    cleaned_content = '\n'.join(line for line in content.splitlines() if line.strip())
    
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(cleaned_content)

# Example usage
file_path = 'combined_text.txt'
remove_extra_newlines(file_path)


def remove_short_and_numbered_lines(input_file, output_file, min_word_count=8, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as infile, open(output_file, 'w', encoding=encoding) as outfile:
        for line in tqdm(infile):
            words = line.split()
            # Check if the line has at least `min_word_count` words and doesn't start with a number
            if len(words) >= min_word_count and not re.match(r'^\d', line.strip()):
                outfile.write(line)

# Example usage
input_file = 'combined_text.txt'
output_file = 'cleaned_text.txt'
remove_short_and_numbered_lines(input_file, output_file)