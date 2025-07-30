def get_num_words(text):
    return len( text.split() )

def get_unique_char_list(text):
    return list(set(list(text)))

def get_char_dictionary(text):
    text = text.lower()
    unique_chars = get_unique_char_list(text)
    char_dict = {}
    for char in unique_chars:
        num_char = text.count(char)
        char_dict[char] = num_char
    return char_dict

def sort_on_num(items):
    return items["num"]

def get_sorted_list(dict):
    new_list = []
    for d in dict:
        new_list.append( {
            "char": d,
            "num": dict[d]
        } )
    new_list.sort(reverse=True, key=sort_on_num)
    return new_list

