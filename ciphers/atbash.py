# Atbash mirrors the alphabet: A↔Z, B↔Y, a↔z
# A+Z = 155 a+z = 219
def atbash(text: str) -> str:
    result = ""
    for char in text:
        if 'a'<=char<='z':
            result += chr(219 - ord(char))
        elif 'A'<=char<='Z':
            result += chr(155 - ord(char))
        else:
            result += char
    return result
#test:
text = "HI"
print(atbash(text))


