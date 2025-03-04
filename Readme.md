# SQL Query Generator with Streamlit

## Description
This project is a SQL Query Generator built using Python, Streamlit, and Langchain. It allows users to input natural language queries, which are then converted into SQL queries and executed against a SQLite database. The results are displayed in a user-friendly interface.

## Features
- Load data from CSV into a SQLite database.
- Generate SQL queries from natural language input.
- Display query results in a structured format.
- Easy to use with a simple web interface.

## Technologies Used
- Python
- Streamlit
- Pandas
- SQLite
- Langchain
- dotenv

## Installation

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

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run TTS.ipynb
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your query in natural language and click "Submit" to see the generated SQL query and its results.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Streamlit](https://streamlit.io/)
- [Langchain](https://langchain.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [SQLite](https://www.sqlite.org/index.html)