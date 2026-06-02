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

##
<img width="822" height="461" alt="image" src="https://github.com/user-attachments/assets/455f933b-a6b8-4d90-86b9-7b973d96389a" />



---

# Part 2: Professional Presentation (Slide-by-Slide)

This structured layout can be used for a technical showcase slide deck, or written down directly as a formal design report.

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

## Slide 3: Visualizing the Data Transformation
### The Conceptual Workflow

Below is the structured data pipeline showing how a 1D sequence transforms step-by-step into structural calculations.

```text
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
