# A~Z: 65~90
# a~z: 97~122

def caesar(shift:int, text:str) -> str:
    after = ""
    for char in text:
        if not 65<=ord(char)<=90 and not 97<=ord(char)<=122:
            after += char
            continue
        else:
            base = 65 if char.isupper() else 97
            identity = ord(char) - base
            final_shift = (identity + shift) % 26
            char = chr(base+final_shift)
            after += char
    return after


# test
# t = caesar(3 , "Hello!")
# print(t)
