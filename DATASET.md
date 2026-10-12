# Dataset documentation

## Source

This repository includes `data/insurance.csv`, commonly published as the
**Medical Cost Personal Datasets** dataset:

- Kaggle page: <https://www.kaggle.com/datasets/mirichoi0218/insurance>
- Kaggle publisher: M. Choi (`mirichoi0218`)
- Commonly attributed origin: Brett Lantz, *Machine Learning with R*, Packt
  Publishing, 2013

The data file is redistributed for education with attribution. The MIT license
in this repository applies to the original code and documentation, not to
third-party data. The dataset remains subject to the terms stated by its
original publisher.

## Contents

The file contains 1,338 rows and seven columns. Each row represents one
insurance record.

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
