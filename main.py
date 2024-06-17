def calc_result(f_problems, r_problems):
    line = []
    lines_list = f_problems.split('\n')
    underline = lines_list[2].split(" " * 4)
    for u, problem in zip(underline, r_problems):
        prob_list = problem.split(' ')
        if prob_list[1] == '+':
            result = int(prob_list[0]) + int(prob_list[2])
        else:
            result = int(prob_list[0]) - int(prob_list[2])
        if line:
            line.append(" " * 4)
        line.append(" " * (len(u) - len(str(result))) + str(result))
    return f_problems + "\n" + "".join(line)


def formatter(problems):
    lines_to_print = []
    line = []
    number_of_spaces = 0
    max_len = []
    for idx, problem in enumerate(problems):
        problem_list = problem.split(' ')
        len1 = len(problem_list[0])
        len2 = len(problem_list[2])
        if len1 >= len2 and line:
            number_of_spaces = 6
        elif len1 < len2 and line:
            number_of_spaces = 6 + len2 - len1
        else:
            if len2 > len1:
                number_of_spaces = 2 + len2 - len1
            else:
                number_of_spaces = 2
        line.append(" " * number_of_spaces)
        line.append(problem_list[0])
        max_len.append(max(len1, len2))
    lines_to_print.append("".join(line.copy()) + "\n")
    line = []
    for idx, problem in enumerate(problems):
        problem_list = problem.split(' ')
        if line:
            line.append(" " * 4)
        line.append(problem_list[1] + " " * (1 + max_len[idx] - len(problem_list[2])))
        line.append(problem_list[2])
    lines_to_print.append("".join(line.copy()) + "\n")
    line = []
    for m in max_len:
        if line:
            line.append(" " * 4)
        line.append(("-" * (m + 2)))
    lines_to_print.append("".join(line.copy()))
    return "".join(lines_to_print)


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        problem_list = problem.split(' ')
        if not (problem_list[0] + problem_list[2]).isdigit():
            return 'Error: Numbers must only contain digits.'
        elif problem_list[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        elif any(len(ele) > 4 for ele in problem_list[::2]):
            return 'Error: Numbers cannot be more than four digits.'
    formatted = formatter(problems)
    if not show_answers:
        return formatted
    else:
        return calc_result(formatted, problems)


if __name__ == '__main__':
    print(arithmetic_arranger(problems=["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], show_answers=True))
