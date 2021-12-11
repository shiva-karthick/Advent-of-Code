d = {"a": 1, "b": 2}
# Append the values from *map to list
m = map(d.get, ["a", "b", "a", "b", "b"])
print(list(m))

