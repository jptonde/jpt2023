import nltk

def dep():
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    nltk.download('punkt')

if __name__ == "__main__":
    dep()
