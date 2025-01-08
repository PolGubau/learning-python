

iterable = "APPLE"
# iterable = ["A","P","P","L","E"]
# iterable = ("A","P","P","L","E")
# iterable = {"A":1,"P":2,"P":3,"L":4,"E":5}
# iterable = range(5)


letter = input("Guess a letter in the word: ")

if letter.upper() in iterable:
    print("Yes, the letter is in the word.")
else:
    print("No, the letter is not in the word.")