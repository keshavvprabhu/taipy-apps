import duckdb

# Load the CSV file into DuckDB
con = duckdb.connect()
con.execute("CREATE TABLE beneficiaries AS SELECT * FROM read_csv_auto('data/beneficiaries.csv', HEADER=TRUE)")

# 1. Count total records
print('Total records:', con.execute('SELECT COUNT(*) FROM beneficiaries').fetchone()[0])

# 2. Count by StateCode
print('\nRecords by StateCode:')
print(con.execute('SELECT StateCode, COUNT(*) FROM beneficiaries GROUP BY StateCode').fetchdf())

# 3. Count by RoutingIdentifierType
print('\nRecords by RoutingIdentifierType:')
print(con.execute('SELECT RoutingIdentifierType, COUNT(*) FROM beneficiaries GROUP BY RoutingIdentifierType').fetchdf())

# 4. List unique cities
print('\nUnique cities:')
print(con.execute('SELECT DISTINCT City FROM beneficiaries').fetchdf())

# 5. Show sample records
print('\nSample records:')
print(con.execute('SELECT * FROM beneficiaries LIMIT 5').fetchdf())

con.close()
