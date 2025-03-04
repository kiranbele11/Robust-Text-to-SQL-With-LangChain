import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

# Load CSV into a pandas DataFrame
csv_file = 'personal_transactions.csv'  
df = pd.read_csv(csv_file)

# Connect to SQLite (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Load the DataFrame into a SQLite table
table_name = 'customers'  
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Verify the data
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {table_name}")
print(cursor.fetchall())

# Close the connection
conn.close()

# Load environment variables
load_dotenv()

# Connect to your SQLite database
db = SQLDatabase.from_uri("sqlite:///mydatabase.db")

# Initialize the OpenAI LLM
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0)

# Create the SQL query chain
query_chain = create_sql_query_chain(llm, db)

# Generate a SQL query
query = query_chain.invoke({"question": "Find the count of rows for each of the categories. Display the category name and count of rows against it"})
print("Generated SQL Query:")
print(query)

# Execute the query
def execute_query(query):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

result = execute_query(query)
print("Query Result:")
print(pd.DataFrame(result))

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())  # List all tables
cursor.execute("PRAGMA table_info(customers);")  
print(cursor.fetchall())  # List all columns in the table
conn.close()

import streamlit as st
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import sqlite3

# Load environment variables
load_dotenv()

# Connect to your SQLite database
db = SQLDatabase.from_uri("sqlite:///mydatabase.db")

# Initialize the OpenAI LLM
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0)

# Create the SQL query chain
query_chain = create_sql_query_chain(llm, db)

# Streamlit app
st.title("SQL Query Generator")

# Custom CSS to increase font size
st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-size: 18px !important; 
    }
    .stButton button {
        font-size: 18px !important;
    }
    h1 {
        font-size: 32px !important;
    }
    h2 {
        font-size: 26px !important;
    }
    .stTextInput input, .stTextArea textarea {
        font-size: 18px !important;
    }
    pre {
        font-size: 20px !important;  /* Increase font size for SQL query */
    }
    .stDataFrame {
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

user_input = st.text_input("Enter your query in natural language:")

if user_input:
    query = query_chain.invoke({"question": user_input})
    st.write("Generated SQL Query:")
    st.code(query)

    # Execute the query
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Get column names
    column_names = [description[0] for description in cursor.description]
    
    conn.close()

    # Convert result to DataFrame with column names
    df_result = pd.DataFrame(result, columns=column_names)

    st.write("Query Executer:")
    st.dataframe(df_result)



