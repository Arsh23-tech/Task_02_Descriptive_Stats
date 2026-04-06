import polars as pl

DATA_FILE = "2024_fb_ads_president_scored_anon.csv"


# -----------------------------
# Load Data
# -----------------------------

def load_data():
    print("Loading dataset...")
    df = pl.read_csv(DATA_FILE)
    print("Dataset loaded successfully!")
    print("Shape:", df.shape)
    return df


# -----------------------------
# Dataset Overview
# -----------------------------

def dataset_overview(df):
    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print("\nSchema:")
    print(df.schema)

    print("\nMissing Values (Count):")
    print(df.null_count())

    print("\nMissing Values (%):")
    print((df.null_count() / df.height) * 100)


# -----------------------------
# Column Statistics
# -----------------------------

def column_analysis(df):
    print("\n" + "=" * 60)
    print("COLUMN STATISTICS")
    print("=" * 60)

    print("\nDescribe:")
    print(df.describe())

    print("\nTop Values for Categorical Columns:")

    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            print(f"\n--- {col} ---")
            print(df[col].value_counts().head(5))

    print("\nUnique Values per Column:")
    print(df.select([pl.col(c).n_unique().alias(c) for c in df.columns]))


# -----------------------------
# Grouped Analysis
# -----------------------------

def grouped_analysis(df):
    print("\n" + "=" * 60)
    print("GROUPED ANALYSIS: page_id")
    print("=" * 60)

    # Select only numeric columns
    numeric_cols = [
        col for col, dtype in df.schema.items()
        if dtype in [pl.Int64, pl.Float64]
    ]

    # Keep only relevant columns (avoid nested data issues)
    df_numeric = df.select(["page_id"] + numeric_cols)

    # Group by page_id
    group_page = df_numeric.group_by("page_id").agg(
        [
            expr
            for col in numeric_cols
            for expr in [
                pl.col(col).count().alias(f"{col}_count"),
                pl.col(col).mean().alias(f"{col}_mean"),
                pl.col(col).min().alias(f"{col}_min"),
                pl.col(col).max().alias(f"{col}_max"),
            ]
        ]
    )

    print(group_page.head())


    print("\n" + "=" * 60)
    print("GROUPED ANALYSIS: page_id + ad_id")
    print("=" * 60)

    df_numeric_2 = df.select(["page_id", "ad_id"] + numeric_cols)

    group_page_ad = df_numeric_2.group_by(["page_id", "ad_id"]).agg(
        [
            expr
            for col in numeric_cols
            for expr in [
                pl.col(col).count().alias(f"{col}_count"),
                pl.col(col).mean().alias(f"{col}_mean"),
                pl.col(col).min().alias(f"{col}_min"),
                pl.col(col).max().alias(f"{col}_max"),
            ]
        ]
    )

    print(group_page_ad.head())


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