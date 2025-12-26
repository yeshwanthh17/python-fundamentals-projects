def main():
    text = "Python is fun. Python is powerful! Python is fun?"

    print("Total Characters:", total_characters(text))
    print("Total Words:", total_words(text))
    print("Total Sentences:", total_sentences(text))
    print("Character Frequency:", character_frequency(text))
    print("Word Frequency:", word_frequency(text))
    print("Most Frequent Word:", most_frequent_word(text))
    print("Least Frequent Word:", least_frequent_word(text))
    print("First Non-Repeating Character:", first_non_repeating_character(text))


def total_characters(text):
    count = 0
    for ch in text:
        count = count + 1
    return count


def total_words(text):
    words = text.split()
    count = 0
    for w in words:
        count = count + 1
    return count


def total_sentences(text):
    count = 0
    for ch in text:
        if ch == "." or ch == "!" or ch == "?":
            count = count + 1
    return count


def character_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq


def word_frequency(text):
    freq = {}
    text = text.lower()
    word = ""

    for ch in text:
        if ch.isalpha():
            word = word + ch
        else:
            if word != "":
                if word in freq:
                    freq[word] = freq[word] + 1
                else:
                    freq[word] = 1
                word = ""

    if word != "":
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    return freq


def most_frequent_word(text):
    freq = word_frequency(text)
    max_word = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            max_word = word

    return max_word


def least_frequent_word(text):
    freq = word_frequency(text)
    min_word = ""
    min_count = None

    for word in freq:
        if min_count is None or freq[word] < min_count:
            min_count = freq[word]
            min_word = word

    return min_word


def first_non_repeating_character(text):
    freq = character_frequency(text)

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


main()
