# E-Commerce Data Analysis & Dashboard

This project aims to analyze an e-commerce dataset to understand transaction patterns, product category performance, and customer payment preferences. The analysis includes data cleaning, exploratory data analysis (EDA), visualization, and RFM analysis. The results are presented through an interactive dashboard built using Streamlit.

Key features of this project include data cleaning and preprocessing, revenue trend analysis, product category analysis, payment method analysis, and customer segmentation using RFM analysis.

Technologies used in this project are Python, Pandas, Matplotlib, and Streamlit.

To run the dashboard, first install the required dependencies using:
pip install -r requirements.txt

Then run the following command:
streamlit run dashboard/dashboard.py

Project structure:
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── raw datasets
├── notebook.ipynb
├── README.md
└── requirements.txt

Key insights obtained from this analysis:
- Revenue increased significantly and peaked at the end of 2017
- Sales are dominated by a few main product categories
- Credit card is the most commonly used payment method
- Most customers only make a single transaction
