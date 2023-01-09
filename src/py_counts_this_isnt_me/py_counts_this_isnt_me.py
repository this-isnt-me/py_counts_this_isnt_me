# Import Packages/Modules
from collections import Counter
from string import punctuation

# Read in text file
def load_text(input_file):
    #Load in text file
    with open(input_file) as file:
        text = file.read()
    # Return text string from file
    return text

# Clean text
def clean_text(input_text):
    # Convert test to lowercase
    text = input_text.lower()
    # Remove punctuation
    for p in punctuation:
        text = text.replace(p, "")
    return text

# Count words in text_file
def count_words(input_file):
    # import text from file
    processed_text = load_text(input_file)
    # clean imported text
    processed_text = clean_text(processed_text)
    # Convert words string into list
    words_list = processed_text.split()
    # count words in list
    word_counts = Counter(words_list)
    # output word count
    print(word_counts)  
    
# count_words("zen.txt")