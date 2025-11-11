names = ['Linus', 'Stefan', 'Mari',]

print(f"{names[0]} I welcome you to dinner.")
print(f"{names[1]} I welcome you to dinner.")
print(f"{names[2]} I welcome you to dinner.")
print(f"{names[2]} Cannot make it.")

names[2] = 'Sebbe'

print(f"{names[0]} I welcome you to dinner.")
print(f"{names[1]} I welcome you to dinner.")
print(f"{names[2]} I welcome you to dinner.")
print(f"I found a bigger dinner table so more space is available.")

names.insert(0, 'Hannes')
names.insert(3, 'Alle')
names.append('Ante')
print(names)

print(f"{names[0]} I welcome you to dinner.")
print(f"{names[1]} I welcome you to dinner.")
print(f"{names[2]} I welcome you to dinner.")
print(f"{names[3]} I welcome you to dinner.")
print(f"{names[4]} I welcome you to dinner.")
print(f"{names[5]} I welcome you to dinner.")
