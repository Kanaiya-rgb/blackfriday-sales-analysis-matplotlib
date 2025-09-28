# Black Friday Sales Analysis Dashboard

##  Project Overview

This project is a **comprehensive Black Friday Sales Analysis Dashboard** built using **Python** and **Matplotlib**. It analyzes a Black Friday retail dataset and creates a multi-panel visualization dashboard with 6 different charts to provide actionable business insights.

The dashboard includes various types of visualizations such as bar charts, pie charts, histograms, scatter plots, and horizontal bar charts to analyze customer demographics, purchase patterns, and sales performance across different dimensions.

##  Dashboard Features

The dashboard consists of 6 key visualizations:

1. **Gender Distribution** - Bar chart showing male vs female shoppers
2. **Age Group Analysis** - Pie chart with percentage breakdown of age groups
3. **Purchase Amount Distribution** - Histogram showing spending patterns
4. **Product Category Performance** - Scatter plot of average purchase by category
5. **Top Occupations by Spending** - Horizontal bar chart of highest spending occupations
6. **City Category Analysis** - Bar chart showing total purchases by city tier

##  Dataset

- **Source:** [Kaggle - Black Friday Sales Dataset](https://www.kaggle.com/datasets/rajeshrampure/black-friday-sale)
- **Columns:** User_ID, Product_ID, Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status, Product_Category_1, Product_Category_2, Product_Category_3, Purchase
- **File:** BlackFriday.csv

##  Dependencies

`ash
pip install pandas matplotlib numpy
`

**Required Libraries:**
- pandas - Data manipulation and analysis
- matplotlib - Data visualization
- 
umpy - Numerical computing (optional, for advanced operations)

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
*Note: Despite the .ipynb extension, this is a Python script that can be run directly*

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

##  Key Insights Generated

The dashboard provides insights into:

- **Customer Demographics**: Gender distribution and age group preferences
- **Spending Patterns**: Purchase amount distribution and average spending
- **Product Performance**: Which product categories generate higher average purchases
- **Occupation Analysis**: Which occupations spend the most during Black Friday
- **Geographic Distribution**: Sales performance across different city tiers (Metro/Urban/Rural)

##  Dashboard Output

The script generates a high-resolution dashboard image (dashboard_blackfriday.png) with:
- **Size:** 20x12 inches at 150 DPI
- **Layout:** 2 rows  3 columns grid
- **Professional styling** with proper titles, labels, and legends

##  Code Features

- **Data Cleaning**: Automatic handling of missing values
- **Professional Visualization**: High-quality plots with proper styling
- **Comprehensive Analysis**: Multiple chart types for different insights
- **Export Functionality**: Saves dashboard as PNG image
- **Responsive Layout**: Uses constrained_layout for optimal spacing

##  Sample Analysis Results

The dashboard reveals patterns such as:
- Gender distribution of shoppers
- Age group preferences (typically 26-35 age group dominates)
- Purchase amount distribution (usually right-skewed)
- Product category performance variations
- Occupation-based spending patterns
- City tier performance differences

##  Customization

You can easily modify the code to:
- Change chart colors and styles
- Adjust figure size and DPI
- Add more analysis dimensions
- Modify chart types
- Export in different formats (PDF, SVG, etc.)

##  Contributing

Contributions are welcome! Feel free to:
- Add new visualization types
- Improve chart styling
- Add statistical analysis
- Enhance data preprocessing
- Submit bug fixes

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Contact

- **Repository:** [https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib)
- **Author:** Kanaiya-rgb

---

**Note:** This project is for educational and analytical purposes. The dataset is used to demonstrate data analysis and visualization techniques using Python and Matplotlib.
