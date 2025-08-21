import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Load data
data = pd.read_csv('data/spam.csv', encoding='latin-1')
# Inspect columns, drop unnecessary columns if present
data = data[['v1', 'v2']]
data.columns = ['label', 'text']

# Map label to binary values: spam=1, ham=0
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

# Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label_num'], test_size=0.2, random_state=42)

# Create a simple text classification pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB()),
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model on test set
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the pipeline (vectorizer + model) to a file
joblib.dump(pipeline, 'app/model.joblib')

print("Model saved to app/model.joblib")
