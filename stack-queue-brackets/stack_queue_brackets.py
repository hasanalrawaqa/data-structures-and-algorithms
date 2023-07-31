def validate_brackets(string):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in brackets.keys():  # Opening bracket
            stack.append(char)
        elif char in brackets.values():  # Closing bracket
            if not stack:  # No opening bracket to match
                return False
            opening_bracket = stack.pop()
            if brackets[opening_bracket] != char:  # Mismatched brackets
                return False

    return len(stack) == 0  # True if all brackets are matched and stack is empty

if __name__ == "__main__":
    print(validate_brackets("{}"))  # True
    print(validate_brackets("{}(){}"))  # True
    print(validate_brackets("()[[Extra Characters]]"))  # True
    print(validate_brackets("(){}[[]]"))  # True
    print(validate_brackets("{}{Code}[Fellows](())"))  # True
    print(validate_brackets("[({}]"))  # False
    print(validate_brackets("(]("))  # False
    print(validate_brackets("{(})"))  # False
