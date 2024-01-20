def is_balanced(expression):
    opening_brackets = []
    brackets = {')': '(', '}': '{', ']': '['}
#We iterate through each character in the expression.
    for char in expression:
        #If the character is an opening bracket, we push it onto the opening_brackets
        if char in '({[':
            opening_brackets.append(char)
            #If the character is a closing bracket, we check whether there is a corresponding opening bracket at the 
            # top of the opening_brackets. If not, or if the opening_brackets list is empty, the expression is unbalanced.
        elif char in ')}]':
            if not opening_brackets or opening_brackets.pop() != brackets[char]:
                return False

    # If the opening_brackets is empty, all brackets were balanced
    return not opening_brackets

# Test the function
expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1))
print(is_balanced(expression2))