# Mean-Variance-Standard Deviation Calculator

This is an implementation of the Mean-Variance-Standard Deviation Calculator project, part of the freeCodeCamp **Data Analysis with Python Certification** curriculum. 

The project showcases the use of **NumPy** to process lists of numbers, reshape them into multi-dimensional arrays, and perform structured matrix calculations along different dimensions (axes).

---

## Project Specifications

The goal is to create a function named `calculate()` in `mean_var_std.py` that outputs the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

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

├── main.py          # Code runner and entry point for verification
├── mean_var_std.py  # Core solution containing the calculation algorithm
├── test_module.py   # Unit test suite provided by freeCodeCamp
└── README.md        # Documentation

---

## Local Verification & Usage

To run the script and execute the automated test module locally, run the following command in your terminal:

python3 main.py

### Example Input
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

### Example Output
{
  "mean": [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  "variance": [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  "standard deviation": [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  "max": [[6, 7, 8], [2, 5, 8], 8],
  "min": [[0, 1, 2], [0, 3, 6], 0],
  "sum": [[9, 12, 15], [3, 12, 21], 36]
}

## Technologies Used
* **Python 3**
* **NumPy** (Numerical Python Library)
* **Unittest** (Built-in Python Testing Framework)

---

# Professional Project Presentation

## Slide 1: Title & Overview
### Matrix Statistical Analysis Engine
* **Context:** freeCodeCamp Data Analysis with Python Portfolio
* **Core Objective:** Design an automated pipeline capable of converting flat raw numerical arrays into fully matrix-computed statistical summaries.

---

## Slide 2: The Problem Statement
### The Challenges of Dimensional Data
* Raw incoming pipeline data is unstructured, flat, and hard to extract deep trends from.
* We must process statistical information in three separate spatial dimensions:
  1. Vertical Trends (Columns)
  2. Horizontal Trends (Rows)
  3. Global Trends (The entire dataset combined)

---

## Slide 3: Illustrating the Data Transformation
### The Conceptual Workflow

Below is the structured data pipeline showing how a 1D sequence transforms step-by-step into structural calculations.

[ Raw 1D Input List ] 
         │  
         ▼ (Length Check: Must equal 9)
[ Array Reshaping ] ───► Transforms to 3x3 Grid Matrix
         │  
         ├─► Axis 0 Operations (Compute downwards per Column ↓)
         ├─► Axis 1 Operations (Compute across per Row ──►)
         └─► Flattened Operations (Compute all combined █)
         │
         ▼ (.tolist() Conversion)
[ Structured Dictionary Report Output ]

---

## Slide 4: Mathematical Execution Mapping
### Understanding Matrix Axises (3 x 3 Sample Mapping)

When an input list like [0, 1, 2, 3, 4, 5, 6, 7, 8] is transformed, it forms this structural matrix layout:

|          | Column 1 | Column 2 | Column 3 | Axis 1 (Row-wise Direction) |
|:--------:|:--------:|:--------:|:--------:|:---------------------------:|
|  Row 1   |    0     |    1     |    2     |    Calculate Row 1 (->)     |
|  Row 2   |    3     |    4     |    5     |    Calculate Row 2 (->)     |
|  Row 3   |    6     |    7     |    8     |    Calculate Row 3 (->)     |
|  Axis 0  |Calculate |Calculate |Calculate | Flattened: Calculate all 9  |
| (Col-wise|  Col 1   |  Col 2   |  Col 3   |  elements together (all)    |
|Direction)|   (v)    |   (v)    |   (v)    |                             |

---

## Slide 5: The Algorithmic Solution
### Modular Structural Architecture
* **Validation Layer:** Guard clause verifies len(list) == 9. If validation fails, safely reject and drop the execution context immediately via ValueError.
* **Vectorization Layer:** Convert input to native NumPy matrix array configurations to run operations in compiled C-speed environments rather than slow vanilla Python loops.
* **Extraction Helpers:** Internal nested abstraction modules process computations concurrently across designated axes.
* **Serialization Layer:** Matrix objects are flattened back down into standard types via native .tolist() processing to guarantee system interoperability.

---

## Slide 6: Summary & Core Takeaways
### Why This Architectural Approach Works
* **Scale-Ready Vectorization:** Utilizing NumPy functions avoids nested for loops, improving computational performance.
* **Deterministic Output:** Structuring data cleanly inside JSON/Dictionary formats makes it highly readable and ready for external APIs or front-end consumption layers.
* **Defensive Design:** Explicit input validation protects downstream analytical pipelines from processing malformed datasets.
