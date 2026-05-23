import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once
nltk.download('stopwords')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


# ✅ Structured Technical Skill Database
SKILL_SET = {

    # Programming Languages
    "python", "java", "c", "c++", "javascript",
    "typescript", "go", "rust", "kotlin", "swift",

    # Web Development
    "html", "css", "react", "angular", "vue",
    "node", "express", "nextjs",

    # Backend
    "api", "rest api", "graphql",
    "flask", "fastapi", "django", "spring boot",

    # Databases
    "sql", "mysql", "postgresql",
    "mongodb", "redis", "firebase",

    # Data Science & ML
    "machine learning",
    "deep learning",
    "computer vision",
    "natural language processing",
    "nlp",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit learn",
    "tensorflow",
    "keras",
    "pytorch",
    "xgboost",
    "opencv",
    "cnn",
    "yolo",

    # Core CS
    "data structures",
    "algorithms",
    "operating systems",
    "dbms",
    "networking",
    "computer networks",

    # Cloud & DevOps
    "aws", "azure", "gcp",
    "docker", "kubernetes",
    "ci cd", "jenkins",

    # Tools
    "git", "github", "gitlab",
    "bitbucket", "linux", "vscode",

    # Mobile
    "android", "flutter",
    "react native", "ios",

    # AI
    "llm", "rag", "langchain",
    "transformers", "openai",

    # Security
    "authentication",
    "oauth",
    "encryption",
    "cybersecurity",
    "jwt",

    # Testing
    "testing",
    "pytest",
    "selenium",
    "unittest",

    # Architecture
    "microservices",
    "system design",
    "software architecture"
}


# ✅ Synonym Mapping
SYNONYMS = {

    # AI/ML
    "ml": "machine learning",
    "ai": "machine learning",
    "dl": "deep learning",
    "cv": "computer vision",
    "nlp": "natural language processing",
    "cnn": "deep learning",
"pytorch": "deep learning",
"opencv": "computer vision",
"yolo": "computer vision",
"aiml": "machine learning",

    # APIs
    "rest": "rest api",

    # Frameworks
    "tf": "tensorflow",

    # CS
    "dsa": "data structures",

    # Cloud
    "aws cloud": "aws"
}


# ✅ Clean text
def clean_text(text):

    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# ✅ Normalize word
def normalize_word(word):

    word = lemmatizer.lemmatize(word)

    if word in SYNONYMS:
        return SYNONYMS[word]

    return word


# ✅ Extract keywords
def extract_keywords(text):

    text = clean_text(text)

    words = text.split()

    # remove stopwords
    words = [
        w for w in words
        if w not in STOPWORDS and len(w) > 2
    ]

    # normalize
    normalized_words = [
        normalize_word(w)
        for w in words
    ]

    # create normalized text
    normalized_text = " ".join(normalized_words)

    detected_skills = []

    # ✅ Presence-based detection
    for skill in SKILL_SET:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, normalized_text):
            detected_skills.append(skill)

    return sorted(list(set(detected_skills)))