import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration (MUST be the first Streamlit command) ---
st.set_page_config(
    page_title="Black Friday Sales Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded" # Keep sidebar open initially
)

# --- Data Loading and Caching ---
@st.cache_data
def load_data():
    """Loads and cleans the Black Friday sales data from a GitHub URL."""
    url = 'https://raw.githubusercontent.com/Kanaiya-rgb/blackfriday-sales-analysis-matplotlib/main/BlackFriday.csv'
    df = pd.read_csv(url)
    # Data Cleaning: Fill missing values more specifically
    # For categorical product columns, filling with 0 might be okay if we treat 0 as 'Not Applicable'
    df['Product_Category_2'].fillna(0, inplace=True)
    df['Product_Category_3'].fillna(0, inplace=True)
    # Convert occupation to string for easier filtering/plotting
    df['Occupation'] = df['Occupation'].astype(str)
    return df

# Load data
try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()


# --- Sidebar for Filters ---
st.sidebar.header('Filter Your Data')

# Gender Filter
gender = st.sidebar.multiselect(
    'Select Gender',
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

# Age Filter
age = st.sidebar.multiselect(
    'Select Age Group',
    options=df['Age'].unique(),
    default=df['Age'].unique()
)

# City Filter
city = st.sidebar.multiselect(
    'Select City Category',
    options=df['City_Category'].unique(),
    default=df['City_Category'].unique()
)

# Filter the dataframe based on user selection
df_selection = df.query(
    "Gender == @gender & Age == @age & City_Category == @city"
)

# Check if the dataframe is empty after filtering
if df_selection.empty:
    st.warning("No data available for the selected filters. Please select different options.")
    st.stop() # Stop the app from running further

# --- Main Page ---
st.title('🛍️ Interactive Black Friday Sales Analysis')
st.markdown("A dynamic dashboard to explore customer purchase behavior.")
st.markdown("---")


# --- Key Performance Indicators (KPIs) ---
total_sales = int(df_selection['Purchase'].sum())
average_purchase = round(df_selection['Purchase'].mean(), 2)
total_transactions = len(df_selection)

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(
    label="Total Sales (USD)",
    value=f"$ {total_sales:,}",
    delta="Based on filtered data"
)
kpi2.metric(
    label="Average Purchase Value (USD)",
    value=f"$ {average_purchase:,.2f}",
    delta="Average spend per transaction"
)
kpi3.metric(
    label="Total Transactions",
    value=f"{total_transactions:,}",
    delta="Total number of purchases"
)

st.markdown("---")

# --- Charts Layout ---
st.header('Comprehensive Sales Analysis')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)


# --- Plot 1: Male vs Female shoppers (Using df_selection) ---
with col1:
    st.subheader('Male vs Female Shoppers')
    gender_counts = df_selection['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig1 = px.bar(gender_counts, x='Gender', y='Count', color='Gender',
                  color_discrete_map={'M': '#1f77b4', 'F': '#ff7f0e'},
                  template='plotly_white')
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

# --- Plot 2: Age group percentage (Using df_selection) ---
with col2:
    st.subheader('Age Group Percentage')
    age_counts = df_selection['Age'].value_counts().reset_index()
    age_counts.columns = ['Age', 'Count']
    fig2 = px.pie(age_counts, names='Age', values='Count', hole=0.4)
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

# --- Plot 3: Purchase Amount Distribution (Using df_selection) ---
with col3:
    st.subheader('Purchase Distribution')
    fig3 = px.histogram(df_selection, x='Purchase', nbins=50, template='plotly_white')
    fig3.update_layout(bargap=0.1)
    st.plotly_chart(fig3, use_container_width=True)

# --- Plot 4: Purchase by City Category (Using df_selection) ---
with col4:
    st.subheader('Total Purchase by City')
    city_purchase = df_selection.groupby('City_Category')['Purchase'].sum().reset_index()
    city_labels = {'A': 'Tier 1 City', 'B': 'Tier 2 City', 'C': 'Tier 3 City'}
    city_purchase['City_Category_Label'] = city_purchase['City_Category'].map(city_labels)
    fig4 = px.bar(city_purchase, x='City_Category_Label', y='Purchase', color='City_Category_Label', template='plotly_white')
    fig4.update_layout(xaxis_title="City Tier", yaxis_title="Total Purchase", showlegend=False)
    st.plotly_chart(fig4, use_container_width=True)

# --- Plot 5: Top 10 Occupations by Spending (Guaranteed Sort) ---
with col5:
    st.subheader('Top 10 Occupations by Spending')
    occupation_amount = (
        df_selection.groupby('Occupation')['Purchase']
          .sum()
          .nlargest(10)
          .sort_values(ascending=True) # Sort ascending for horizontal bar chart
          .reset_index()
    )
    fig5 = px.bar(occupation_amount,
                  x='Purchase',
                  y='Occupation',
                  orientation='h',
                  text='Purchase',
                  template='plotly_white')
    fig5.update_traces(texttemplate='$%{text:,.2s}', textposition='outside')
    fig5.update_layout(yaxis_title="Occupation ID", xaxis_title="Total Spending")
    st.plotly_chart(fig5, use_container_width=True)


# --- Plot 6: Purchase by Marital Status ---
with col6:
    st.subheader('Purchase by Marital Status')
    marital_status_spending = df_selection.groupby('Marital_Status')['Purchase'].sum().reset_index()
    status_labels = {0: 'Single', 1: 'Married'}
    marital_status_spending['Marital_Status_Label'] = marital_status_spending['Marital_Status'].map(status_labels)

    fig6 = px.pie(marital_status_spending,
                  names='Marital_Status_Label',
                  values='Purchase',
                  title='Total Spending: Single vs. Married',
                  hole=0.4)
    st.plotly_chart(fig6, use_container_width=True)


# --- Optional Raw Data View ---
if st.checkbox('Show Filtered Raw Data'):
    st.subheader('Filtered Sales Data')
    st.write(df_selection)
