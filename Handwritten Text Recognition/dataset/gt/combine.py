f1=open('words.txt','a')
f2=open('wordsadd.txt','r')

for i in range(240):
	sentence=f2.readline()
	f1.write(sentence)