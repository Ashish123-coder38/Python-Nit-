# Function to count word frequencies and write results
def word_frequency_counter(input_file, output_file):
    word_freq = {}  # Dictionary to store word frequencies
    
    # Step 1: Read the input file and process words
    with open(input_file, 'r') as file:
        for line in file:
            # Clean up the line: remove punctuation and convert to lowercase
            words = line.strip().lower().replace('.', '').split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # Step 2: Sort the words alphabetically
    sorted_word_freq = dict(sorted(word_freq.items()))
    
    # Step 3: Write the results to the output file
    with open(output_file, 'w') as file:
        for word, freq in sorted_word_freq.items():
            file.write(f"{word} : {freq}\n")

# Input and output file names
input_file = 'input.txt'
output_file = 'word_counts.txt'

# Create input.txt with sample data
sample_text = "Python is easy to learn. python is fun\n"
with open(input_file, 'w') as file:
    file.write(sample_text)

# Call the function to process the files
word_frequency_counter(input_file, output_file)

print(f"Word frequencies have been written to {output_file}")
