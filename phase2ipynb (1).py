# -*- coding: utf-8 -*-
"""phase2ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ApMwkpWGwCnyq37_v4qPNM8y32L4gapa
"""

from google.colab import files
import pandas as pd
uploaded = files.upload()
df = pd.read_csv(next(iter(uploaded)))
df.head()

from google.colab import sheets
sheet = sheets.InteractiveSheet(df=df)

# prompt: column name Platform give a value Instagram

import pandas as pd

# Assuming social_media_sentiment.csv is in the current directory
# If not, provide the full path to the file
try:
    df = pd.read_csv('social_media_sentiment.csv')

    # Check if 'Platform' column exists
    if 'Platform' in df.columns:
        # Assign 'Instagram' to the 'Platform' column
        df['Platform'] = 'Instagram'
        print(df.head())
    else:
        print("Error: 'Platform' column not found in the DataFrame.")

except FileNotFoundError:
    print("Error: social_media_sentiment.csv not found.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: Could not parse the CSV file correctly.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")