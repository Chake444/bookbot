def count_words(file_contents):
    count = len(file_contents.split())
    return count

def count_characters(file_contents):
    characters = {}
    for char in file_contents.lower():
        if char in characters:
            characters[char] += 1
        if char not in characters:
            characters[char] = 1
    return characters


def sort_chars(characters):
    chars_list = []

    for char, count in characters.items():
        chars_list.append({"char" : char, "count" : count})

    chars_list.sort(reverse=True, key=lambda x: x["count"])

    return chars_list

