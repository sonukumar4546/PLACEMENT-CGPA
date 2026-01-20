# Student Package Prediction 🎓💰

A Machine Learning project that implements **Simple Linear Regression** to predict the salary package of a student based on their CGPA. This project demonstrates how Linear Regression works under the hood by implementing the algorithm from scratch and comparing it with the standard Scikit-Learn implementation.

## 📂 Project Structure

- **`ML.ipynb`**: The Jupyter Notebook containing the data analysis, visualization, custom Linear Regression class, and model training.
- **`placementtohogyan.csv`**: The dataset used for training and testing the model.

## 📊 Dataset Details

The dataset (`placementtohogyan.csv`) contains simple academic and placement data:

| Column | Description |
| :--- | :--- |
| **cgpa** | Cumulative Grade Point Average (Independent Variable / Feature) |
| **package** | Salary Package in LPA (Dependent Variable / Target) |

## 🚀 Features & Methodology

1.  **Exploratory Data Analysis (EDA):**
    - Visualizing the relationship between CGPA and Package using `matplotlib` and `seaborn`.
    - Analyzing data shape and distribution.

2.  **Linear Regression from Scratch (`meralr`):**
    - Implementation of a custom Python class `meralr` to understand the mathematics behind the model.
    - Calculation of **Slope ($m$)** and **Intercept ($b$)** using closed-form formulas:
      $$m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$
      $$b = \bar{y} - m\bar{x}$$

3.  **Scikit-Learn Implementation:**
    - Training a standard `LinearRegression` model for performance comparison.

4.  **Prediction:**
    - Predicting package values for test data.

## 🛠️ Requirements

To run this project, you need Python installed along with the following libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
