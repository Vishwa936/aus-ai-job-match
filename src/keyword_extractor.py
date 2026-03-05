import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

# Generic resume words that are not technical skills
GENERIC_TERMS = {
    "experience","developer","engineer","team","project","projects",
    "work","development","application","applications","role","candidate",
    "system","systems","technology","technologies","software","analysis"
}

# Valid multi-word skills
VALID_BIGRAMS = {
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",
    "computer vision",
    "natural language processing",
    "neural networks",
    "rest api",
    "rest apis"
}


def extract_keywords(text, top_n=15):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2)
    )

    tfidf_matrix = vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    keyword_scores = list(zip(feature_names, scores))
    keyword_scores.sort(key=lambda x: x[1], reverse=True)

    keywords = []

    for phrase, score in keyword_scores:

        words = phrase.split()

        # remove stopwords
        if any(word in STOP_WORDS for word in words):
            continue

        # remove generic resume terms
        if any(word in GENERIC_TERMS for word in words):
            continue

        doc = nlp(phrase)

        # keep only nouns / proper nouns
        if not all(token.pos_ in ["NOUN", "PROPN"] for token in doc):
            continue

        # handle bigrams
        if len(words) == 2:

            # keep only if it is a valid bigram
            if phrase not in VALID_BIGRAMS:
                continue

        keywords.append(phrase)

        if len(keywords) >= top_n:
            break

    # Remove single words if they belong to multi-word skills
    clean_keywords = set(keywords)

    for kw in list(clean_keywords):
        if " " not in kw:
            for other in clean_keywords:
                if kw in other and kw != other:
                    clean_keywords.discard(kw)
                    break

    return clean_keywords


def find_missing_keywords(resume_text, job_text):

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    missing = job_keywords - resume_keywords

    return missing