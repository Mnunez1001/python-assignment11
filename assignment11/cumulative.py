import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


try:
    # Connecting to the database
    conn = sqlite3.connect("../db/lesson.db")


    # Geting the total price for each order

    query = """
        SELECT
            orders.order_id,
            SUM(products.price * line_items.quantity) AS total_price
        FROM orders
        JOIN line_items
            ON orders.order_id = line_items.order_id
        JOIN products
            ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id;
    """


    # Loading the SQL results into a DataFrame
    df = pd.read_sql_query(
        query,
        conn
    )


    print("Order Totals:")
    print(df.head())


    # Calculating cumulative revenue

    def cumulative(row):
        totals_above = df["total_price"][0:row.name + 1]
        return totals_above.sum()


    df["cumulative"] = df.apply(
        cumulative,
        axis=1
    )


    print("\nOrder Totals with Cumulative Revenue:")
    print(df.head())

    # Creating the line plot

    df.plot(
        kind="line",
        x="order_id",
        y="cumulative",
        figsize=(10, 6),
        legend=False
    )


    plt.title("Cumulative Revenue by Order")
    plt.xlabel("Order ID")
    plt.ylabel("Cumulative Revenue ($)")

    plt.tight_layout()
    plt.show()


except sqlite3.Error as error:
    print(f"SQLite error: {error}")


finally:
    if "conn" in locals():
        conn.close()
        print("Database connection closed.")