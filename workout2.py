a = [10, 20, 30, 40, 50]

print(a)
print(type(a))
print(len(a))

print("Indexing methods")
print(a[2])
a[1]=15
print(a)
print(a[-1])
print(a[-3])

print("Append function")
a.append(60)
print(a)

print("Insert function")
a.insert(4,70)
print(a)

print("Remove function")
a.remove(50)
print(a)

print("Pop function")
a.pop()
print(a)
a.pop(2)
print(a)

print("Delete function")
del a[2]
print(a)

print("Clear function")
a.clear()
print(a)
