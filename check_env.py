import streamlit, nltk, spacy, pandas, numpy 
nlp = spacy.load("en_core_web_sm") 
doc = nlp("Gradient descent minimizes the loss function.") 
print([t.text for t in doc]); print("Environment OK") 
