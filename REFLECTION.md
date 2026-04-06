# 🔍 Reflection: Comparison of Data Analysis Approaches

## 1. Challenges in Producing Consistent Results

One of the key challenges in this project was ensuring consistency in numerical results across all three approaches: Pure Python, Pandas, and Polars.

Differences arose due to:
- Handling of missing values (NaN vs empty strings)
- Data type inference differences
- Floating-point precision variations

These discrepancies were resolved by standardizing preprocessing steps and ensuring consistent filtering of invalid values.

---

## 2. Ease of Use and Performance

Each approach offered a different experience:

### Pure Python
- Most difficult to implement
- Required manual handling of:
  - Missing values
  - Grouping logic
  - Statistical calculations
- Slowest performance, especially for grouped analysis

### Pandas
- Easiest to use
- Built-in methods like `describe()` and `groupby()` simplified analysis
- Good balance between readability and performance

### Polars
- Fastest performance
- More strict and expressive syntax using column expressions
- Slight learning curve compared to Pandas

---

## 3. Recommended Approach for Beginners

For a junior data analyst, Pandas is the best starting point because:
- It is widely used in industry
- Provides intuitive syntax
- Requires minimal code for complex operations

Pure Python is useful for understanding underlying mechanics, while Polars is better suited for advanced or performance-critical workflows.

---

## 4. Role of AI Tools in Development

AI tools such as ChatGPT were helpful in generating template code and accelerating development.

Observations:
- AI tools typically recommend Pandas by default for data analysis tasks
- They provide efficient boilerplate code for grouping and aggregation
- However, understanding the logic is still necessary to debug and adapt code

Overall, AI tools are effective assistants but should not replace conceptual understanding.

---

## 5. Handling Complex Data Columns

The dataset contains several complex columns, such as:
- Nested dictionaries (e.g., demographic distributions)
- Lists (e.g., publisher platforms, mentions)

Challenges:
- These columns could not be directly processed as numeric data
- Required treating them as categorical strings or excluding them from certain calculations

Differences across approaches:
- Pure Python required manual detection and handling
- Pandas handled them as object types automatically
- Polars enforced stricter typing but still allowed processing as strings

---

## 6. Key Takeaways

- Pure Python provides deep understanding but is inefficient for large datasets
- Pandas is the most practical tool for everyday data analysis
- Polars offers superior performance and modern design principles
- Handling messy, real-world data is a critical skill across all approaches

---

## 7. Conclusion

This project highlights the importance of choosing the right tool for the task. While all three approaches can achieve the same analytical goals, their differences in performance, usability, and abstraction make them suitable for different use cases.

Understanding these trade-offs is essential for effective data analysis.