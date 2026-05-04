# 🎓 Student Package Prediction 💰  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikitlearn)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![Accuracy](https://img.shields.io/badge/Model%20Accuracy-~90%25-brightgreen)  

A Machine Learning project that predicts a student’s **salary package (LPA)** based on their **CGPA** using **Simple Linear Regression**.  

---

## 🚀 Live Demo  

🌐 **Try the model here:**  
👉 https://obsolete-employee-equation.ngrok-free.dev/

---

## 📂 Project Structure  

---

## 📊 Dataset Details  

| Column  | Description |
|--------|------------|
| **cgpa** | Student's CGPA (Input Feature) |
| **package** | Salary Package in LPA (Target Variable) |

---

## 📈 Project Workflow  

### 1️⃣ Exploratory Data Analysis (EDA)
- Scatter plot of CGPA vs Package  
- Correlation analysis  
- Visualization using matplotlib & seaborn  

### 2️⃣ Linear Regression from Scratch  
- Custom class: `meralr`  
- Manual calculation of slope & intercept  

### 3️⃣ Scikit-Learn Model  
- Used `LinearRegression`  
- Compared with custom implementation  

### 4️⃣ Prediction  
- Input: CGPA  
- Output: Predicted Package  

---

## 🛠️ Tech Stack  

- Python  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- Scikit-learn  
- Ngrok  

---

## ⚙️ Installation  

```bash
git clone https://github.com/your-username/student-package-prediction.git
cd student-package-prediction
pip install numpy pandas matplotlib seaborn scikit-learn
jupyter notebook ML.ipynb

