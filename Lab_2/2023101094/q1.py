sentence = input("Enter the sentence: ")

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

print(" ".join(words))