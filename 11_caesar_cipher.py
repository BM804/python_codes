"""Encrypt or decrypt ASCII letters with a Caesar shift."""
def transform(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    message = input("Text: ")
    shift = int(input("Shift (negative decrypts): "))
    print(transform(message, shift))
