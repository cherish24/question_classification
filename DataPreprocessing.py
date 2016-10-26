import csv

def question_category():
	with open('resource/LabelledData.txt','r') as labeled, \
	 open('resource/question.csv','wt') as question,   \
	  open('resource/category.csv','wt') as category:

		for line in labeled:
			line_question = line.split(",,,")[0]
			line_category = line.split(',,,')[1]
			line_question=line_question.replace("?","")
			line_question=line_question.strip()
			line_category=line_category.strip()
			line_category=line_category.replace("\n","").replace("\r","")#.replace('" ','')
			csv.writer(question).writerow([line_question])
			csv.writer(category).writerow([line_category])

def data_check():
	with open('resource/LabelledData.txt','r') as labeled, open('resource/need_Check.txt','wt') as check :
		counter = 1
		for line in labeled:
			first = line.split(' ', 1)[0]
			last = line.rsplit(None, 1)[-1]
			if first not in last:
				check.write(str(counter))
				check.write(line)
			counter = counter+1


def txt_to_tsv():
	counter = 0
	with open('resource/LabelledData.txt','r') as labeled, \
	 open('resource/LabelledData.csv','wt') as question  :
	 	
		for line in labeled:
			l = []
			line_question = line.split(",,,")[0]
			line_category = line.split(',,,')[1]
			line_question=line_question.replace("?","")
			line_question=line_question.strip()
			line_category=line_category.strip()
			line_category=line_category.replace("\n","").replace("\r","")
			l.append(line_question)
			l.append(line_category)
			csv.writer(question).writerow(l)
			counter = counter+1
	print(counter)

if __name__ == '__main__':
	
	txt_to_tsv()
	# data_check()