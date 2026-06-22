def first_non_repeating(s):
    for c in s:
        if s.lower().count(c.lower()) == 1:   #checks the number of times each character occurs in a string s and checks the condition if it occurs once
            return c
    return ""
