# TOPSIS Implementation 

This repository contains a complete implementation of the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method across three parts — a command-line program, a PyPI package, and a Flask web service.

---

## Structure
```
├── Part-I-TOPSIS-CLI/        - Command-line TOPSIS implementation
├── Part-II-TOPSIS-Package/        - TOPSIS Python package (PyPI)
├── TOPSIS-WEB-SERVICE/        - TOPSIS Flask web service

```

---

## Part I – Command Line Program

Implements TOPSIS as a command-line Python program.

### Usage
```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example
```bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv
```

### Validations
- Correct number of parameters must be provided (`inputFileName`, `Weights`, `Impacts`, `resultFileName`).
- Handles `File Not Found` exception with appropriate messages.
- Input file must contain three or more columns.
- Columns from 2nd to last must contain numeric values only.
- Number of weights, impacts, and columns (2nd to last) must be equal.
- Impacts must be either `+` or `-` only.
- Weights and impacts must be separated by `,` (comma).

---

## Part II – PyPI Package

A Python package built and published to [PyPI](https://pypi.org).

### Naming Convention
```
Topsis-FirstName-RollNumber
```

### Installation
```bash
pip install Topsis-FirstName-RollNumber
```

### Usage
```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example
```bash
topsis data.csv "1,1,1,2" "+,+,-,+" output-result.csv
```

### Features
- Installable via `pip`
- Full user manual included
- Tested via command line after installation
- Reference: [Sample PyPI Package](https://pypi.org/project/topsis-3283/)

---

## Part III – Web Service

A Flask-based web application for TOPSIS where users upload a decision matrix and receive results via email.

### Features
- Upload Excel decision matrix
- Enter weights and impacts via web form
- Automatic email delivery of `result.xlsx`
- Input validation for weights, impacts, and email format


### Validations
- Number of weights must equal number of impacts.
- Impacts must be either `+` or `-` only.
- Weights and impacts must be separated by `,` (comma).
- Email must be in a valid format.

---

## Tech Stack

| Part | Technology |
|------|------------|
| Part I | Python, pandas, numpy |
| Part II | Python, PyPI, setuptools |
| Part III | Python, Flask, pandas, openpyxl |

---

## Author
Palak

> 📌 Each assignment folder contains its own detailed README with setup instructions, screenshots, and examples.
