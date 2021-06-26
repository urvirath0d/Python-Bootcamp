import re


def specified_char(string):
    charR = re.compile(r'[^a-zA-Z0-9.]')
    string = charR.search(string)
    return not bool(string)


print(specified_char("cbx30PwWX"))
print(specified_char("1*#kR"))
print(specified_char("P0w8"))


def text_search(text):
    patterns = 'ab'
    if re.search(patterns, text):
        return "Matched"
    else:
        return "Not Matched"


print(text_search("profound"))
print(text_search("absolutely"))


def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False


print(end_num('U06'))
print(end_num('urvi'))
print(end_num('Urvi610'))
results = re.finditer(r"([0-9]{1,3})", "Example number 20,35,46,57,100 is important")
print("Numbers of length 1 to 3")
for n in results:
    print(n.group(0))


def text_match(string):
    text = re.compile(r".*[A-Z]")
    if text.match(string):
        return True
    else:
        return False


print(text_match("Urvi"))
print(text_match("LALITKUMAR"))
print(text_match("rathod"))
