import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')
print(pd.read_sql("""
SELECT *
 FROM products;
""", conn))
print("\n")

#Step 1
# Select the product line.
 # Count the number of each product line.
 # Give the count the alias "count."
 # Sort descending by count.
print(pd.read_sql("""
SELECT productLine, COUNT(*) AS count
 FROM products
 GROUP BY productLine
 ORDER By count DESC;
""", conn))
print("\n")


# Step 2
# Select the product line.
 # Determine the average price by product line.
 # Give the average the alias "avgPrice."
 # Sort descending by avgPrice.
print(pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
 FROM products
 GROUP BY productLine
 ORDER By avgPrice DESC;
""", conn))
print("\n")


# Step 3
# Select the product line.
 # Find the minimum of the MSRP as minMSRP.
 # Find the maximum of the MSRP as maxMSRP.
print(pd.read_sql("""
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP
 FROM products
 GROUP BY productLine
""", conn))
print("\n")


# Step 4
# Repeat (3), but only select the rows where the MSRP is $50 or more.
print(pd.read_sql("""
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP
 FROM products
 WHERE MSRP >= 50
 GROUP BY productLine
""", conn))
print("\n")


# Step 5
# Repeat (2), but only select the product lines with an average price greater than $50.
print(pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
 FROM products
 GROUP BY productLine
 HAVING avgPrice >= 50
 ORDER By avgPrice DESC
""", conn))
print("\n")


# Step 6
# Select the product line.
 # Find the average buy price as 'buyPrice' and the average MSRP as 'avgMSRP'.
 # Only select MSRP greater than or equal to $50.
 # Only select avgPrice greater than or equal to $50.
 # Group by product line and order by the ascending average price.
print(pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP
 FROM products
 WHERE MSRP >= 50
 GROUP BY productLine
 HAVING avgPrice >= 50
 ORDER By avgPrice ASC
""", conn))
print("\n")

conn.close()