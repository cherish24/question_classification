import csv
cou = 0
cou1=0
training = []
with open("resource/LabelledData.txt") as tsv:
	cou = cou+1
	for line in tsv:
		train =  '\t'.join([line[0],line[1],line[2]])
		if not train in training:
			training.append(train)
			cou1 = cou1+1
print ("tatal--", cou, "ttotal after duplicate removal--",cou1)


training = []
with open("resource/LabelledData.txt") as tsv:
	for line in tsv:
		training.append(line[1])
	count = 0
	count1 = 0
	temp = []
	for a in training:
		count1 = count1 +1
		# print (a)
		if not a in temp:
			temp.append(a)
			count = count +1
print ("count is---",count)
print ("count1 is--",count1)