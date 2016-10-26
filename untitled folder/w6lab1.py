nouns = ["cat", "dog", "ant"]
adjs = ["big", "small", "old", "young", "awsom"]
prpNns =  ["Bob", "Snowden", "Andy", "Rob"]
sentence = "Hello i am *prpNn and I am a *adj *noun"
vows =  ["a", "e", "i", "o", "u"]
sentence = sentence.split()
i = 0
for wrd in sentence:
	if wrd == "*noun":
		nw = random.choice(nouns)
		sentence[i] = nw
	if wrd == "*prpNn":
		nw = random.choice(prpNns)
		sentence[i] = nw
	if wrd == "*adj":
		nw = random.choice(adjs)
		sentence[i] = nw
		if nw[0] in vows:
			sentence[i-1] = "an"
	i += 1

final = ""
for word in sentence:
	final += word 
	final += " "

print(final)
