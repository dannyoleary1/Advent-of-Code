def get_resulting_frequency(file_path):
    """The function will read in the input from the supplied text file, and add them to the already existing value.
    For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3."""

    current_frequency = 0

    #Step 2. Read the input and add/subtract.
    with open(file_path) as f:
        for line in f:
            current_frequency += check_operand(line)

    return current_frequency

def check_operand(current_op):
    if current_op[0] is '+':
        return int(current_op[1:])
    else:
        return int(current_op[1:]) * -1

print(get_resulting_frequency("input.txt"))