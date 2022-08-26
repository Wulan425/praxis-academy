with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
# We can check that the file has been automatically closed.
(f.closed)

f.close()
print(f.read())