"""Question 47: Check whether brackets are balanced.

Given a string containing only (), [], and {}, decide whether every opening
bracket is closed by the right kind of bracket in the correct order.
"""


def is_balanced(text: str) -> bool:
    """Return True when all brackets in text are correctly paired.

    Runs in O(n) time and uses O(n) space for the stack.
    """
    opening_for = {")": "(", "]": "[", "}": "{"}
    stack = []

    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in opening_for:
            if not stack or stack.pop() != opening_for[character]:
                return False

    return not stack


if __name__ == "__main__":
    print(is_balanced("{[()]}"))  # True
    print(is_balanced("([)]"))    # False
