# Mean-Variance-Standard Deviation Calculator

This is an implementation of the Mean-Variance-Standard Deviation Calculator project, part of the freeCodeCamp **Data Analysis with Python Certification** curriculum. 

The project showcases the use of **NumPy** to process lists of numbers, reshape them into multi-dimensional arrays, and perform structured matrix calculations along different dimensions (axes).

---

## Project Specifications

The goal is to create a function named `calculate()` in `mean_var_std.py` that outputs the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a $3 \times 3$ matrix.

### Input
* A Python list containing exactly **9 numbers**.

### Output
* A dictionary containing calculations mapped across three states:
  1. **Axis 0:** Calculations performed column-wise.
  2. **Axis 1:** Calculations performed row-wise.
  3. **Flattened:** Calculations performed across all elements mixed together.

### Error Handling
* If a list containing fewer or more than 9 elements is passed, the function raises a `ValueError` exception with the message: `"List must contain nine numbers."`.

---
## Project Structure

```text
├── main.py          # Code runner and entry point for verification
├── mean_var_std.py  # Core solution containing the calculation algorithm
├── test_module.py   # Unit test suite provided by freeCodeCamp
└── README.md        # Documentation
