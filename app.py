import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    df.fillna(0, inplace=True)
    return df

# --- Main Application ---
st.title('🛍️ Black Friday Sales Analysis Dashboard')

# Load data
df = load_data()

st.markdown("---")

# --- Layout using Streamlit Columns ---
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# --- Plot 1: Male vs Female shoppers ---
with col1:
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    # Colors matched with Matplotlib
    colors = {'M': 'blue', 'F': 'orange'}
    fig1 = px.bar(gender_counts, x='Gender', y='Count', title='Male vs Female Shoppers',
                  color='Gender', color_discrete_map=colors)
    st.plotly_chart(fig1, use_container_width=True)

# --- Plot 2: Age group percentage ---
with col2:
    age_counts = df['Age'].value_counts().reset_index()
    age_counts.columns = ['Age', 'Count']
    # Matplotlib's default color cycle for pie charts
    pie_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    fig2 = px.pie(age_counts, names='Age', values='Count', title='Age Group Percentage',
                  color_discrete_sequence=pie_colors)
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

# --- Plot 3: Purchase Amount Distribution ---
with col3:
    fig3 = go.Figure()
    fig3.add_trace(go.Histogram(x=df['Purchase'], nbinsx=30,
                                marker_color='purple',
                                marker_line=dict(color='black', width=1)))
    fig3.update_layout(title_text='Purchase Amount Distribution',
                       xaxis_title_text='Amount',
                       yaxis_title_text='Number of Transactions')
    st.plotly_chart(fig3, use_container_width=True)

# --- Plot 4: Product Category vs Avg Purchase ---
with col4:
    product_purchase = df.groupby('Product_Category_1')['Purchase'].mean().reset_index()
    fig4 = px.scatter(product_purchase, x='Product_Category_1', y='Purchase',
                      title='Product Category vs Avg Purchase')
    # Marker color set to red
    fig4.update_traces(marker=dict(color='red', size=8))
    fig4.update_layout(xaxis_title='Product Category', yaxis_title='Avg Purchase Amount')
    st.plotly_chart(fig4, use_container_width=True)

# --- Plot 5: Top 10 Occupations by Spending ---
with col5:
    occupation_amount = df.groupby('Occupation')['Purchase'].sum().nlargest(10).reset_index()
    occupation_amount['Occupation'] = occupation_amount['Occupation'].astype(str)
    
    fig5 = px.bar(occupation_amount,
                  x='Purchase',
                  y='Occupation',
                  orientation='h',
                  title='Top 10 Occupations By Spending')
    # Bar color set to teal with black border
    fig5.update_traces(marker_color='teal', marker_line=dict(color='black', width=1))
    fig5.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig5, use_container_width=True)

# --- Plot 6: City Category Wise Total Purchase ---
with col6:
    city_purchase = df.groupby('City_Category')['Purchase'].sum().reset_index()
    city_labels = {'A': 'Tier 1 (Metro)', 'B': 'Tier 2 (Urban)', 'C': 'Tier 3 (Rural)'}
    city_purchase['City_Category'] = city_purchase['City_Category'].map(city_labels)
    # Custom colors matched with Matplotlib
    city_colors = {'Tier 1 (Metro)': 'gold', 'Tier 2 (Urban)': 'lightgreen', 'Tier 3 (Rural)': 'lightcoral'}
    fig6 = px.bar(city_purchase, x='City_Category', y='Purchase', title='City Category Wise Total Purchase',
                  color='City_Category', color_discrete_map=city_colors)
    fig6.update_layout(xaxis_title='City Category', yaxis_title='Total Purchase')
    st.plotly_chart(fig6, use_container_width=True)