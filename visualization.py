import os
import textwrap

import matplotlib.pyplot as plt
import pandas as pd


def ensure_output_dir(output_dir="figures"):
    os.makedirs(output_dir, exist_ok=True)


def save_and_close(output_path):
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def normalize_food_storage(value):
    value = str(value).strip().lower()

    if value in ["granaries", "state storage", "stored surplus", "stored grain"]:
        return "Storage Present"
    elif value in ["none", "no storage", "not stored"]:
        return "No Storage"
    else:
        return "Other"


def plot_pipeline_overview(output_dir="figures"):
    ensure_output_dir(output_dir)

    steps = [
        "Environment\n(River / Floodplain)",
        "Food Production\n(Agriculture)",
        "Storage & Irrigation\n(Stability)",
        "Permanent\nSettlement",
        "Complex Community\n& Labor Division",
        "Political\nOrganization",
    ]

    fig, ax = plt.subplots(figsize=(14, 3))
    ax.axis("off")

    x_positions = [0.04, 0.21, 0.38, 0.55, 0.72, 0.89]
    y = 0.5

    for i, (x, step) in enumerate(zip(x_positions, steps)):
        ax.text(
            x,
            y,
            step,
            ha="center",
            va="center",
            fontsize=11,
            bbox=dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="white"),
            transform=ax.transAxes,
        )

        if i < len(x_positions) - 1:
            ax.annotate(
                "",
                xy=(x_positions[i + 1] - 0.07, y),
                xytext=(x + 0.07, y),
                xycoords=ax.transAxes,
                textcoords=ax.transAxes,
                arrowprops=dict(arrowstyle="->", lw=1.8),
            )

    plt.title("Ancient Civilization Development Pipeline", fontsize=14)
    save_and_close(os.path.join(output_dir, "pipeline_overview.png"))


def plot_environment_vs_settlement(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    cross_tab = pd.crosstab(df["environment_type"], df["settlement_type"])
    cross_tab.plot(kind="bar", figsize=(10, 6))

    plt.title("Environmental Conditions and Settlement Patterns")
    plt.xlabel("Environment Type")
    plt.ylabel("Number of Civilizations")
    plt.xticks(rotation=20, ha="right")

    save_and_close(os.path.join(output_dir, "environment_vs_settlement.png"))


def plot_settlement_vs_food(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    cross_tab = pd.crosstab(df["settlement_type"], df["food_source"])
    cross_tab.plot(kind="bar", stacked=True, figsize=(10, 6))

    plt.title("Permanent Settlements and Food Systems")
    plt.xlabel("Settlement Type")
    plt.ylabel("Number of Civilizations")
    plt.xticks(rotation=0)

    save_and_close(os.path.join(output_dir, "settlement_vs_food.png"))


def plot_food_system_overview(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    summary_df = pd.DataFrame({
        "Food Storage": df["food_storage"].apply(normalize_food_storage),
        "Irrigation": df["irrigation"],
        "Agriculture": df["agriculture"]
    })

    counts = {
        "Storage Present": (summary_df["Food Storage"] == "Storage Present").sum(),
        "Irrigation Present": (summary_df["Irrigation"].str.lower() == "yes").sum(),
        "Agricultural System Listed": summary_df["Agriculture"].notna().sum(),
    }

    pd.Series(counts).plot(kind="bar", figsize=(9, 6))

    plt.title("Food Stability Systems Across Civilizations")
    plt.xlabel("System")
    plt.ylabel("Count")
    plt.xticks(rotation=15, ha="right")

    save_and_close(os.path.join(output_dir, "food_system_overview.png"))


def plot_community_vs_labor(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    cross_tab = pd.crosstab(df["community_structure"], df["labor_division"])
    cross_tab.plot(kind="bar", stacked=True, figsize=(10, 6))

    plt.title("Community Structure and Labor Specialization")
    plt.xlabel("Community Structure")
    plt.ylabel("Number of Civilizations")
    plt.xticks(rotation=20, ha="right")

    save_and_close(os.path.join(output_dir, "community_vs_labor.png"))


def plot_civilization_profile(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    profile_df = pd.DataFrame({
        "Civilization": df["civilization"],
        "Permanent Settlement": df["settlement_type"].str.contains("Permanent", case=False).astype(int),
        "Storage Present": df["food_storage"].apply(
            lambda x: 1 if normalize_food_storage(x) == "Storage Present" else 0
        ),
        "Irrigation": df["irrigation"].str.lower().eq("yes").astype(int),
        "Developed Labor": df["labor_division"].str.contains("Developed", case=False).astype(int),
    })

    profile_df = profile_df.set_index("Civilization")
    ax = profile_df.plot(kind="bar", figsize=(11, 6))

    plt.title("Civilization Feature Profile")
    plt.xlabel("Civilization")
    plt.ylabel("Presence (0 = No, 1 = Yes)")
    plt.xticks(rotation=20, ha="right")
    plt.ylim(0, 1.2)
    ax.legend(loc="upper right")

    save_and_close(os.path.join(output_dir, "civilization_profile.png"))


def plot_civilization_summary_table(df, output_dir="figures"):
    ensure_output_dir(output_dir)

    fig, ax = plt.subplots(figsize=(14, 3.5))
    ax.axis("off")

    display_df = df[[
        "civilization",
        "environment_type",
        "settlement_type",
        "food_source",
        "community_structure",
        "political_structure",
    ]].copy()

    for col in display_df.columns:
        display_df[col] = display_df[col].apply(
            lambda x: "\n".join(textwrap.wrap(str(x), width=18))
        )

    table = ax.table(
        cellText=display_df.values,
        colLabels=[
            "Civilization",
            "Environment",
            "Settlement",
            "Food Source",
            "Community",
            "Political Structure",
        ],
        loc="center",
        cellLoc="center",
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.0)

    plt.title("Ancient Civilization Comparison Overview", pad=20)
    save_and_close(os.path.join(output_dir, "civilization_summary_table.png"))


def generate_all_figures(df, output_dir="figures"):
    plot_pipeline_overview(output_dir)
    plot_environment_vs_settlement(df, output_dir)
    plot_settlement_vs_food(df, output_dir)
    plot_food_system_overview(df, output_dir)
    plot_community_vs_labor(df, output_dir)
    plot_civilization_profile(df, output_dir)
    plot_civilization_summary_table(df, output_dir)

    print(f"\nSaved all figures to: {output_dir}/")
