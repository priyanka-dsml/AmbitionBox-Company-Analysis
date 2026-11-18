from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from config.db_config import get_db_connection
from scrapping.data_analysis import generate_graphs
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


app = Flask(__name__)

# LOGIN
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    conn = get_db_connection()

    cities = pd.read_sql("SELECT DISTINCT city FROM companies", conn)["city"].tolist()
    industries = pd.read_sql("SELECT DISTINCT industry FROM companies", conn)["industry"].tolist()

    # 🔹 Filters
    city = request.args.get("city")
    industry = request.args.get("industry")
    rating = request.args.get("rating")
    search = request.args.get("search")

    query = "SELECT DISTINCT company_name, rating, industry, city, metro_city FROM companies WHERE 1=1"
    params = []

    if city:
        query += " AND city = %s"
        params.append(city)

    if industry:
        query += " AND industry = %s"
        params.append(industry)

    if rating:
        query += " AND rating >= %s"
        params.append(float(rating))

    if search:
        query += " AND company_name LIKE %s"
        params.append(f"%{search}%")

    df = pd.read_sql(query, conn, params=params)
    # 🔹 GRAPH (filtered data)
    if not df.empty:

       graph_data = df.groupby("industry").size()

       plt.figure()
       graph_data.plot(kind="bar")
       plt.xticks(rotation=90)
       plt.savefig("static/bar.png")

    else:
        print("No data for selected filters")

    conn.close()

    return render_template(
        "index.html",
        data=df.to_dict(orient="records"),
        cities=cities,
        industries=industries
    )
# 🔹 GRAPH PAGE
@app.route("/graph")
def graph():

    generate_graphs()   # reuse from analysis.py

    return render_template("graphview.html")

if __name__ == "__main__":
    app.run(debug=True,port = 5002)