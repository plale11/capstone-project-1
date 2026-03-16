def analyze_settlement(df):
    print("\n=== Settlement Types ===")
    settlement_counts = df["settlement_type"].value_counts()
    print(settlement_counts)

    print("\nInterpretation:")
    print(
        "Settlement type shows whether societies became permanent communities "
        "rather than remaining mobile hunter-gatherer groups."
    )


def analyze_food_system(df):
    print("\n=== Food Sources ===")
    food_source_counts = df["food_source"].value_counts()
    print(food_source_counts)

    print("\n=== Food Storage Systems ===")
    food_storage_counts = df["food_storage"].value_counts()
    print(food_storage_counts)

    print("\n=== Irrigation Systems ===")
    irrigation_counts = df["irrigation"].value_counts()
    print(irrigation_counts)

    print("\nInterpretation:")
    print(
        "Food production, storage, and irrigation reveal how early civilizations "
        "moved beyond simple subsistence and developed stable agricultural systems."
    )


def analyze_community(df):
    print("\n=== Community Structures ===")
    community_counts = df["community_structure"].value_counts()
    print(community_counts)

    print("\n=== Labor Division ===")
    labor_counts = df["labor_division"].value_counts()
    print(labor_counts)

    print("\nInterpretation:")
    print(
        "Community structure and labor division suggest increasing social complexity, "
        "cooperation, and organization in early civilizations."
    )


def run_all_analysis(df):
    print("\n==============================")
    print(" Ancient Civilization Analysis ")
    print("==============================")

    analyze_settlement(df)
    analyze_food_system(df)
    analyze_community(df)

    print("\n=== Overall Insight ===")
    print(
        "The dataset suggests that early river civilizations developed through a process "
        "of permanent settlement, agricultural production, food surplus storage, "
        "and increasingly organized community life."
    )
