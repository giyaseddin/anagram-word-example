def get_anagram_diff_report(a, b):
    a_hashmap = get_frequency_hashmap(a)
    b_hashmap = get_frequency_hashmap(b)

    chars_to_remove_from_a = get_char_difference(a_hashmap, b_hashmap)
    chars_to_remove_from_b = get_char_difference(b_hashmap, a_hashmap)

    return "remove {cnt_a} characters from '{a}' and {cnt_b} characters from '{b}'".format(
        a = a,
        cnt_a = chars_to_remove_from_a,
        b = b,
        cnt_b = chars_to_remove_from_b
    )


def get_char_difference(subject_hashmap, target_hashmap):
    chars_to_remove_from_subject = 0

    for char in subject_hashmap:
        if (char not in target_hashmap) or (subject_hashmap[char] > target_hashmap[char]):
            chars_to_remove_from_subject += 1

    return chars_to_remove_from_subject


def get_frequency_hashmap(s):
    hashmap = {}
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    return hashmap


def check_anagram(a, b):
    return a == b


def anagram_example_result(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if check_anagram(sorted_a, sorted_b):
        return "they are anagrams"
    else:
        return get_anagram_diff_report(a, b)


def main():
    a = input("a:")
    b = input("b:")

    print(anagram_example_result(a, b))


if __name__ == '__main__':
    main()
