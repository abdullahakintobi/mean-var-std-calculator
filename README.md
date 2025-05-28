# Mean-Variance-Standard Deviation Calculator

A Python project that calculates statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix using NumPy.

## 📋 Project Description

This project implements a statistical calculator that takes a list of 9 numbers, converts it into a 3x3 NumPy array, and computes various statistical measures along different axes:
- **Axis 0**: Statistics calculated along columns (vertical)
- **Axis 1**: Statistics calculated along rows (horizontal)  
- **Overall**: Statistics calculated for the entire matrix as a single value

## 🚀 Features

- **Mean calculation** along columns, rows, and overall matrix
- **Variance calculation** for all three orientations
- **Standard deviation** computation
- **Maximum and minimum** value identification
- **Sum calculation** across different axes
- **Input validation** with appropriate error handling
- **Elegant implementation** using NumPy's getattr() for dynamic method calling

## 📁 Project Structure

```
mean-var-std-calculator/
├── mean_var_std.py    # Main implementation file
├── main.py           # Test runner and development file
├── test_module.py    # Unit tests
└── README.md         # Project documentation
```

## 🛠️ Requirements

- Python 3.x
- NumPy

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/abdullahakintobi/mean-var-std-calculator.git
cd mean-var-std-calculator
```

2. Install required dependencies:
```bash
pip install numpy
```

## 💻 Usage

### Basic Usage

```python
from mean_var_std import calculate

# Example usage
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

### Expected Output Format

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.667, 0.667, 0.667], 6.667],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.582],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## 🧪 Testing

Run the tests using:

```bash
python3 main.py
```

This will execute both your code and the unit tests from `test_module.py`.

## ⚠️ Error Handling

The function includes input validation:
- Raises `ValueError` if the input list contains fewer than 9 elements
- Error message: "List must contain nine numbers."

## 🔍 Function Specification

### `calculate(list)`

**Parameters:**
- `list` (list): A list containing exactly 9 numerical values

**Returns:**
- `dict`: Dictionary containing statistical calculations with the following structure:
  - Each key maps to a list with three elements: [axis0_result, axis1_result, overall_result]

**Raises:**
- `ValueError`: When input list contains fewer than 9 elements

## 🎯 Example

```python
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Represents the 3x3 matrix:
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
# Returns statistical measures along columns, rows, and overall matrix
```

## 🚫 Academic Integrity Disclaimer

**⚠️ IMPORTANT NOTICE:**

This repository contains reference code for educational purposes only. If you are working on this project as part of a course, certification program, or academic assignment:

- **DO NOT** copy this code directly for your submissions
- **DO NOT** use this code to complete course requirements or certifications
- **USE** this code only as a learning reference to understand concepts and approaches

**Remember:** The goal of educational projects is to learn and demonstrate your understanding, not to submit someone else's work.

---

**Note:** This project is part of the freeCodeCamp Data Analysis with Python certification curriculum.
