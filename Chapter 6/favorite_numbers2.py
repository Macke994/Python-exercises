favorite_numbers = {
    "linus": [7, 17],
    "stefan": [42, 55],
    "mari": [3, 19],
    "hannes": [9, 27],
    "sebbe": [13, 30]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"  - {number}")
        