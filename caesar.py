from banner import ascii
def processing(char, shift, method):
    result = ""
    if char.islower() and method == "encrypt":
        result += chr((ord(char) + shift - 97) % 26 + 97)
    elif char.islower() and method == "decrypt":
        result += chr((ord(char) - shift - 97) % 26 + 97)
    elif char.isupper() and method == "encrypt":
        result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.isupper() and method == "decrypt":
        result += chr((ord(char) - shift - 65) % 26 + 65)
    elif ord(char) == 32:
        result += chr(32)
    return result
if __name__ == '__main__':
    result = ""
    ascii()
    plain_text = str(input("encrypted or plain text: "))
    shift = int(input("shift: "))
    print("1. Encrypt\n2. Decrypt")
    method = int(input("method: "))
    for char in plain_text:
        method_process = {
            "1": processing(char, shift, "encrypt"),
            "2": processing(char, shift, "decrypt")
        }
        for key in method_process:
            if method == int(key):
                result += method_process[key]
    print("Result: {}".format(result))
    