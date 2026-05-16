# Module 2 Coding Exercises (Marimo Apps)

This repository contains interactive coding exercises for weeks 1 and 2 in **Code:You Data Analysis Module 2**.

Each week includes a **Marimo app** that guides you through exercises and allows you to check your work by revealing expected outputs.

---

## What This Is

Instead of completing exercises directly in TopHat, you will:

- Write your code in **your own environment (VS Code or Jupyter)**
- Use the Marimo apps to:
  - Read prompts
  - Reveal expected outputs
  - Check your work

You will **not see the answer code** — only what your output should match.

---

## Setup Instructions

### 1. Fork & Clone the Repository

```bash
git clone https://github.com/CodeYouOrg/DA_M2_CodingExercises
cd DA_M2_CodingExercises
```

### 2. Create exercise notebooks

```bash
touch w1_exercises.ipynb w2_exercises.ipynb
```

---

### 3. Install Required Package

You must install Marimo before running any exercises:
Windows:
```bash
pip install marimo
```
Mac/Linux:
```bash
pip3 install marimo
```

---

## How to Run the Exercises

Each week has its own `.py` file.

For example,  **Module 2 Week 1**, run:

```bash
marimo run m2w1_marimo.py
```

This will open the interactive app in your browser.

---

## How to Use the Exercises

For each exercise:

1. Read the prompt in the Marimo app
2. Copy the provided starter code into the exercise notebook you created
3. Write your solution
4. Run your code locally
5. Go back to the Marimo app
6. Click **"Show expected output"**
7. Compare your result

---

## Important Notes

- You should **NOT write code inside the Marimo app**
- All coding should happen in your own environment
- The Marimo app is only for:
  - Instructions
  - Expected outputs
  - Checking your work

---

## Weekly Structure


### Week 1
- Pandas: A Data Analyst’s Best Friend
- Clean & Tidy Data
- Data Wrangling Essentials

### Week 2
- Practice Questions - create bar, scatter, and histogram plots

---

## Troubleshooting

### If Marimo won’t run:
- Make sure you installed it:
  ```bash
  marimo --verson
  ```

### If you get errors:
- Make sure you're located in the project directory when you run the command:
  ```bash
  pwd
  ```

---

## Goal

The goal of these exercises is to help you:

- Build confidence using Pandas
- Practice real data manipulation tasks
- Learn how to debug and validate your own work

---

If something feels confusing or broken, ask questions in class! That’s part of the process.
