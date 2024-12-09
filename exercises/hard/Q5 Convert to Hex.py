# Convert to Hex
# Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.

def convert_to_hex(txt):
    #txt = txt.lower()
    hex_val = ""
    for l in txt:
        val = hex(ord(l))
        val = val.replace("x","")
        idx = val.find("0")
        if idx != -1:
            val = val[:idx] + val[idx+1:]

        if hex_val == "":
            hex_val += val
        else:
            hex_val += " " + val
    return hex_val