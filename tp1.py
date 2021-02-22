Texte="bonjour"
alphabet="abcdefghijklmnopqrstuvwxyz"
key=5
TexteC=[]
for c in Texte:
	y=alphabet.find(c)+key
	if (y>=26):
		y=y-25
	TexteC.append(alphabet[y])
TexteZ=''.join(TexteC)
print(TexteC)
	
for k in range(25):
	TexteD=[]
	for c in TexteZ:
		y=alphabet.find(c)-k
		if (y<0):
			y=y+25
		TexteD.append(alphabet[y])
	print(TexteD)
