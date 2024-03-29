import json
from difflib import get_close_matches
def load_dictionary(file_path):
    with open('data.json') as file:
        data = json.load(file)
    return data
def get_definition(dictionary, word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        suggestions = get_close_matches(word, dictionary.keys(), n=3, cutoff=0.7)
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found in the dictionary."

def main():
    file_path = 'dictionary.json'  
    dictionary = load_dictionary(file_path)
    while True:
        user_input = input("Enter a word to get its definition (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        definition = get_definition(dictionary, user_input)
        print(definition)
if __name__ == "__main__":
    main()
