"""Explore the Medical Cost Personal dataset and create a simple chart.

Run it from the repository folder: python3 scripts/main.py The starting version
works completely; the TODO comments identify safe places to experiment.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent  # the repository folder, one level above scripts/
DATA_PATH = PROJECT_ROOT / "data" / "insurance.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "charges_by_smoking.png"


def load_data() -> pd.DataFrame:
    """Load the locally downloaded CSV file into a pandas DataFrame."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Dataset not found. Make a folder named data next to scripts/, "
            "download insurance.csv from the Kaggle link in README.md, "
            "and put it there: data/insurance.csv"
        )
    return pd.read_csv(DATA_PATH)


def inspect_data(data: pd.DataFrame) -> None:
    """Print a few checks that help us understand the dataset."""
    print("Dataset shape (rows, columns):", data.shape)
    print("\nColumn names:")
    print(list(data.columns))
    print("\nFirst five rows:")
    print(data.head())

    # TODO 1: What else would help you assess data quality?
    # Try printing data.dtypes, data.isna().sum(), or data.describe().


def summarize_data(data: pd.DataFrame) -> pd.Series:
    """Calculate mean insurance charges for each smoking category."""
    summary = data.groupby("smoker")["charges"].mean()

    # TODO 2: Change the question.
    # For example, group by "region" instead of "smoker", or summarize "bmi"
    # instead of "charges". Update the chart labels when you do this.
    return summary


def create_chart(summary: pd.Series) -> None:
    """Display the summary as a bar chart and save it as a PNG file."""
    plt.figure(figsize=(8, 5))
    summary.plot(kind="bar", color="steelblue")

    plt.title("Average insurance charges by smoking status")
    plt.xlabel("Smoking status")
    plt.ylabel("Average annual charges")
    plt.xticks(rotation=0)
    plt.tight_layout()

    # TODO 3: Make one visible change: title, color, labels, or chart type.

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    plt.savefig(OUTPUT_PATH, dpi=150)
    plt.show()
    plt.close()


def main() -> None:
    """Run the complete data exploration workflow."""
    data = load_data()
    inspect_data(data)

    summary = summarize_data(data)
    print("\nAverage charges by smoking status:")
    print(summary.round(2))

    create_chart(summary)
    print(f"\nSaved chart to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
