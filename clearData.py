from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+');
stpWrd = set(stopwords.words('english'))
ps = PorterStemmer()

def getCleanReview(review):
	review = review.lower();
	review = review.replace("<br/><br/>"," ")
	tokens = tokenizer.tokenize(review)
	newTokens = [token for token in tokens if token not in stpWrd]
	stemmedToken = [ps.stem(token) for token in newTokens]

	cleanedReview = ' '.join(stemmedToken)
	return cleanedReview
