def is_isogram(string):
    dic = {}
    string = string.lower()
    string = "".join(filter(str.isalpha, string))
    for letter in string:
        if letter in dic:
            dic[letter] = dic[letter] + 1
        else:
            dic[letter] = 1
    x = list(dic.values())
    for element in x[1:]:
        if x[0] != element:
            return False
    return True
