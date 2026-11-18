# AmbitionBox Company Analysis

## Project Overview
This project focuses on collecting, cleaning, storing, and analyzing company-related data from AmbitionBox using Python, Web Scraping, MySQL, and Flask.

The application provides data visualization and tabular views to explore company information.

## Technologies Used
- Python
- Flask
- MySQL
- Pandas
- BeautifulSoup
- HTML
- CSS
- Matplotlib

## Project Features
- Web scraping for company information
- Data cleaning and preprocessing
- Storing structured data in CSV and MySQL
- Company data analysis
- Graphical data visualization
- Table-based data presentation
- Flask-based web application

## Project Structure

```text
AmbitionBox_Project/
│
├── app.py
├── config/
│   └── db_config.py
├── data/
│   └── ambitionbox_cleaned.csv
├── scrapping/
│   ├── scrape.py
│   ├── clean_data.py
│   ├── data_analysis.py
│   
├── static/
│   ├── bar.png
│   └── style.css
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── graphview.html
│   └── tableview.html
└── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/priyanka-dsml/AmbitionBox-Company-Analysis.git
```

### 2. Open the project folder

```bash
cd AmbitionBox-Company-Analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL
- Install and start MySQL.
- Create the database `ambitionbox_db`.
- Configure your database connection locally.
- Do not upload database passwords or credentials to GitHub.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes
- Practical experience with Python web scraping
- Data cleaning and preprocessing
- MySQL database connectivity
- Exploratory Data Analysis
- Data visualization
- Flask application development

## Author
Priyanka Sharma

GitHub: https://github.com/priyanka-dsml
