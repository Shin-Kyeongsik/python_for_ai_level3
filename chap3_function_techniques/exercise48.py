def double_values(values):
    for key, value in values.items():
        values[key] = 2 * value
    return values


data = {'a': 10, 'b': 20, 'c': 30}
data_doubled = double_values(data)

print(f"{data = }")
print(f"{data_doubled = }")