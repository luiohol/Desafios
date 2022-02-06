word = input()
letters = list(set(list(word)))
dictWord = {}
for letter in letters: dictWord[letter] = 0
score = 0
steps = 0
while score != len(letters):
    score = 0
    userInput = input()
    if userInput in dictWord:
        dictWord[userInput] = 1
    steps += 1
    for field in dictWord: score += dictWord[field]
print(steps)