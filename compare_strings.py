def difference_score(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if 'remix' in str1 and 'remix' not in str2:
        return float('inf')

    chars = {}
    for char in str1:
        chars[char] = chars.get(char, 0) + 1

    for char in str2:
        chars[char] = chars.get(char, 0) - 1

    score = 0
    for count in chars.values():
        score += abs(count)
 
    return score