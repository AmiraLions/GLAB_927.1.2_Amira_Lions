# GLAB 927.1.2 - Hands-On Text Processing for Email Management
# Task 1: Import Libraries

# Import the Natural Language Toolkit (NLTK) library
import nltk

# Check the installed NLTK version 
nltk_version = nltk.__version__

# Print confirmation that NLTK imported successfully
print(f"NLTK library successfully imported. NLTK version: {nltk_version}")

# Taxk 2: Implementing Stemming

from nltk.stem import PorterStemmer

# Download the tokenizer resources required by NLTK
nltk.download("punkt")
nltk.download("punkt_tab")

# Sample business email
email_content = (
    "Our team will be working on the upcoming project deadlines. "
    "Please ensure that all deliverables are submitted before "
    "the end of the week."
)

# Create a Porter Stemmer Instance
porter_stemmer = PorterStemmer()

# Break the email into words and apply stemming
stemmed_words = [
    porter_stemmer.stem(word)
    for word in nltk.word_tokenize(email_content)
]

# Display the original and processed email
print("\n--- Task 2: Stemming ---")
print("Original Email Content:", email_content)
print("Stemmed Email Content:", " ".join(stemmed_words))

# Task 3: Applying Lemmatization

from nltk.stem import WordNetLemmatizer

# Download the WordNet resource
nltk.download("wordnet")

# Sample business email for lemmatization
email_content_lemma = (
    "The team members are working on their tasks diligently. "
    "Please ensure that every report is submitted promptly."
)

# Create a WordNet Lemmatizer instance
lemmatizer = WordNetLemmatizer()

# Break the email into words and apply lemmatization
lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in nltk.word_tokenize(email_content_lemma)
]

# Display the original and processed email
print("\n--- Task 3: Lemmatization ---")
print("Original Email Content:", email_content_lemma)
print("Lemmatized Email Content:", " ".join(lemmatized_words))