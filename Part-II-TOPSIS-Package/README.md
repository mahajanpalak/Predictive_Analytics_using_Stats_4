# 📦 Topsis-Palak-102497010  
*A Python Package for Multi-Criteria Decision Making using TOPSIS*

---

## 📖 Overview

This project is developed as part of an academic assignment to **create, package, and publish a Python library on PyPI** implementing the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method.

The package allows users to rank alternatives based on multiple criteria using a **command-line interface**, following proper software packaging standards.

---

## 🎯 Assignment Objectives

This project fulfills the following requirements:

- Develop a Python package implementing TOPSIS
- Follow the naming convention: `Topsis-FirstName-RollNumber`
- Upload the package to **pypi.org**
- Provide a **User Manual**
- Test installation and execution via command line
- Document methodology, usage, and results clearly

---

## 📌 Package Information

- **Package Name:** Topsis-Palak-102497010  
- **Version:** 1.0.1  
- **Platform:** PyPI  
- **Execution Mode:** Command Line  

---

## 🧠 About TOPSIS Methodology

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** technique used to rank alternatives by comparing their distances from:

- **Ideal Best Solution**
- **Ideal Worst Solution**

### Core Idea:
The best alternative should:
- Have the **minimum distance from the ideal best**
- Have the **maximum distance from the ideal worst**

---

## 🧮 Methodology Implemented

The package follows the standard TOPSIS methodology:

### Step 1: Input Decision Matrix
- Rows represent alternatives
- Columns represent criteria

---

### Step 2: Normalize the Decision Matrix
Each value is normalized using vector normalization:

```
rij = xij / √(Σ xij²)
```

This removes scale differences among criteria.

---

### Step 3: Apply Weights
Each normalized value is multiplied by its corresponding weight:

```
vij = rij × wj
```

This reflects the importance of each criterion.

---

### Step 4: Determine Ideal Best and Ideal Worst
- For **positive (+)** impact → higher value is better
- For **negative (-)** impact → lower value is better

---

### Step 5: Calculate Separation Measures

Distance from Ideal Best:
```
Si+ = √ Σ (vij − vj+)²
```

Distance from Ideal Worst:
```
Si− = √ Σ (vij − vj−)²
```

---

### Step 6: Calculate TOPSIS Score

```
Ci = Si− / (Si+ + Si−)
```

- Higher `Ci` → Better alternative

---

### Step 7: Ranking
Alternatives are ranked in descending order of TOPSIS score.

---

## 📦 Package Structure

```
Topsis-Palak-102497010/
│
├── setup.py
├── README.md
├── __init__.py
├── topsis.py
└── screenshots/
    ├── pypi_page.png
    ├── pip_install.png
    └── package_execution.png
```

---

## 🛠 Installation Guide (User Manual)

Install the package directly from PyPI:

```bash
pip install topsis_palak_102497010
```

---

## 🖥️ Command Line Usage

### Syntax
```bash
python -m topsis <InputFile> <Weights> <Impacts> <OutputFile>
```

### Example
```bash
python -m topsis data.xlsx "1,1,1,2,2" "+,+,-,+,-" result.xlsx
```

---

## 📂 Input File Requirements

- Minimum **3 columns**
- First column → Alternative names
- Remaining columns → Numeric values only
- Weights must be comma-separated numbers
- Impacts must be `+` or `-`
- Number of weights = Number of criteria
- Number of impacts = Number of criteria

---

## 📊 Output Description

The output file contains:
- Original input data
- **TOPSIS Score**
- **Rank**

Higher TOPSIS score indicates better performance.

---

## ✅ Validation & Error Handling

The package validates:

✔ Correct number of arguments  
✔ File existence  
✔ Numeric criteria values  
✔ Matching weights and impacts count  
✔ Valid impact symbols (`+` or `-`)  
✔ Proper comma-separated inputs  

Clear error messages are shown for invalid inputs.

---

## 📸 Screenshots (Proof of Execution)

### PyPI Package Page
![PyPI Page](screenshots/pypi_page.png)

### Package Installation
![Pip Install](screenshots/pip_install.png)

### Command Line Execution
![Execution](screenshots/package_execution.png)

---

## 🧪 Testing

The package was tested by:
- Installing from PyPI
- Running via command line
- Verifying output generation
- Checking ranking correctness

---

## 🧰 Technologies Used

- Python 3.x
- Pandas
- NumPy
- OpenPyXL
- setuptools
- twine

---

## 📌 Conclusion

This project successfully demonstrates:
- Development of a Python package
- Publishing to PyPI
- Command-line execution
- Proper documentation and testing
- Correct implementation of TOPSIS methodology

All assignment requirements have been fulfilled.

---

## 👩‍🎓 Author

**Palak**  


