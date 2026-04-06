import pandas as pd

DATA_FILE = "2024_fb_ads_president_scored_anon.csv"


# -----------------------------
# Load Data
# -----------------------------

def load_data():
    print("Loading dataset...")
    df = pd.read_csv(DATA_FILE)
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    return df


# -----------------------------
# Dataset Overview
# -----------------------------

def dataset_overview(df):
    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print("\nBasic Info:")
    print(df.info())

    print("\nMissing Values (Count):")
    print(df.isnull().sum())

    print("\nMissing Values (%):")
    print((df.isnull().sum() / len(df)) * 100)


# -----------------------------
# Column Statistics
# -----------------------------

def column_analysis(df):
    print("\n" + "=" * 60)
    print("COLUMN STATISTICS")
    print("=" * 60)

    print("\nNumeric Columns Summary:")
    print(df.describe())

    print("\nCategorical Columns Summary:")
    print(df.describe(include=['object']))

    print("\nTop Values per Categorical Column:")
    for col in df.select_dtypes(include='object').columns:
        print(f"\n--- {col} ---")
        print(df[col].value_counts().head(5))

    print("\nUnique Values per Column:")
    print(df.nunique())


# -----------------------------
# Grouped Analysis
# -----------------------------

def grouped_analysis(df):
    print("\n" + "=" * 60)
    print("GROUPED ANALYSIS: page_id")
    print("=" * 60)

    group_page = df.groupby("page_id")

    numeric_cols = df.select_dtypes(include='number').columns
    print("\nNumeric Aggregations (Top 5 Groups):")
    print(group_page[numeric_cols].agg(['count', 'mean', 'min', 'max']).head())

    print("\nSample Group (first page_id):")
    first_key = list(group_page.groups.keys())[0]
    print(group_page.get_group(first_key).head())


    print("\n" + "=" * 60)
    print("GROUPED ANALYSIS: page_id + ad_id")
    print("=" * 60)

    group_page_ad = df.groupby(["page_id", "ad_id"])

    numeric_cols = df.select_dtypes(include='number').columns
    print("\nNumeric Aggregations (Top 5 Groups):")
    print(group_page_ad[numeric_cols].agg(['count', 'mean', 'min', 'max']).head())

    print("\nSample Group:")
    first_key = list(group_page_ad.groups.keys())[0]
    print(group_page_ad.get_group(first_key).head())


# -----------------------------
# Main Execution
# -----------------------------

def main():
    df = load_data()

    dataset_overview(df)
    column_analysis(df)
    grouped_analysis(df)


if __name__ == "__main__":
    main()