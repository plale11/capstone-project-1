from data_loader import load_civilization_data
from analysis import analyze_settlement, analyze_food_system, analyze_community
from visualization import plot_food_storage_grouped, plot_settlement_vs_food


def main():
    file_path = "data/civilizations.csv"

    df = load_civilization_data(file_path)

    analyze_settlement(df)
    analyze_food_system(df)
    analyze_community(df)

    plot_food_storage_grouped(df)
    plot_settlement_vs_food(df)


if __name__ == "__main__":
    main()