class Test():
    def __init__(self, attr=[]):
        self.attr = attr


a = Test()
b = Test()

a.attr.append(1)

print(a.attr)
print(b.attr)

# The reason my first snippet of code works is because, with immutable types, Python creates a new instance of it whenever you want one.
# If you needed to add 1 to 1, Python makes a new 2 for you, because the old 1 cannot be changed. The reason is mostly for hashing, I believe.

# https://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python
