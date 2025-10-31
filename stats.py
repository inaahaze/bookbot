def get_num_words(text):
    words = text.split()
    return len(words)
def letter_counting(text):
    letters = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters
def key_helper(item):
    return item["num"]

def list_conversion(letters):
    list_of_dicts = []
    for k, v in letters.items():
        list_of_dicts.append({"char": k, "num": v})
    return list_of_dicts
        


# python
def dictionary_sorting(letters):
    lst = list_conversion(letters)      # build list of {"char","num"}
    lst.sort(key=key_helper, reverse=True)  # sorts in place, returns None
    return lst

