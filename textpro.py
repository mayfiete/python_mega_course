

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "when", "where", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


print(sentence_maker("how are you"))

results = []

while True:
    user_input = input("Say something: ")
    if user_input == "quit":
        break
    else:
        results.append(sentence_maker(user_input))

print(results)

print(" ".join(results))  # concatenate all the results from a list
