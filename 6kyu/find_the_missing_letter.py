def find_missing_letter(chars):
    ascii_vals = [ord(char) for char in chars]
    for i in range(len(ascii_vals)):
        if ascii_vals[i] + 1 != ascii_vals[i+1]:
            return chr(ascii_vals[i]+1)