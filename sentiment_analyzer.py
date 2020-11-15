import spacy
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spacy model 'en_core_web_sm'...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        return {"text": text, "polarity": polarity, "subjectivity": subjectivity, "sentiment": sentiment}

    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = [{
            "text": ent.text,
            "label": ent.label_,
            "start_char": ent.start_char,
            "end_char": ent.end_char
        } for ent in doc.ents]
        return entities

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    text1 = "This movie was absolutely fantastic! I loved every moment of it."
    print(f"Sentiment for \"{text1}\": {analyzer.analyze_sentiment(text1)}")
    print(f"Entities for \"{text1}\": {analyzer.extract_entities(text1)}\n")

    text2 = "The service was terrible, and the food was mediocre."
    print(f"Sentiment for \"{text2}\": {analyzer.analyze_sentiment(text2)}")
    print(f"Entities for \"{text2}\": {analyzer.extract_entities(text2)}\n")

    text3 = "The quick brown fox jumps over the lazy dog."
    print(f"Sentiment for \"{text3}\": {analyzer.analyze_sentiment(text3)}")
    print(f"Entities for \"{text3}\": {analyzer.extract_entities(text3)}\n")
