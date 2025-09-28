import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(
    page_title="Black Friday Sales Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# --- Data Loading and Caching ---
@st.cache_data
def load_data():
    """Loads and cleans the Black Friday sales data from a GitHub URL."""
    url = 'https://raw.githubusercontent.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib/main/BlackFriday.csv'
    df = pd.read_csv(url)
    # Data Cleaning: Fill missing values
    df.fillna(0, inplace=True)
    return df

# --- Main Application ---
st.title('🛍️ Black Friday Sales Analysis')

# Load data
df = load_data()

# --- Optional Raw Data View ---
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Sales Data')
    st.write(df)

st.markdown("---")
st.header('Comprehensive Sales Analysis')

# --- NEW LAYOUT: Using Streamlit Columns ---
# Create two rows of three columns each
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)


# --- Plot 1: Male vs Female shoppers ---
with col1:
    st.subheader('Male vs Female Shoppers')
    gender_counts = df['Gender'].value_counts()
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    ax1.bar(gender_counts.index, gender_counts.values, color=['#1f77b4', '#ff7f0e'])
    ax1.set_xlabel('Gender')
    ax1.set_ylabel('Count')
    st.pyplot(fig1)

# --- Plot 2: Age group percentage ---
with col2:
    st.subheader('Age Group Percentage')
    age_counts = df['Age'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.pie(age_counts.values, labels=age_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

# --- Plot 3: Purchase Amount Distribution ---
with col3:
    st.subheader('Purchase Distribution')
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    ax3.hist(df['Purchase'], bins=30, color='purple', edgecolor='black')
    ax3.set_xlabel('Amount')
    ax3.set_ylabel('Transactions')
    st.pyplot(fig3)

# --- Plot 4: Product Category vs Avg Purchase ---
with col4:
    st.subheader('Avg Purchase by Category')
    product_purchase = df.groupby('Product_Category_1')['Purchase'].mean()
    fig4, ax4 = plt.subplots(figsize=(6, 5))
    ax4.scatter(product_purchase.index, product_purchase.values, color='red', alpha=0.7)
    ax4.set_xlabel('Product Category')
    ax4.set_ylabel('Avg Purchase Amount')
    ax4.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig4)

# --- Plot 5: Top Occupation by Amount Spent ---
with col5:
    st.subheader('Top 10 Occupations')
    occupation_amount = (
        df.groupby('Occupation')['Purchase']
          .sum()
          .sort_values(ascending=True)
          .tail(10)
    )
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    ax5.barh(occupation_amount.index.astype(str), occupation_amount.values, color='teal')
    ax5.set_xlabel('Total Purchase')
    ax5.set_ylabel('Occupation')
    st.pyplot(fig5)

# --- Plot 6: City Category Wise Total Purchase ---
with col6:
    st.subheader('Purchase by City Category')
    city_purchase = df.groupby('City_Category')['Purchase'].sum()
    city_labels = {'A': 'Tier 1', 'B': 'Tier 2', 'C': 'Tier 3'}
    city_purchase.index = city_purchase.index.map(city_labels)
    fig6, ax6 = plt.subplots(figsize=(6, 5))
    ax6.bar(city_purchase.index, city_purchase.values, color=['gold', 'lightgreen', 'lightcoral'])
    ax6.set_xlabel('City Category')
    ax6.set_ylabel('Total Purchase')
    st.pyplot(fig6)