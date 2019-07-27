
import re

def readFile(filename):
	#Implement this
	f = open(filename, "r")

	str = f.read().lower()
	f.close()
	return str
	
def wordCount(str, keywords):
	
	dict = {}
	str = re.sub(r"[^a-zA-Z]+", " ", str)
	words_list = str.split(" ")
	set_of_words = set(words_list)
	#initialize dictionary
	for i in set_of_words:
		if i not in keywords:
			dict[i]=0
	
	for i in words_list:
		if i in dict:
			dict[i] += 1
	
	return dict
	
def topTenWords(wordCountDict):
	#Implement this
	sorted_dict = sorted(wordCountDict, key= wordCountDict.get, reverse=True)
	for i in range(10):
		print(sorted_dict[i] +" : " + str(wordCountDict[sorted_dict[i]]))
	


def main():
	filename= "town-mouse.txt"
	keywords = ["a", "an", "the", "how", "to", "i", "you", "of", "this", "gutenberg", "tm"]
	contents= readFile(filename)
	wordCountDict= wordCount(contents, keywords)
	topTenWords(wordCountDict)
	

if __name__=="__main__":
	main()
