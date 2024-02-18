# -----------------------------Task 1------------------------------------

# def compare_files(file1, file2):
#     with open("your_full_path", 'r', encoding='utf-8') as file1:
#         lines_file1 = set(file1.readlines())

#     with open(f"your_full_path", 'r', encoding='utf-8') as file2:
#         lines_file2 = set(file2.readlines())

#     common_lines = lines_file1.intersection(lines_file2)
#     if common_lines:
#         print("Same rows:")
#         for line in common_lines:
#             print(line.strip())
#     else:
#         print("Files have different rows.")

#     unique_lines_file1 = lines_file1 - common_lines
#     if unique_lines_file1:
#         print("\nUnique rows in first file:")
#         for line in unique_lines_file1:
#             print(line.strip())

#     unique_lines_file2 = lines_file2 - common_lines
#     if unique_lines_file2:
#         print("\nUnique rows:")
#         for line in unique_lines_file2:
#             print(line.strip())


# compare_files('file1.txt', 'file2.txt')

# -----------------------------Task 2------------------------------------

# def calculate_statistics(input_file_path):
#     vowels = 'aeiouAEIOU'
#     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#     digits = '0123456789'

#     with open(input_file_path, 'r', encoding='utf-8') as input_file:
#         content = input_file.read()

#     num_characters = len(content)
#     num_lines = content.count('\n') + 1
#     num_vowels = sum(1 for char in content if char in vowels)
#     num_consonants = sum(1 for char in content if char in consonants)
#     num_digits = sum(1 for char in content if char in digits)

#     output_file_path = input_file_path.replace('.txt', '_statistics.txt')


#     with open(output_file_path, 'w', encoding='utf-8') as output_file:
#         output_file.write(f"Amount of symbols: {num_characters}\n")
#         output_file.write(f"Amount of rows: {num_lines}\n")
#         output_file.write(f"Amount of golosnuh letters: {num_vowels}\n")
#         output_file.write(f"Amount of prigoloshnuh letters: {num_consonants}\n")
#         output_file.write(f"Amount of digits: {num_digits}\n")

# input_file_path = 'your_file_path'

# calculate_statistics(input_file_path)

# -----------------------------Task 3------------------------------------

# def remove_last_line(input_file_path, output_file_path):
#     with open(input_file_path, 'r', encoding='utf-8') as input_file:
#         lines = input_file.readlines()

#     lines = lines[:-1]

#     with open(output_file_path, 'w', encoding='utf-8') as output_file:
#         output_file.writelines(lines)

# input_file_path = 'input.txt'
# output_file_path = 'output.txt'

# remove_last_line(input_file_path, output_file_path)

# -----------------------------Task 4------------------------------------

# def find_longest_line_length(file_path):

#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     longest_line_length = max(len(line.strip()) for line in lines)
#     return longest_line_length

# file_path = 'your_path'


# longest_line_length = find_longest_line_length(file_path)
# print(f"Longest row: {longest_line_length}")

# -----------------------------Task 5------------------------------------

# def count_word_occurrences(file_path, target_word):
#     word_count = 0

#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()

#         words = content.split()

#         for word in words:
#             if word == target_word:
#                 word_count += 1

#     return word_count

# file_path = 'Your_file_path'
# target_word = input("Enter word, wich you want to count ")

# occurrences = count_word_occurrences(file_path, target_word)
# print(f"Amount of '{target_word}' in file: {occurrences}")

# -----------------------------Task 5------------------------------------

# def replace_word_in_file(file_path, target_word, replacement_word):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()

#     replaced_content = content.replace(target_word, replacement_word)

#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(replaced_content)

# file_path = 'your_file_path'
# target_word = input("Enter word you want to replace: ")
# replacement_word = input("Enter word you want to replace it: ")

# replace_word_in_file(file_path, target_word, replacement_word)

# ---------------------------------END------------------------------------