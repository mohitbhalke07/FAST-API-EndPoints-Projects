def simple():
    print("start")
    yield 1
    print("end")


g = simple()
print(next(g))
# print(next(g))

