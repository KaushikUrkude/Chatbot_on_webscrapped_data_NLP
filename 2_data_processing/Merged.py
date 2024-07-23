import os
from tqdm import tqdm

def combine_text_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8', errors='ignore') as outfile:
        for filename in tqdm(os.listdir(input_folder)):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write("\n")  # Add a newline to separate files
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

input_folder = 'extracted_text'  # Replace with the path to your text files
output_file = 'combined_text.txt'  # Name of the output file

combine_text_files(input_folder, output_file)
print(f"All text files have been combined into {output_file}")
