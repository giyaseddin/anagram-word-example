def format_anagram_diff_report(a, b):
    return "They are not anagram"


def check_anagram(a, b):
    return a == b


def anagram_example_result(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if check_anagram(sorted_a, sorted_b):
        return "they are anagrams"
    else:
        return format_anagram_diff_report(sorted_a, sorted_b)


def main():
    a = input("a:")
    b = input("b:")

    print(anagram_example_result(a, b))


if __name__ == '__main__':
    main()
