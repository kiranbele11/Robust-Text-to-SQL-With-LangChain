# SQL Query Generator with Streamlit

![SQL Query Generator Banner](assets/banner.png)

> Transform natural language into SQL queries with the power of AI

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.18-green.svg)](https://github.com/langchain-ai/langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Table of Contents
- [Description](#description)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Queries](#sample-queries)
- [Demo](#demo)
- [Contributing](#contributing)
- [FAQ](#faq)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 📝 Description
This project is a powerful SQL Query Generator built using Python, Streamlit, and Langchain. It allows users to input natural language queries, which are then converted into SQL queries and executed against a SQLite database. The results are displayed in a user-friendly interface, making database queries accessible to everyone - not just SQL experts.

## ✨ Features
- **Natural Language Processing**: Convert plain English to SQL syntax
- **Interactive Web Interface**: Clean and intuitive design using Streamlit
- **Data Loading**: Load data from CSV into a SQLite database
- **SQL Query Generation**: Generate SQL queries from natural language input
- **Result Visualization**: Display query results in a structured format
- **Real-time Processing**: Get instant feedback on your queries

## 📸 Screenshots

### Main Interface
![Main Interface](assets/main_interface.png)

### Query Example
![Query Example](assets/query_example.png)

### Results Display
![Results Display](assets/results_display.png)

## 🔧 Technologies Used
- **Python**: Core programming language
- **Streamlit**: Front-end web application framework
- **Pandas**: Data manipulation and analysis
- **SQLite**: Lightweight database
- **Langchain**: Framework for AI-powered applications
- **OpenAI API**: Natural language processing
- **dotenv**: Environment variable management

## 🧠 How It Works
1. **Data Ingestion**: The application loads transaction data from a CSV file into a SQLite database
2. **Natural Language Processing**: User queries in plain English are processed by OpenAI's language model
3. **SQL Generation**: Langchain converts the natural language query into proper SQL syntax
4. **Query Execution**: The generated SQL is executed against the database
5. **Results Rendering**: Query results are beautifully displayed in the Streamlit interface

## 🔌 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sql-query-generator.git
   cd sql-query-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## 🚀 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run tts.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your query in natural language and click "Submit" to see the generated SQL query and its results.

## 📊 Sample Queries

Try these examples to see the power of the application:

### Basic Queries
- "Show me all transactions from January 2018"
- "List all transactions with Amazon"
- "What is the total amount spent on groceries?"

### Intermediate Queries
- "Calculate the average transaction amount for each category"
- "What are the top 5 most expensive purchases?"
- "Show me the total amount spent on each account type"

### Advanced Queries
- "Compare spending between the first and second half of the year"
- "Show me monthly spending trends by category"
- "What day of the week do I spend the most money?"

## 🎮 Demo

Check out our live demo at [demo-link](https://your-demo-link-here) to see the SQL Query Generator in action!

## 👥 Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ❓ FAQ

**Q: Do I need to know SQL to use this app?**  
A: No! The whole point of this application is to let you query databases using natural language.

**Q: What types of databases does this support?**  
A: Currently, the app works with SQLite databases, but it can be extended to support other SQL databases.

**Q: Is my data secure?**  
A: Your data remains local unless you deploy the application to a public server. API calls to OpenAI follow their privacy policies.

**Q: Can I customize the database schema?**  
A: Yes, you can modify the CSV import and database creation part in the code to match your data structure.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [Langchain](https://langchain.readthedocs.io/en/latest/) for LLM application development
- [Pandas](https://pandas.pydata.org/) for data processing capabilities
- [SQLite](https://www.sqlite.org/index.html) for database functionality
- [OpenAI](https://openai.com/) for the powerful language models