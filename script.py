
import collections
#import statistics
from os import listdir
from os.path import isfile, join





positive_sentiment = ["appetizing", "delectable", "delicious", "flavorful", "gourmet", "luscious", "mouthwatering", "savory", "scrumptious", "tastiest", "tasty", "toothsome", "yummy"]
plenty = ["big", "bigger", "biggest", "bottomless", "bountiful", "colossal", "endless", "enormous", "generous", "generously", "gigantic", "ginormous", "heaped", "heaping", "hearty", "hefty", "huge", "largest", "loaded", "loads", "lots", "mammoth", "massive", "mega", "oversized", "overstuffed", "piled", "plentiful", "plenty", "refills", "unlimited", "and more", "king sized", "texas sized", "thick cut", "tons of", "with more"]
choice = ["choice", "choose", "any", "add", "or", "specify", "substitutions", "specifications", "options", "pick", "your way", "your own", "your liking", "your style", "your favorite", "you like", "you want", "you request", "way you", "you may", "select your", "select from", "you select", "select one", "select any", "select or", "select a", "select up", "select two"]
traditional = ["home", "traditional", "timeless", "family recipe", "all american", "our founder", "old fashioned", "old school", "american favorite", "america's favorite", "all time favorite", "old favorite"]
healthy = ["organic", "certified", "superfood", "artisan", "aquafaba", "bpa", "natural", "sugar free", "probiotic", "gluten", "omega", "grass-fed", "grass fed", "gmo", "cage free", "cage-free", "range free", "range-free", "real fruit", "whole grain", "whole wheat", "acv", "multigrain", "local", "antioxidant", "cold brew", "kale", "quinoa", "acai", "avocado", "spinach", "responsibl", "wage", "recycl", "clean", "environment", "farm", "pasture"]

wordsets = [positive_sentiment,plenty,choice,traditional, healthy]

Frequencies = collections.namedtuple('Frequencies', ['filename', 'postive', 'plenty', 'choice', 'traditional', 'healthy'])

def analysis(file):
	with open(file, 'r') as f:
		content = f.read()
		content = content.lower()
		corpus = ' '.join(content.split('\n'))
		numwords = float(len(corpus.split(' ')))

		means = [file]
		for wordset in wordsets:
			count = 0.0
			for word in wordset:
				count += corpus.count(word)
			means.append(count/numwords)
		return Frequencies(*means)





def main():
	fast_casual = [f for f in listdir('fast\ casual') if isfile(str('fast\ casual/' +f)) and (".py" not in f)] #working in directory with all the files
	freqs1 = [analysis(str('fast\ casual/' +f)) for file in fast_casual]
	print(len(freqs1))

	casual_dining = [f for f in listdir('Casual Dining') if isfile(str('Casual Dining/' +f)) and (".py" not in f)] #working in directory with all the files
	freqs2 = [analysis(str('Casual Dining/' +f)) for file in casual_dining]
	print(len(freqs2))

	fast_food = [f for f in listdir('Fast Food') if isfile(str('Fast Food/' +f)) and (".py" not in f)] #working in directory with all the files
	freqs3 = [analysis(str('Fast Food/' +f)) for file in fast_food]
	print(len(freqs3))


	for freq in freqs1:
		print(" ")
		print(freq)

	for freq in freqs2:
		print(" ")
		print(freq)

	for freq in freqs3:
		print(" ")
		print(freq)




	




if __name__ == '__main__':
	main()