def generate_squares(n):
    return[i**2 for i in range(1,n)]
for x in generate_squares(100):
    print(x)
#Keyword: yield
def generate_squares(n):
    for i in range(1,n):
        yield i**2
for i in generate_squares(100):
    print(i)
it=iter(generate_squares(10))
next(it)
def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
ir=iter(func())
next(ir)
print("hello")