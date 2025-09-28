import streamlit as st
import pandas as pd
import plotly.express as px  # Import Plotly Express

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
st.title('🛍️ Interactive Black Friday Sales Analysis')

# Load data
df = load_data()

# --- Optional Raw Data View ---
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Sales Data')
    st.write(df)

st.markdown("---")
st.header('Comprehensive Sales Analysis')

# --- NEW LAYOUT: Using Streamlit Columns ---
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# --- Plot 1: Male vs Female shoppers ---
with col1:
    st.subheader('Male vs Female Shoppers')
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig1 = px.bar(gender_counts, x='Gender', y='Count', color='Gender',
                  color_discrete_map={'M': '#1f77b4', 'F': '#ff7f0e'})
    st.plotly_chart(fig1, use_container_width=True)

# --- Plot 2: Age group percentage ---
with col2:
    st.subheader('Age Group Percentage')
    age_counts = df['Age'].value_counts().reset_index()
    age_counts.columns = ['Age', 'Count']
    fig2 = px.pie(age_counts, names='Age', values='Count')
    st.plotly_chart(fig2, use_container_width=True)

# --- Plot 3: Purchase Amount Distribution ---
with col3:
    st.subheader('Purchase Distribution')
    fig3 = px.histogram(df, x='Purchase', nbins=30)
    fig3.update_layout(bargap=0.1)
    st.plotly_chart(fig3, use_container_width=True)

# --- Plot 4: Avg Purchase by Category ---
with col4:
    st.subheader('Avg Purchase by Category')
    product_purchase = df.groupby('Product_Category_1')['Purchase'].mean().reset_index()
    fig4 = px.scatter(product_purchase, x='Product_Category_1', y='Purchase',
                      labels={'Product_Category_1': 'Product Category'})
    st.plotly_chart(fig4, use_container_width=True)

# --- Plot 5: Top 10 Occupations by Spending ---
# --- Plot 5: Top 10 Occupations by Spending (Matplotlib Style) ---
with col5:
    # Data ko ascending order mein sort karein taaki horizontal bar chart mein top par sabse bada value aaye
    occupation_amount = (
        df.groupby('Occupation')['Purchase']
          .sum()
          .sort_values(ascending=True) # Sort ascending for barh
          .nlargest(10) # Get top 10
    ).reset_index()

    # Occupation ko string banayein taaki ajeeb sorting na ho
    occupation_amount['Occupation'] = occupation_amount['Occupation'].astype(str)

    fig5 = px.bar(occupation_amount,
                  x='Purchase',
                  y='Occupation',
                  orientation='h',
                  title='Top 10 Occupations By Spending')

    # Matplotlib jaisa look: teal color, black border
    fig5.update_traces(marker_color='teal', marker_line=dict(color='black', width=1.5))

    # Y-axis ko total purchase ke hisaab se order karein (highest at top)
    fig5.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title='Total Purchase Amount',
        yaxis_title='Occupation',
        xaxis_gridcolor='lightgrey', # Grid lines
        xaxis_gridwidth=1
    )
    st.plotly_chart(fig5, use_container_width=True)
    
# --- Plot 6: Purchase by City Category ---
with col6:
    st.subheader('Purchase by City Category')
    city_purchase = df.groupby('City_Category')['Purchase'].sum().reset_index()
    city_labels = {'A': 'Tier 1', 'B': 'Tier 2', 'C': 'Tier 3'}
    city_purchase['City_Category'] = city_purchase['City_Category'].map(city_labels)
    fig6 = px.bar(city_purchase, x='City_Category', y='Purchase', color='City_Category')
    st.plotly_chart(fig6, use_container_width=True)