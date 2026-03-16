def analyze_settlement(df):
    print("\nSettlement Types")
    print(df["settlement_type"].value_counts())


def analyze_food_system(df):
    print("\nFood Sources")
    print(df["food_source"].value_counts())

    print("\nFood Storage")
    print(df["food_storage"].value_counts())


def analyze_community(df):
    print("\nCommunity Structure")
    print(df["community_structure"].value_counts())

    print("\nLabor Division")
    print(df["labor_division"].value_counts())
