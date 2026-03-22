import matplotlib.pyplot as plt
import pandas as pd


def normalize_food_storage(value):
    value = str(value).strip().lower()

    if value in ["granaries", "stored grain", "surplus storage"]:
        return "Storage Present"
    elif value in ["none", "no storage", "not stored"]:
        return "No Storage"
    else:
        return "Other"


def plot_food_storage_grouped(df):
    grouped_storage = df["food_storage"].apply(normalize_food_storage)
    counts = grouped_storage.value_counts()

    counts.plot(kind="bar")
    plt.title("Food Storage Systems in Early Civilizations")
    plt.xlabel("Storage Category")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_settlement_vs_food(df):
    cross_tab = pd.crosstab(df["settlement_type"], df["food_source"])

    cross_tab.plot(kind="bar")
    plt.title("Settlement Type vs Food Source")
    plt.xlabel("Settlement Type")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()