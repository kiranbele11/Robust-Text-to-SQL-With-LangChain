# SQL Query Generator 🔍

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

A powerful natural language to SQL query converter built with Streamlit and LangChain. Transform plain English questions into SQL queries and get instant results from your database.

## ✨ Features

- **Natural Language Processing**: Convert everyday language into SQL queries
- **Instant Query Execution**: Execute generated SQL queries with a single click
- **Data Visualization**: View results in a clean, tabular format
- **User-Friendly Interface**: Simple and intuitive web interface
- **CSV to Database**: Automatically import CSV data into SQLite
- **Customizable Font Size**: Enhanced readability with larger font options

## 🖼️ Screenshots

![App Homepage](Screenshot 2025-03-04 at 6.54.55 PM.png)
![Query Results](Screenshot 2025-03-04 at 1.00.09 PM.png)

## 📹 Demo Video

[Watch the demo](Screen Recording 2025-03-04 at 6.44.59 PM.mov)

## 🛠️ How It Works

1. **Natural Language Input**: Users enter queries in plain English
2. **LangChain Processing**: The app uses OpenAI through LangChain to translate natural language to SQL
3. **SQL Execution**: The generated query runs against the SQLite database
4. **Results Display**: Query results appear in a clean, formatted table

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sql-query-generator.git
   cd sql-query-generator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**:
   - Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 📊 Usage

1. **Prepare your data**:
   - Place your CSV file in the project directory (default: `personal_transactions.csv`)
   
2. **Launch the app**:
   ```bash
   streamlit run tts.py
   ```

3. **Access the web interface**:
   - Open your browser and go to `http://localhost:8602`

4. **Using the app**:
   - Type your question in natural language (e.g., "How many transactions are in each category?")
   - View the generated SQL query and results

## 🧩 Customization

- **Change the data source**: Edit `tts.py` to point to your own CSV file
- **Modify the database**: Change the SQLite database name or structure
- **Adjust font sizes**: Modify the CSS in the Streamlit app

## 📘 Technical Details

- **Backend**: Python with SQLite database
- **Frontend**: Streamlit web interface
- **AI Integration**: LangChain with OpenAI
- **Data Processing**: Pandas for data manipulation

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin new-feature`
5. Submit a pull request


## Acknowledgments

- [Streamlit](https://streamlit.io/) for the interactive web framework
- [LangChain](https://langchain.readthedocs.io/) for NLP capabilities
- [OpenAI](https://openai.com/) for the language model
- [Pandas](https://pandas.pydata.org/) for data processing
- [SQLite](https://www.sqlite.org/) for database functionality

---

