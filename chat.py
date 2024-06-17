def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    second_operands = []
    operators = []
    results = []
    widths = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Each problem must contain two operands and one operator.'

        first_operand, operator, second_operand = parts

        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(first_operand), len(second_operand)) + 2
        widths.append(width)

        first_operands.append(first_operand.rjust(width))
        second_operands.append(operator + second_operand.rjust(width - 1))

        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))

        results.append(result.rjust(width))

    first_line = '    '.join(first_operands)
    second_line = '    '.join(second_operands)
    dash_line = '    '.join('-' * width for width in widths)

    if show_answers:
        result_line = '    '.join(results)
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}\n{result_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}"

    return arranged_problems


# Example usage
if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
