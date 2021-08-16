# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(s):
    if s == "":
        return ""
    else:
        li = []
        temp = ""

        for i in range(len(s)):
            if s[i]!= "-" and s[i]!= "_":
                temp += s[i]
            else:
                li.append(temp)
                temp = ""

        if temp != "":
            li.append(temp)
        ans = li[0]
        for i in li[1:]:
            ans += i.capitalize()
        return ans
