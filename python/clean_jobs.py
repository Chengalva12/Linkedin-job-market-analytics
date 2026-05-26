import pandas as pd

df = pd.read_csv(r"C:\Users\cheng\OneDrive\Desktop\job-market-analytics\data\archive\postings.csv")

print(df.head())

df = df.drop_duplicates()

df["title"] = df["title"].fillna("Unknown")
df["company_name"] = df["company_name"].fillna("Unknown")
df["location"] = df["location"].fillna("Unknown")
df["description"] = df["description"].fillna("")

skills = [
    "python",
    "sql",
    "power bi",
    "tableau",
    "excel",
    "aws",
    "azure",
    "machine learning",
    "data analysis",
    "data visualization",
    "spark",
    "hadoop",
    "etl",
    "javascript",
    "java"
]

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return ", ".join(found)

df["extracted_skills"] = df["description"].apply(extract_skills)

df.to_csv(
    r"C:\Users\cheng\OneDrive\Desktop\job-market-analytics\data\cleaned_jobs.csv",
    index=False
)

print("Dataset cleaned successfully")