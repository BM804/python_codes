"""Convert Roman numerals to integers and integers to Roman numerals."""
VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"), (1, "I"),
]

def to_roman(number: int) -> str:
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    result = []
    for value, symbol in VALUES:
        count, number = divmod(number, value)
        result.append(symbol * count)
    return "".join(result)

def from_roman(numeral: str) -> int:
    if not numeral:
        raise ValueError("Roman numeral cannot be empty")
    total = index = 0
    for value, symbol in VALUES:
        while numeral.startswith(symbol, index):
            total += value
            index += len(symbol)
    if to_roman(total) != numeral:
        raise ValueError("Invalid Roman numeral")
    return total

if __name__ == "__main__":
    numeral = input("Roman numeral: ").strip().upper()
    print(from_roman(numeral))
