import pandas as pd

# Define the mapping of sentiment labels
sentiment_mapping = {"negative": 0, "positive": 1, "neutral": 2}

# Read the text file into a DataFrame
with open("base-data\FinancialPhraseBank\Sentences_75Agree.txt", "r") as file:
    lines = file.readlines()

data = []
for line in lines:
    text, sentiment = line.strip().rsplit('@', 1)
    label = sentiment_mapping[sentiment.lower()]
    data.append((text, label))

df = pd.DataFrame(data, columns=["Text", "Label"])

# Write the DataFrame to a CSV file
df.to_csv("base-data\\FinancialPhraseBank\\all-data-75-above.csv", index=False)
