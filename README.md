# E-Commerce Data Analysis & Dashboard

## Live Dashboard
https://louiee-jason-ecommerce-dashboard-analysis.streamlit.app/

## Description
This project aims to analyze an e-commerce dataset to understand transaction patterns, product category performance, and customer payment preferences. The analysis includes data cleaning, exploratory data analysis (EDA), visualization, and RFM analysis. The results are presented through an interactive dashboard built using Streamlit.

## Key Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Revenue trend analysis
- Product category analysis
- Payment method analysis
- RFM analysis for customer segmentation
- Interactive dashboard using Streamlit

## Technologies Used
- Python
- Pandas
- Matplotlib
- Streamlit

## Environment Setup

### Using Conda
conda create --name main-ds python=3.9  
conda activate main-ds  
pip install -r requirements.txt  

### Using Pipenv
pip install pipenv  
pipenv install  
pipenv shell  
pip install -r requirements.txt  

## Run the Dashboard
streamlit run dashboard/dashboard.py  

## Project Structure
submission/
├── dashboard/
│   ├── dashboard.py
│   └── clean_data.csv
├── data/
│   ├── raw datasets
├── notebook.ipynb
├── README.md
└── requirements.txt

## Key Insights
- Revenue increased significantly and peaked at the end of 2017  
- Sales are dominated by a few main product categories  
- Credit card is the most commonly used payment method  
- Most customers only make a single transaction  