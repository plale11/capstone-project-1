from data_loader import load_civilization_data
from analysis import run_all_analysis
from visualization import generate_all_figures


def main():
    file_path = "data/civilizations.csv"
    df = load_civilization_data(file_path)

    run_all_analysis(df)
    generate_all_figures(df, output_dir="figures")


if __name__ == "__main__":
    main()
