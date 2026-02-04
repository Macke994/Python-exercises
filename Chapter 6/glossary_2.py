programming_words = {"string" : "text data"}

programming_words["variable"] = "name that stores a value"
programming_words["integer"] = "whole number"
programming_words["list"] = "collection of multiple values stored in one variable"
programming_words["dictionary"] = "stores data as key-value pairs"
programming_words["boolean"] = "value that can only be true or false"
programming_words["conditional"] = "code that runs based on a condition"
programming_words["loop"] = "repeat code automatically"
programming_words["function"] = "reusable block of code that performs a task"
programming_words["index"] = "position of an item in a list or string"

for word, meaning in programming_words.items():
    print(f"{word.title()}:\n  {meaning}\n")
