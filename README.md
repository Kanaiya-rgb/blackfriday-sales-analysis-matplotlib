<div align="center">

# 🛍️ Black Friday Sales Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)](https://matplotlib.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib.svg)](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib/stargazers)

*A comprehensive data visualization dashboard for Black Friday sales analysis*

[🚀 Quick Start](#-quick-start) • [📊 Features](#-dashboard-features) • [📈 Demo](#-dashboard-preview) • [🛠️ Setup](#-installation)

</div>

---

## 📋 Project Overview

This project is a **comprehensive Black Friday Sales Analysis Dashboard** built using **Python** and **Matplotlib**. It analyzes a Black Friday retail dataset and creates a multi-panel visualization dashboard with 6 different charts to provide actionable business insights.

The dashboard includes various types of visualizations such as bar charts, pie charts, histograms, scatter plots, and horizontal bar charts to analyze customer demographics, purchase patterns, and sales performance across different dimensions.

### 🎯 What You'll Get

- 📊 **6 Interactive Visualizations** in a single dashboard
- 🎨 **Professional Styling** with high-resolution output
- 📈 **Business Insights** from customer behavior analysis
- 🔧 **Easy Customization** for different datasets
- 💾 **Export Ready** PNG format for presentations

## 📊 Dashboard Features

The dashboard consists of 6 key visualizations:

<table>
<tr>
<td width="50%">

### 📈 Visualization Types

- 🧑‍🤝‍🧑 **Gender Distribution** - Bar chart showing male vs female shoppers
- 🎂 **Age Group Analysis** - Pie chart with percentage breakdown of age groups  
- 💰 **Purchase Amount Distribution** - Histogram showing spending patterns
- 📦 **Product Category Performance** - Scatter plot of average purchase by category
- 💼 **Top Occupations by Spending** - Horizontal bar chart of highest spending occupations
- 🏙️ **City Category Analysis** - Bar chart showing total purchases by city tier

</td>
<td width="50%">

### 🎨 Visual Elements

- **High Resolution**: 20×12 inches at 150 DPI
- **Professional Layout**: 2×3 grid with constrained layout
- **Color Schemes**: Distinct colors for each chart type
- **Interactive Legends**: Clear labeling and legends
- **Export Ready**: PNG format for presentations

</td>
</tr>
</table>

## 📥 Dataset Information

<div align="center">

| 📊 **Dataset Details** | |
|:---|:---|
| **Source** | [Kaggle - Black Friday Sales Dataset](https://www.kaggle.com/datasets/rajeshrampure/black-friday-sale) |
| **File** | `BlackFriday.csv` |
| **Size** | ~550,000 records |
| **Columns** | 12 features |

</div>

### 📋 Dataset Schema

| Column | Type | Description |
|:---|:---|:---|
| `User_ID` | Integer | Unique customer identifier |
| `Product_ID` | String | Unique product identifier |
| `Gender` | String | Customer gender (M/F) |
| `Age` | String | Age group (0-17, 18-25, etc.) |
| `Occupation` | Integer | Customer occupation code |
| `City_Category` | String | City tier (A/B/C) |
| `Stay_In_Current_City_Years` | String | Years in current city |
| `Marital_Status` | Integer | Marital status (0/1) |
| `Product_Category_1` | Integer | Primary product category |
| `Product_Category_2` | Integer | Secondary product category |
| `Product_Category_3` | Integer | Tertiary product category |
| `Purchase` | Integer | Purchase amount in INR |

## 📦 Installation & Dependencies

### 🚀 Quick Install

`ash
pip install pandas matplotlib numpy
`

### 📚 Required Libraries

| Library | Version | Purpose |
|:---|:---|:---|
| **pandas** | 1.0+ | Data manipulation and analysis |
| **matplotlib** | 3.0+ | Data visualization and plotting |
| **numpy** | 1.18+ | Numerical computing (optional) |

### 🔧 Alternative Installation

`ash
# Using conda
conda install pandas matplotlib numpy

# Using pip with requirements.txt
pip install -r requirements.txt
`

## 🚀 Quick Start

### 1️⃣ Clone the Repository

`ash
git clone https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib.git
cd blackfriday-sales-analysis-matplotlib
`

### 2️⃣ Install Dependencies

`ash
pip install pandas matplotlib numpy
`

### 3️⃣ Download Dataset

- Download BlackFriday.csv from [Kaggle](https://www.kaggle.com/datasets/rajeshrampure/black-friday-sale)
- Place it in the project root directory

### 4️⃣ Run Analysis

`ash
python BlackFriday.ipynb
`

> **Note:** Despite the .ipynb extension, this is a Python script that can be run directly

## 📁 Project Structure

```
blackfriday-sales-analysis-matplotlib/
├── 📄 BlackFriday.ipynb          # Main analysis script
├── 📊 BlackFriday.csv            # Dataset (download from Kaggle)
├── 🖼️ dashboard_blackfriday.png  # Generated dashboard image
├── 📝 .gitignore
├── 📄 LICENSE
└── 📖 README.md
```

## 📈 Dashboard Preview

<div align="center">

### 🎨 Sample Dashboard Output

![Black Friday Sales Dashboard](dashboard_blackfriday.png)

*High-resolution dashboard with 6 comprehensive visualizations*

</div>

## 📊 Key Insights Generated

The dashboard provides insights into:

### 👥 Customer Demographics
- **Gender Distribution**: Male vs female shopping patterns
- **Age Group Preferences**: Which age groups shop most during Black Friday
- **Occupation Analysis**: Which professions spend the most

### 💰 Spending Patterns
- **Purchase Amount Distribution**: Spending behavior analysis
- **Product Category Performance**: Which categories generate higher sales
- **Geographic Distribution**: Sales performance across city tiers

### 🏙️ Geographic Analysis
- **City Tier Performance**: Metro vs Urban vs Rural sales
- **Regional Spending Patterns**: Location-based purchase behavior

## 🎨 Dashboard Output Specifications

The script generates a high-resolution dashboard image (dashboard_blackfriday.png) with:

| Specification | Value |
|:---|:---|
| **Size** | 20×12 inches |
| **DPI** | 150 (high resolution) |
| **Layout** | 2 rows × 3 columns grid |
| **Format** | PNG with transparency support |
| **Styling** | Professional with proper titles and legends |

## 🔧 Code Features

### ✨ Advanced Features

- 🔄 **Data Cleaning**: Automatic handling of missing values
- 🎨 **Professional Visualization**: High-quality plots with proper styling
- 📊 **Comprehensive Analysis**: Multiple chart types for different insights
- 💾 **Export Functionality**: Saves dashboard as PNG image
- 📐 **Responsive Layout**: Uses `constrained_layout` for optimal spacing
- 🎯 **Customizable**: Easy to modify colors, styles, and dimensions

### 🛠️ Technical Highlights

```python
# Key features in the code
fig, axes = plt.subplots(2, 3, figsize=(20, 12), dpi=150, constrained_layout=True)
fig.suptitle('Black Friday Sales Analysis Dashboard', fontsize=22, fontweight='bold')
```

## 📈 Sample Analysis Results

The dashboard reveals patterns such as:

- **Gender Distribution**: Typically shows male dominance in Black Friday shopping
- **Age Group Preferences**: 26-35 age group usually dominates purchases
- **Purchase Distribution**: Right-skewed distribution with most purchases in lower ranges
- **Product Categories**: Electronics and fashion typically perform well
- **Occupation Patterns**: IT and business professionals often spend more
- **City Performance**: Metro cities (Tier A) usually show higher sales

## 🛠️ Customization Options

You can easily modify the code to:

### 🎨 Visual Customization
- Change chart colors and styles
- Adjust figure size and DPI
- Modify chart types (bar → line, pie → donut, etc.)
- Add custom themes and color palettes

### 📊 Analysis Enhancement
- Add more analysis dimensions
- Include statistical annotations
- Add trend lines and correlations
- Implement interactive features

### 💾 Export Options
- Export in different formats (PDF, SVG, etc.)
- Create multiple dashboard variants
- Generate individual chart exports
- Add custom branding and logos

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🚀 Quick Contributions
- 🐛 **Bug Fixes**: Report and fix issues
- 📊 **New Visualizations**: Add more chart types
- 🎨 **Styling Improvements**: Enhance visual appeal
- 📈 **Statistical Analysis**: Add advanced analytics

### 🔧 Development Setup

1. Fork the repository
2. Create a feature branch: git checkout -b feature/amazing-feature
3. Make your changes
4. Commit: git commit -m 'Add amazing feature'
5. Push: git push origin feature/amazing-feature
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact & Support

<div align="center">

| Contact Method | Details |
|:---|:---|
| **Repository** | [GitHub Repository](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib) |
| **Author** | Kanaiya-rgb |
| **Issues** | [Report Issues](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib/issues) |
| **Discussions** | [GitHub Discussions](https://github.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib/discussions) |

</div>

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ for the data science community**

[⬆ Back to Top](#-black-friday-sales-analysis-dashboard)

</div>

---

**Note:** This project is for educational and analytical purposes. The dataset is used to demonstrate data analysis and visualization techniques using Python and Matplotlib.
