# Cognifyz Machine Learning Internship

## Author

**Satya Ranjan Pattanayak**  
B.Tech Computer Science & Engineering Student  
Nalanda Institute of Technology, Bhubaneswar

---

# Project Overview

This repository contains the Machine Learning internship tasks completed as part of the Cognifyz Technologies Internship Program.

The project focuses on data analysis, machine learning model development, classification, and recommendation systems using the Zomato Restaurant Dataset.

---

# Dataset Information

**Dataset:** Zomato Restaurant Dataset

**Total Records:** 9551

**Total Features:** 21

### Main Attributes

- Restaurant Name
- City
- Cuisines
- Average Cost for Two
- Price Range
- Aggregate Rating
- Votes
- Online Delivery
- Table Booking

---

# Task 1: Restaurant Rating Prediction

## Objective

Build a machine learning model to predict restaurant ratings based on restaurant characteristics.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

## Machine Learning Model

**Random Forest Regressor**

## Data Preprocessing

- Handled missing values
- Selected important features
- Encoded categorical variables
- Split dataset into training and testing sets

## Evaluation Metrics

- Mean Squared Error (MSE): **0.1022**
- R² Score: **0.9551**

## Result

The model achieved an **R² Score of 95.51%**, indicating excellent predictive performance.

## Feature Importance Analysis

The analysis revealed that **Votes** is the most influential factor affecting restaurant ratings.

### Key Insight

Restaurants with higher customer engagement and votes tend to receive better ratings.

---

# Task 2: Restaurant Recommendation System

## Objective

Develop a recommendation system that suggests restaurants based on user preferences.

## Features

- Cuisine-based recommendation
- Price range filtering
- Rating-based ranking
- Top restaurant suggestions

## User Input Example

### Preferred Cuisine

North Indian

### Preferred Price Range

3

## Recommendation Process

1. Filter restaurants based on cuisine preference.
2. Filter restaurants based on price range.
3. Sort restaurants according to aggregate rating.
4. Display top-rated matching restaurants.

## Sample Recommendations

- AB's - Absolute Barbecues
- Barbeque Nation
- Mirchi And Mime
- Kopper Kadai
- Rajasthan Al Malaki

## Result

The system successfully recommends highly rated restaurants that match user preferences.

---

# Task 3: Cuisine Classification

## Objective

Predict the primary cuisine category of a restaurant using machine learning techniques.

## Technologies Used

- Python
- Pandas
- Scikit-Learn

## Machine Learning Model

**Random Forest Classifier**

## Features Used

- Price Range
- Votes
- Aggregate Rating

## Data Preprocessing

- Removed missing cuisine values
- Extracted primary cuisine labels
- Encoded categorical target labels
- Split dataset into training and testing sets

## Result

### Accuracy

**22.52%**

## Observation

Cuisine prediction is a challenging multi-class classification problem because multiple cuisines often share similar ratings, vote counts, and pricing characteristics.

---

# Libraries Used

- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

# Project Structure

```text
Cognifyz-ML-Internship
│
├── Dataset.csv
├── README.md
├── task1.py
├── task2.py
├── task3.py
│
├── outputs
│   └── feature_importance.png
│
├── .gitignore
│
└── venv
```

---

# Future Improvements

- Advanced Content-Based Recommendation System
- Collaborative Filtering
- Deep Learning Models
- Restaurant Similarity Search
- Interactive Dashboard
- Streamlit Web Application Deployment
- Real-Time Recommendation Engine

---

# Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Classification
- Regression
- Recommendation Systems
- Model Evaluation
- Data Visualization

---

# Internship Details

**Organization:** Cognifyz Technologies

**Domain:** Machine Learning

**Duration:** June 2026 – July 2026

---

# Results Summary

| Task | Project | Result |
|--------|----------|----------|
| Task 1 | Restaurant Rating Prediction | R² Score = 0.9551 |
| Task 2 | Restaurant Recommendation System | Successfully Implemented |
| Task 3 | Cuisine Classification | Accuracy = 22.52% |

---

# Author

**Satya Ranjan Pattanayak**

Machine Learning Enthusiast | Android Developer | Web Developer

### Connect With Me

- LinkedIn: [Satya Ranjan Pattanayak](https://www.linkedin.com/in/satya-ranjan-pattanayak-976189302/)
- GitHub: [drsatyaranjan01-crypto](https://github.com/drsatyaranjan01-crypto)

---

⭐ If you found this project useful, consider giving it a star.