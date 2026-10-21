# GLAB 927.1.2 — Hands-On Text Processing for Email Management with Python

**Author:** Amira Lions  
**Course:** Per Scholas CAX 215

## Project Overview

This project demonstrates how Python's Natural Language Toolkit (NLTK) can be used to process business email content through stemming and lemmatization.

## Learning Objectives

- Import and use the NLTK library.
- Apply stemming to business email text.
- Apply lemmatization to standardize words.
- Understand how text processing supports email analysis and categorization.

## Implementation

**Task 1 — Importing NLTK**

Imports the NLTK library and displays its installed version.

**Task 2 — Stemming**

Uses `PorterStemmer` to reduce words in a sample business email to simplified root forms.

**Task 3 — Lemmatization**

Uses `WordNetLemmatizer` to convert words in another sample email to their dictionary forms.

## Technologies

- Python 3.14.7
- NLTK 3.10.3
- VS Code
- uv
- Git and GitHub

## Running the Program

From the project directory, install the required dependencies:

```powershell
uv sync
```

Then execute the Python file:

```powershell
uv run python glab_927_1_2.py
```

The program displays the NLTK version, original email text, stemmed text, and lemmatized text.

NLTK may download required language resources on the first run.

## Testing

All three tasks were executed successfully in the local Python environment without errors.

## Submission

The required Python source file is:

`glab_927_1_2.py`

This file is submitted directly to Canvas for instructor review.
