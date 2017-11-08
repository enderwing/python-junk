def add_values(values):
    while '0' in values:
        values.remove('0')

    new_values = []

    while len(values) > 1:
        if values[0] == values[1]:
            new_values.append(str(int(values[0])*2))
            values.pop(0)
            values.pop(0)
        else:
            new_values.append(values.pop(0))
    if len(values) == 1:
        new_values.append(values.pop())
    while len(new_values) < 4:
        new_values.append('0')

        return new_values

print(add_values([2,2,4,2]))
