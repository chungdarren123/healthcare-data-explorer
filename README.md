# Healthcare Data Explorer

A small, beginner-friendly Python project for exploring a public health
insurance dataset with **pandas** and **Matplotlib**. It is the starter
repository for Coding for Healthcare Session 2: a real development environment
and AI-assisted data exploration.

The supplied program provides a working baseline once you download the dataset
from Kaggle. Run it first, then use the `TODO` comments in `scripts/main.py` to make
small changes and immediately see their effect in the terminal and the
generated chart.

> **Educational use only.** This project is not clinical software and its
> output must not be used for healthcare or insurance decisions. Never add real
> patient or research-participant data to this repository.

## Research question

How are annual insurance charges distributed, and how do the recorded charges
differ across observable categories such as smoking status and region?

This project explores associations. It does not establish that any variable
causes a change in insurance charges.

## What you will practice

- Opening and navigating a repository in VS Code
- Running a Python script locally
- Creating a project-specific Python environment
- Installing dependencies from `requirements.txt`
- Loading and inspecting a CSV file with pandas
- Summarizing tabular data
- Displaying and saving a chart with Matplotlib
- Using GitHub Copilot Chat for focused assistance
- Reviewing and committing changes with Git

## Repository structure

```text
healthcare-data-explorer/
├── scripts/
│   └── main.py             # Working analysis with student TODOs
├── outputs/
│   └── .gitkeep            # Keeps the initially empty folder in Git
├── .gitignore              # Files Git should not track
├── CONTRIBUTING.md         # How others can contribute
├── DATASET.md              # Data provenance and limitations
├── LICENSE                 # License for original code and documentation
├── README.md               # Project purpose and instructions
└── requirements.txt        # Required Python packages

data/                       # You create this folder; Git never tracks it
└── insurance.csv           # Downloaded from Kaggle
```

## Requirements

- Python 3
- Git
- Visual Studio Code
- The Microsoft Python extension for VS Code
- A GitHub account for GitHub Copilot Chat
- A free Kaggle account to download the dataset

VS Code and its Python extension do not include the Python interpreter. Python
must also be installed on your laptop.

## Getting started

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/chungdarren123/healthcare-data-explorer.git
cd healthcare-data-explorer
```

Then open the `healthcare-data-explorer` folder in VS Code using **File → Open
Folder**.

If cloning is unavailable during the workshop, download the repository ZIP,
extract it, and open the extracted folder. Git history is not included in that
fallback workflow.

### 2. Download the dataset from Kaggle

Download the dataset from the publisher as part of the project setup:

1. Open the [Medical Cost Personal Datasets page on
   Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).
2. Sign in to Kaggle if prompted, then select **Download**.
3. Open the downloaded ZIP file and extract `insurance.csv`.
4. In the VS Code Explorer, right-click the repository folder → **New Folder** → name it `data`.
5. Drag `insurance.csv` from your Downloads folder onto `data`.

The final path must be:

```text
healthcare-data-explorer/data/insurance.csv
```

The whole `data/` folder is excluded from version control, so the dataset
never reaches GitHub. Keep the original filename so that `scripts/main.py` can
locate it.

### 3. Create the Python environment

In VS Code:

1. Open the Command Palette (`Ctrl+Shift+P` on Windows or `Cmd+Shift+P` on
   macOS).
2. Run **Python: Create Environment**.
3. Choose **Venv**.
4. Choose your installed Python interpreter.
5. Select `requirements.txt` when asked which dependencies to install.

VS Code should create a `.venv` folder and select it for this project. The
`.venv` folder is intentionally excluded from Git because every contributor
can recreate it from `requirements.txt`.

The same thing from the terminal, in the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
```

### 4. Run the baseline

In the terminal, from the repository folder:

```bash
python3 scripts/main.py
```

Or open `scripts/main.py` and select **Run Python File in Terminal** from the
top-right of the editor.

The program should:

1. Print the dataset shape, columns, and first five rows.
2. Print mean charges by smoking status.
3. Save `outputs/charges_by_smoking.png`.
4. Display the chart in a graphical window.

You may need to close the chart window before the script finishes.

## Exercises

Always rerun the program after one small change. Use the terminal output and
saved chart as evidence that the change worked.

### TODO 1 — Inspect data quality

Add one or more checks inside `inspect_data`:

```python
print(data.dtypes)
print(data.isna().sum())
print(data.describe())
```

Explain what the output tells you about the data.

### TODO 2 — Ask a different question

Modify `summarize_data`. Possibilities include:

- Mean charges by region
- Mean BMI by smoking status
- Number of records in each region

Update the printed description and chart labels so they still describe the
calculation accurately.

### TODO 3 — Make a visible change

Change one or more of:

- Chart title
- Bar color
- Axis labels
- Figure size
- Chart type

Open the saved PNG after each run and check that the result matches your code.

## Using GitHub Copilot Chat

Ask for one focused change at a time. Provide the relevant variable and column
names, then verify the result yourself.

Example prompts:

> Explain `summarize_data` line by line for someone who knows basic Python. Do
> not change any files.

> The DataFrame is named `data`. Help me calculate average charges by region.
> Change only `summarize_data` and explain the change.

> Explain this exact error and suggest one thing to check first: [paste error].

Do not paste patient information, research-participant data, passwords, API
keys, or other sensitive material into Copilot Chat.

## Save a Git checkpoint

First inspect the changes:

```bash
git status
git diff
```

Stage the files intentionally and commit them:

```bash
git add scripts/main.py
git add outputs/charges_by_smoking.png
git commit -m "Add insurance charge analysis and visualization"
git status
```

Saving a file is not the same as committing it, and committing locally does not
upload the commit to GitHub.

## Troubleshooting

### Python is not available

Close and reopen VS Code after installing Python. Then run **Python: Select
Interpreter** and choose the installed interpreter or `.venv`.

### `ModuleNotFoundError`

Confirm that `.venv` is selected in VS Code and that the dependencies from
`requirements.txt` were installed into it.

### `FileNotFoundError`

Confirm that `data/insurance.csv` exists and that you opened the repository
folder rather than only opening `scripts/main.py`. If it is missing, complete the
Kaggle download steps above and check that the file was not left inside the ZIP
archive or placed in an extra nested folder.

### The chart does not appear

Check whether `outputs/charges_by_smoking.png` was created. The saved PNG is the
authoritative output even if a graphical chart window cannot open.

### Git will not commit

Git may ask you to configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Use an email address you are comfortable associating with your local commits.

## Data and license

Read [`DATASET.md`](DATASET.md) for download instructions, provenance, fields,
and limitations. The MIT license applies only to this repository's original
code and documentation. The dataset remains subject to the terms stated by its
publisher.
