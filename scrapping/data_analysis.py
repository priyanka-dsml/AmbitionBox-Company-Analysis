import matplotlib.pyplot as plt
import pandas as pd
from config.db_config import get_db_connection

def generate_graphs():   # create a funtion for reuse

    conn = get_db_connection()

    df1 = pd.read_sql("""
        SELECT industry, COUNT(*) as count
        FROM companies
        GROUP BY industry
    """, conn)

    df2 = pd.read_sql("""
        SELECT city, COUNT(*) as count
        FROM companies
        GROUP BY city
    """, conn)

    conn.close()

    plt.figure()
    plt.bar(df1["industry"], df1["count"])
    plt.xticks(rotation=90)
    plt.savefig("static/bar.png")

    plt.figure()
    plt.pie(df2["count"], labels=df2["city"], autopct='%1.1f%%')
    plt.savefig("static/pie.png")