# Dataset documentation

## Source

This project uses `insurance.csv`, commonly published as the **Medical Cost
Personal Datasets** dataset:

- Kaggle page: <https://www.kaggle.com/datasets/mirichoi0218/insurance>
- Kaggle publisher: M. Choi (`mirichoi0218`)
- Commonly attributed origin: Brett Lantz, *Machine Learning with R*, Packt
  Publishing, 2013

Download the data file directly from the Kaggle page, extract `insurance.csv`,
and place it at:

```text
data/insurance.csv
```

The MIT license in this repository applies only to the original code and
documentation. The dataset remains subject to the terms stated by its
publisher.

## Contents

The downloaded file contains 1,338 rows and seven columns. Each row represents
one insurance record.

| Column | Description |
|---|---|
| `age` | Age in years |
| `sex` | Sex category recorded in the source data |
| `bmi` | Body mass index |
| `children` | Number of dependent children represented in the record |
| `smoker` | Smoking-status category (`yes` or `no`) |
| `region` | US residential region |
| `charges` | Annual individual medical charges billed by health insurance |

## Responsible interpretation

This is a small educational dataset, not a representative clinical cohort.
Its collection period, sampling method, and wider population are not fully
documented on the distribution page. Therefore:

- Describe patterns as **associations**, not causes.
- Do not use the data to make clinical, insurance, or individual decisions.
- Do not assume that the categories reflect every relevant identity or risk
  factor.
- Do not generalize results to another country, health system, or population.
- Do not add identifiable patient or research-participant data to this public
  repository.
