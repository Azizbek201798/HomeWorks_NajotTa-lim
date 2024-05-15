# Task - 2 => CodeWars_Medium_2 Done by Azizbek;

# longest_substring("225424272163254474441338664823") ➞ "272163254"
# # substrings = 254, 272163254, 474, 41, 38, 23

# longest_substring("594127169973391692147228678476") ➞ "16921472"
# # substrings = 94127, 169, 16921472, 678, 476

# longest_substring("721449827599186159274227324466") ➞ "7214"
# # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# # 7214 and 9274 have same length, but 7214 occurs first.

# longest_substring("20") ➞ "2"

# longest_substring("") ➞ ""

def longest_substring(digits):
    longest = ''
    current = ''

    for digit in digits:
        if current == '':
            current += digit
        elif int(digit) % 2 != int(current[-1]) % 2:
            current += digit
        else:
            if len(current) > len(longest):
                longest = current
            current = digit

    if len(current) > len(longest):
        longest = current

    return longest