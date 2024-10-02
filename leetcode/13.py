s = "DCXXI"

roman_dict = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}
order=["M", "D", "C", "L", "X", "V", "I"]

count = 0
i = 0
while i<len(s):
    if i+2<len(s) and s[i] == s[i+1] and s[i] == s[i+2]:
        count += roman_dict[s[i]]*3
        i += 3
    elif i+1<len(s) and s[i] == s[i+1]:
        count += roman_dict[s[i]]*2
        i += 2
    elif i+1<len(s) and order.index(s[i]) > order.index(s[i+1]):
        count += roman_dict[s[i+1]] - roman_dict[s[i]]
        i += 2
    else:
        count += roman_dict[s[i]]
        i += 1
print(count)