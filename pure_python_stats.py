import csv
import math
from collections import Counter, defaultdict

DATA_FILE = "2024_fb_ads_president_scored_anon.csv"


# -----------------------------
# Utility Functions
# -----------------------------

def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]


def std_dev(values):
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


# -----------------------------
# Data Loading
# -----------------------------

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


# -----------------------------
# Column Analysis
# -----------------------------

def analyze_column(values):
    clean_values = [v for v in values if v not in ("", None)]

    if not clean_values:
        return None

    # Detect complex structures (dict/list stored as string)
    if any(str(v).startswith("{") or str(v).startswith("[") for v in clean_values):
        counter = Counter(clean_values)
        return {
            "type": "complex/categorical",
            "count": len(clean_values),
            "unique": len(counter),
            "top_5": counter.most_common(5)
        }

    # Try numeric
    numeric_values = []
    for v in clean_values:
        try:
            numeric_values.append(float(v))
        except:
            numeric_values = []
            break

    if numeric_values:
        return {
            "type": "numeric",
            "count": len(numeric_values),
            "mean": round(mean(numeric_values), 2),
            "median": round(median(numeric_values), 2),
            "min": min(numeric_values),
            "max": max(numeric_values),
            "std_dev": round(std_dev(numeric_values), 2)
        }

    # Otherwise categorical
    counter = Counter(clean_values)
    return {
        "type": "categorical",
        "count": len(clean_values),
        "unique": len(counter),
        "mode": counter.most_common(1)[0],
        "top_5": counter.most_common(5)
    }


# -----------------------------
# Dataset-Level Analysis
# -----------------------------

def dataset_analysis(data):
    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    columns = list(data[0].keys())

    print(f"Total Rows: {len(data)}")
    print(f"Total Columns: {len(columns)}")

    print("\nMissing Values Per Column:")
    for col in columns:
        missing = sum(1 for row in data if row[col] in ("", None))
        print(f"{col}: {missing}")

    print("\nColumn Statistics:")
    for col in columns:
        values = [row[col] for row in data]
        stats = analyze_column(values)

        print(f"\n--- {col} ---")
        print(stats)


# -----------------------------
# Grouping Logic
# -----------------------------

def group_by(data, keys):
    groups = defaultdict(list)

    for row in data:
        key = tuple(row[k] for k in keys)
        groups[key].append(row)

    return groups


# -----------------------------
# Grouped Analysis
# -----------------------------

def grouped_analysis(data, group_keys, label, limit=5):
    print("\n" + "=" * 60)
    print(f"GROUPED ANALYSIS: {label}")
    print("=" * 60)

    groups = group_by(data, group_keys)

    print(f"Total Groups: {len(groups)}")

    for key, rows in list(groups.items())[:limit]:
        print(f"\nGroup: {key}")
        print(f"Rows in group: {len(rows)}")

        columns = rows[0].keys()

        for col in columns:
            values = [row[col] for row in rows]
            stats = analyze_column(values)

            print(f"{col}: {stats}")


# -----------------------------
# Main Execution
# -----------------------------

def main():
    print("Loading dataset...")
    data = load_data(DATA_FILE)

    print("Dataset loaded successfully!")

    # Dataset-level stats
    dataset_analysis(data)

    # Group by page_id
    grouped_analysis(data, ["page_id"], "By page_id")

    # Group by page_id + ad_id
    grouped_analysis(data, ["page_id", "ad_id"], "By page_id & ad_id")


if __name__ == "__main__":
    main()