# Descriptive Analysis of Facebook Political Ads (Milestone A)

## Project Overview

This project performs descriptive statistical analysis on a dataset of Facebook political advertisements related to the 2024 U.S. presidential election.

The objective is to implement the same analysis using three different approaches:

- Pure Python (standard library only)
- Pandas
- Polars

This allows comparison of implementation complexity, performance, and usability across different data processing methods.

---

## Dataset Access

The dataset is not included in this repository due to size and usage restrictions.

You can download it from:
[Google Drive: 2024 Election Social Media Data](https://drive.google.com/file/d/1UPo11lH2Mlk2cnLtjv8P9XqlKitms-gp/view)

### Instructions:
1. Download the dataset
2. Rename it to:
   fb_ads_president_scored_anon.csv
3. Place it in the project root directory

---

## Project Structure
```bash
task_02/
├── pure_python_stats.py # Manual implementation using standard library
├── pandas_stats.py # Analysis using Pandas
├── polars_stats.py # Analysis using Polars
│
├── README.md # Project documentation
├── REFLECTION.md # Analysis & comparison of approaches
├── requirements.txt # Dependencies
├── visualizations.py
└── .gitignore
```

---

## Requirements

Install dependencies:
pip install pandas polars

---

## How to Run

Run each script separately:

python pure_python_stats.py<br/>
python pandas_stats.py<br/>
python polars_stats.py


---

## Analysis Performed

For each script, the following analysis is performed:

### Dataset-Level Statistics
- Row count and column count
- Missing values (count and percentage)
- Inferred data types

### Column-Level Statistics
- Numeric columns:
  - Count, mean, median, min, max, standard deviation
- Categorical columns:
  - Count, unique values
  - Mode and frequency
  - Top 5 most frequent values

### Grouped Analysis
- Grouped by `page_id`
- Grouped by `page_id` and `ad_id`

---

## Key Observations

- The dataset contains a mix of numeric, categorical, and complex nested fields
- Binary indicator columns (0/1) are widely used for topics and message types
- Some columns contain nested structures (e.g., demographic distributions), requiring special handling
- Grouped analysis significantly increases computational complexity in pure Python

---

## Approach Comparison

| Aspect | Pure Python | Pandas | Polars |
|------|------------|--------|--------|
| Complexity | High | Low | Medium |
| Performance | Slow | Fast | Very Fast |
| Readability | Verbose | Clean | Concise |
| Flexibility | High | High | High |

---

## Conclusion

This project demonstrates how the same analytical tasks can be implemented using different tools, highlighting trade-offs between control, performance, and developer productivity.

---

## Author

Arsh Chandrakar  
M.S. Information Systems
