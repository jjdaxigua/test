from tasks import add
result = add.delay(4, 5)
print(result.ready())
print(result.get(timeout=1))
print(result.ready())