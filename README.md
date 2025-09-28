# Black Friday Sales Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)](https://matplotlib.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple data visualization dashboard for Black Friday sales analysis using Python and Matplotlib.

##  Overview

This project analyzes Black Friday retail data and creates a dashboard with 6 different charts to show business insights.

##  Features

The dashboard includes:

1. **Gender Distribution** - Bar chart showing male vs female shoppers
2. **Age Group Analysis** - Pie chart with age group percentages
3. **Purchase Amount Distribution** - Histogram showing spending patterns
4. **Product Category Performance** - Scatter plot of average purchase by category
5. **Top Occupations by Spending** - Horizontal bar chart of highest spending occupations
6. **City Category Analysis** - Bar chart showing total purchases by city tier

##  Dataset

- **Source:** [Kaggle - Black Friday Sales Dataset](https://www.kaggle.com/datasets/rajeshrampure/black-friday-sale)
- **File:** BlackFriday.csv
- **Size:** ~550,000 records
- **Columns:** 12 features (User_ID, Product_ID, Gender, Age, Occupation, City_Category, etc.)

##  Installation

`ash
pip install pandas matplotlib numpy
`

##  Quick Start

1. **Clone the repository:**
`ash
git clone https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib.git
cd blackfriday-sales-analysis-matplotlib
`

2. **Install dependencies:**
`ash
pip install pandas matplotlib numpy
`

3. **Download the dataset:**
   - Download BlackFriday.csv from [Kaggle](https://www.kaggle.com/datasets/rajeshrampure/black-friday-sale)
   - Place it in the project root directory

4. **Run the analysis:**
`ash
python BlackFriday.ipynb
`

> **Note:** Despite the .ipynb extension, this is a Python script that can be run directly

##  Project Structure

`
blackfriday-sales-analysis-matplotlib/
 BlackFriday.ipynb          # Main analysis script
 BlackFriday.csv            # Dataset (download from Kaggle)
 dashboard_blackfriday.png  # Generated dashboard image
 .gitignore
 LICENSE
 README.md
`

##  Dashboard Output

The script generates a high-resolution dashboard image (dashboard_blackfriday.png) with:
- **Size:** 2012 inches at 150 DPI
- **Layout:** 2 rows  3 columns grid
- **Format:** PNG with professional styling

##  Key Insights

The dashboard shows:
- Customer demographics (gender, age, occupation)
- Spending patterns and purchase behavior
- Product category performance
- Geographic distribution across city tiers

##  Code Features

- **Data Cleaning:** Automatic handling of missing values
- **Professional Visualization:** High-quality plots with proper styling
- **Export Functionality:** Saves dashboard as PNG image
- **Customizable:** Easy to modify colors, styles, and dimensions

##  Customization

You can easily modify the code to:
- Change chart colors and styles
- Adjust figure size and DPI
- Add more analysis dimensions
- Export in different formats (PDF, SVG, etc.)

##  Contributing

Contributions are welcome! Feel free to:
- Add new visualization types
- Improve chart styling
- Add statistical analysis
- Submit bug fixes

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Contact

- **Repository:** [GitHub Repository](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib)
- **Author:** Kanaiya-rgb

---

**Note:** This project is for educational and analytical purposes. The dataset is used to demonstrate data analysis and visualization techniques using Python and Matplotlib.
