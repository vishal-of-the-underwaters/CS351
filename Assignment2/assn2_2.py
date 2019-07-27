
import re

def readFile(filename):
	#Implement this
	f = open(filename, "r")

	str = f.read().lower()
	f.close()
	return str
	
def wordCount(str):
	#str = unicode_to_ascii(str.lower().strip())
	
	dict = {}
	str = re.sub(r"[^a-zA-Z]+", " ", str)
	words_list = str.split(" ")
	set_of_words = set(words_list)
	#initialize dictionary
	for i in set_of_words:
		dict[i]=0
	
	for i in words_list:
		dict[i] += 1
	
	return dict
	
def topTenWords(wordCountDict):
	#Implement this
	sorted_dict = sorted(wordCountDict, key= wordCountDict.get, reverse=True)
	for i in range(10):
		print(sorted_dict[i] +" : " + str(wordCountDict[sorted_dict[i]]))
	


def main():
	filename= "town-mouse.txt"
	
	contents= readFile(filename)
	wordCountDict= wordCount(contents)
	topTenWords(wordCountDict)
	

if __name__=="__main__":
	main()
