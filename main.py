def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    list_of_dictionaries = to_list_of_dict(chars_dict)
    report(list_of_dictionaries,book_path,num_words)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def to_list_of_dict(dictionary):
    list_of_dict = []
    for key in dictionary:
        if key.isalpha():
            list_of_dict.append({"char" : key, "count" : dictionary[key]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict


def sort_on(dict):
    return dict["count"]


def report(list_of_dictionaries, file_path, words_found):
    print(f"--- Begin report of {file_path} ---")
    print(f"{words_found} words found in the document")
    for i in range(0,len(list_of_dictionaries)):
        key = list_of_dictionaries[i]['char']
        value = list_of_dictionaries[i]['count']
        print(f"The '{key}' character was found {value} times")
    print('--- End report ---')



main()
