# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])

def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''
    
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
