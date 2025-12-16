# Define the facts
tests = [
    {"fact": "Harry Potter's wand is made of holly and phoenix feather.", "result": True, "description": "Harry Potter's wand material."},
    {"fact": "Hermione Granger was born in 1980.", "result": False, "description": "Hermione's birth year."},
    {"fact": "The Hogwarts house colors are Gryffindor (red), Slytherin (green), Ravenclaw (blue), and Hufflepuff (yellow).", "result": True, "description": "Hogwarts house colors."},
    {"fact": "Albus Dumbledore is the head of Gryffindor house.", "result": False, "description": "Dumbledore's house role."},
    {"fact": "The Triwizard Tournament takes place every 4 years.", "result": True, "description": "Triwizard Tournament frequency."},
    {"fact": "The Weasley twins are older than Ron Weasley.", "result": False, "description": "Weasley twins' age relation."},
    {"fact": "Harry Potter can speak Parseltongue, the language of snakes.", "result": True, "description": "Harry's ability to speak Parseltongue."},
    {"fact": "Severus Snape was never a member of the Order of the Phoenix.", "result": False, "description": "Snape's Order membership."},
    {"fact": "The Marauder's Map was created by James Potter, Sirius Black, Remus Lupin, and Peter Pettigrew.", "result": True, "description": "Marauder's Map creators."},
    {"fact": "Cedric Diggory was the winner of the Triwizard Tournament in the fourth book.", "result": False, "description": "Cedric Diggory's Triwizard Tournament victory."},
]

# Loop through the tests and print the description and prediction
for test in tests:
    print(f"Test: {test['description']}")
    print(f"Fact: {test['fact']}")
    print(f"Prediction: This is {'True' if test['result'] else 'False'}.\n")
