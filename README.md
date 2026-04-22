 📊 Exploratory Data Analysis and Health Indicator Prediction using NFHS-5 Dataset

📌 Project Overview

This project analyzes India's national health survey data using the **NFHS-5 (National Family Health Survey 2019–2021)** dataset.
It applies **data cleaning, exploratory data analysis (EDA), statistical analysis, and machine learning** to understand health patterns and predict survey outcomes across Indian states and union territories.



🎯 Objectives

* Analyze state-wise health and demographic indicators across India
* Study the relationship between household survey coverage and health outcomes
* Understand distribution patterns of key health indicators
* Perform advanced data visualization
* Build a predictive model for women interviewed based on households surveyed


📊 Key Insights

* 📈 Survey coverage is highly right-skewed — large states dominate the data
* 🏠 Households surveyed and women interviewed are perfectly correlated (r ≈ 1.0)
* 🩸 Significant variation in anaemia and nutrition indicators across states
* 🔗 Strong positive correlation between all survey count variables
* 🤖 Linear Regression model predicts women interviewed with near-perfect accuracy


🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy


📁 Project Structure

NFHS5-EDA-Project/
│
├── NFHS5_EDA_Analysis.ipynb      # Complete project notebook
├── NFHS_5_Factsheets_Data.xls    # NFHS-5 dataset
├── README.md                      # Project documentation
├── requirements.txt               # Required libraries


⚙️ Features

✔ Data cleaning and preprocessing
✔ State-wise health indicator analysis
✔ Advanced visualizations (histogram, bar chart, line plot, boxplot, pairplot, violin plot, regression plot, heatmap)
✔ Statistical analysis (correlation, hypothesis testing)
✔ Outlier detection
✔ Machine Learning model (Linear Regression)
✔ Health indicator prediction


📈 Visualizations Included

* Histogram – Distribution of Households Surveyed
* Bar Chart – Sum of Selected Indicators
* Line Plot – Trend of Households Surveyed Across Index
* Boxplot – Outlier Detection
* Pair Plot – Multi-variable Relationships
* Violin Plot – Density Distribution Analysis
* Regression Plot – Households Surveyed vs Women Interviewed
* Correlation Heatmap


🤖 Machine Learning

* Model: Linear Regression
* Input Feature: Number of Households Surveyed
* Target Variable: Number of Women age 15-49 years interviewed
* Evaluation Metrics:

  * Mean Squared Error (MSE)
  * R² Score


▶️ How to Run

1. Install required libraries:

pip install -r requirements.txt


2. Run the project:

jupyter notebook NFHS5_EDA_Analysis.ipynb


📌 Conclusion

This project demonstrates how data science techniques can be used to analyze national health survey data and predict health indicator outcomes. The results highlight the strong relationship between survey coverage and demographic health patterns across Indian states.


👨‍💻 Author

**Srikar Mourya Koppana**


🚀 Future Improvements

* Combine NFHS-4 and NFHS-5 data for time-series comparison
* Apply advanced ML models (Random Forest, XGBoost)
* Build interactive dashboards (Power BI / Streamlit)


⭐ If you like this project, give it a star!
