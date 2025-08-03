guestlist = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David", "Alice"]

seen = set()
duplicates = set()

for name in guestlist:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

print("Unique guest names:")
for name in seen:
    print(name)

print("Duplicate guest names:")
for name in duplicates:
    print(name)