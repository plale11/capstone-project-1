import pandas as pd
import matplotlib.pyplot as plt


# ============================================
# Ancient River Civilizations
# Environment, Settlement, and the Rise of Early Societies
#
# Main Question:
# How did environmental conditions influence
# the emergence and development of early civilizations?
# ============================================


def summarize_project_direction() -> None:
    print("\n=== Project Direction ===")
    print("This project explores how river environments supported settlement,")
    print("food production, storage systems, and the growth of early communities.")
    print("It focuses on how environmental stability led to agriculture,")
    print("surplus storage, and organized community life in early civilizations.")


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def show_basic_info(df: pd.DataFrame) -> None:
    print("\n=== First 5 Rows ===")
    print(df.head())

    print("\n=== Columns ===")
    print(df.columns.tolist())

    print("\n=== Data Info ===")
    df.info()


def analyze_settlement_and_food(df: pd.DataFrame) -> None:
    print("\n=== Settlement Types ===")
    print(df["settlement_type"].value_counts())

    print("\n=== Food Sources ===")
    print(df["food_source"].value_counts())

    print("\n=== Food Storage Systems ===")
    print(df["food_storage"].value_counts())

    print("\n=== Irrigation Systems ===")
    print(df["irrigation"].value_counts())

    print("\n=== Community Structures ===")
    print(df["community_structure"].value_counts())


def visualize_food_storage(df: pd.DataFrame) -> None:
    storage_counts = df["food_storage"].value_counts()

    plt.figure(figsize=(8, 5))
    storage_counts.plot(kind="bar")
    plt.title("Food Storage Systems in Early Civilizations")
    plt.xlabel("Food Storage Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def visualize_community_structure(df: pd.DataFrame) -> None:
    community_counts = df["community_structure"].value_counts()

    plt.figure(figsize=(8, 5))
    community_counts.plot(kind="bar")
    plt.title("Community Structures in Early Civilizations")
    plt.xlabel("Community Structure")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def main() -> None:
    file_path = "data/river_civilizations.csv"

    summarize_project_direction()
    df = load_data(file_path)
    show_basic_info(df)
    analyze_settlement_and_food(df)
    visualize_food_storage(df)
    visualize_community_structure(df)


if __name__ == "__main__":
    main()
