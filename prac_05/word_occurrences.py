"""
Word Occurrences
Estimate: 40 minutes
Actual: 45 minutes
"""


def main():
    """Program that counts the occurrences of words in a string."""
    # text = "This is a collection of words of nice words this is a fun thing it is"
    get_words = input("Text: ")
    count_words(get_words)


def count_words(text):
    """Converts words to lowercase and counts them."""
    word_to_count = {}
    words = text.split()
    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1
    calculate_longest_word(word_to_count)


def calculate_longest_word(word_to_count):
    """Calculates longest word for formatting."""
    longest_word = max(len(word) for word in word_to_count)
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{longest_word}} : {count}")


main()
