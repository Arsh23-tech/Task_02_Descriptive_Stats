import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_FILE = "2024_fb_ads_president_scored_anon.csv"

# Create output folder
os.makedirs("output", exist_ok=True)


# -----------------------------
# Load Data
# -----------------------------
print("Loading dataset...")
df = pd.read_csv(DATA_FILE)
print("Dataset loaded:", df.shape)


# -----------------------------
# 1. Message Type Distribution
# -----------------------------
message_cols = [col for col in df.columns if "msg_type" in col]

if message_cols:
    message_counts = df[message_cols].sum()

    clean_labels = [col.replace("_msg_type_illuminating", "") for col in message_counts.index]

    plt.figure(figsize=(10,6))
    plt.bar(clean_labels, message_counts)

    plt.title("Distribution of Message Types")
    plt.ylabel("Number of Ads")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("output/message_types.png")
    plt.close()


# -----------------------------
# 2. Top Political Topics
# -----------------------------
topic_cols = [col for col in df.columns if "topic_illuminating" in col]

if topic_cols:
    topic_counts = df[topic_cols].sum().sort_values(ascending=False).head(10)

    clean_topics = [col.replace("_topic_illuminating", "") for col in topic_counts.index]

    plt.figure(figsize=(12,6))
    plt.bar(clean_topics, topic_counts)

    plt.title("Top Political Topics in Ads")
    plt.ylabel("Number of Ads")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("output/top_topics.png")
    plt.close()


# -----------------------------
# 3. Incivility Distribution
# -----------------------------
if "incivility_illuminating" in df.columns:
    incivility = df["incivility_illuminating"].replace({
        0: "Civil Ads",
        1: "Incivil Ads"
    })

    counts = incivility.value_counts()

    plt.figure(figsize=(6,6))
    counts.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Incivility in Ads")
    plt.ylabel("")

    plt.tight_layout()
    plt.savefig("output/incivility.png")
    plt.close()


# -----------------------------
# 4. Spend vs Impressions
# -----------------------------
if "estimated_spend" in df.columns and "estimated_impressions" in df.columns:

    plt.figure(figsize=(8,6))
    plt.scatter(df["estimated_spend"], df["estimated_impressions"])

    plt.title("Spend vs Impressions")
    plt.xlabel("Estimated Spend")
    plt.ylabel("Estimated Impressions")

    plt.tight_layout()
    plt.savefig("output/spend_vs_impressions.png")
    plt.close()


# -----------------------------
# 5. Ads Over Time
# -----------------------------
if "ad_creation_time" in df.columns:
    df["ad_creation_time"] = pd.to_datetime(df["ad_creation_time"], errors="coerce")

    ads_over_time = df.groupby(df["ad_creation_time"].dt.to_period("M")).size()

    plt.figure(figsize=(12,6))
    ads_over_time.plot()

    plt.title("Number of Ads Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Ads")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("output/ads_over_time.png")
    plt.close()


print("All visualizations saved in /output folder!")