import re

class Calculator:
    def calculate(self, s):
        """Takes in a string s, and returns a number."""
        result = 0
        current = 0
        sign = 1
        stack = []  # use the (LIFO)-Last in, First out
        
        for ss in s:
            if ss.isdigit():
                current = current * 10 + int(ss)
            elif ss in ["*", "/"]:
                print("This operation is not currently supported.")
                break
            elif ss in ["-", "+"]:
                result += sign * current
                current = 0
                if ss == "+":
                    sign = 1
                else:
                    sign = -1
            elif ss == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ss == ")":
                result += sign * current
                current = 0
                # Pop the sign and result from stack
                result *= stack.pop()  # sign before parentheses
                result += stack.pop()  # result before parentheses
        
        # Handle the final number
        result += sign * current
        return result

if __name__ == "__main__":
    print("Launching the calculator....")
    calc = Calculator()
    user_input = ""
    while user_input not in ["exit", "quit", "stop", "close"]:
        user_input = input("> ")
        if user_input not in ["exit", "quit", "stop", "close"]:
            regex = re.search("[a-zA-Z]", user_input)
            if regex != None:
                print("Please write a mathematical expression.")
            else:
                try:
                    output = calc.calculate(user_input)
                    print(output)
                except Exception as e:
                    print(f"Error: {e}")
    print("Closing the calculator...")
