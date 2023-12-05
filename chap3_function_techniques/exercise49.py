def double_values(values):
    values = values.copy()
    for idx, value in enumerate(values):
        values[idx] = 2 * value
    return values


data = [1, 2, 3]
data_doubled = double_values(data)

print(f"{data = }")
print(f"{data_doubled = }")