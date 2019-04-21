from bs4 import BeautifulSoup
import os

def reset_lists():
	listName.clear()
	listXMin.clear()
	listYMin.clear()
	listXMax.clear()
	listYMax.clear()

def createTxt(soup, output):
	filename = ''

	for fn in soup.find_all('filename'):
		filename = fn.string

	for obj in soup.find_all('object'):
		for name in obj.find_all('name'):
			listName.append(name.string)
		for xmin in obj.find_all('xmin'):
			listXMin.append(xmin.string)
		for xmax in obj.find_all('xmax'):
			listXMax.append(xmax.string)
		for ymin in obj.find_all('ymin'):
			listYMin.append(ymin.string)
		for ymax in obj.find_all('ymax'):
			listYMax.append(ymax.string)

		if len(listName) != len(listXMin) or \
			len(listName) != len(listXMax) or \
			len(listName) != len(listYMin) or \
			len(listName) != len(listYMax):
			print("Error !!")

		for i in range(len(listName)):
			listBB.append([listName[i],listXMin[i],listYMin[i],listXMax[i],listYMax[i]])
		i = i + 1

		reset_lists()

	outputName = "../AnnotationsTxt/" + output

	f = open(outputName, "a+")

	for i in range(len(listBB)):
		f.write(filename + "," + listBB[i][1] + "," + listBB[i][2] + "," + \
			listBB[i][3] + "," + listBB[i][4] + "," + listBB[i][0])
		f.write("\n")


listBB   = []
listName = []
listXMin = []
listYMin = []
listXMax = []
listYMax = []

j = 0

for filename in os.listdir(os.getcwd()):
	print(j)
	reset_lists()
	listBB.clear()
	if ".xml" in filename:	
		html_doc = open(filename, 'r')
		soup = BeautifulSoup(html_doc, 'html.parser')
		out = filename.replace(".xml", ".txt", 1)
		createTxt(soup, out)
	j = j + 1