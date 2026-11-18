import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

fake['label'] = 1
real['label'] = 0

df = pd.concat([fake[:2000], real[:2000]])  # only 2000 fake + 2000 real
df = df[['title', 'text', 'label']]
df.dropna(inplace=True)
df['content'] = df['title'] + " " + df['text']

# Split
X = df['content']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = PassiveAggressiveClassifier()
model.fit(X_train_vec, y_train)

# Save both together
pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print(df['label'].value_counts())

sample = ["India wins the T20 World Cup 2024 after a thrilling final."]
sample_vec = vectorizer.transform(sample)
print(model.predict(sample_vec))  # Should be 0 for Real
