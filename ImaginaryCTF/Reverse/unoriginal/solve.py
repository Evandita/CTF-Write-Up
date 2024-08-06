result = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"
input = ""

for char in result:
    input += chr(ord(char) ^ 5)

print(input)