import json

def load_dictionary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}
def search_word(word, dictionary):
    meanings = dictionary.get(word)
    return meanings
def main():
    dictionary_file_path = './data.json'
    english_dictionary = load_dictionary(dictionary_file_path)
    if not english_dictionary:
        print(f"Error: Unable to load data from {dictionary_file_path}")
        return
    word = input("Enter a word: ")
    meanings = search_word(word, english_dictionary)
    if meanings:
        print(f"Meanings of '{word}': {meanings}")
    else:
        print(f"The word '{word}' is not in the data file.")
if __name__ == "__main__":
    main()
