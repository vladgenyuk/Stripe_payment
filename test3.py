import psycopg2

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="your_host",
        port="5432",
        database="your_database",
        user="your_user",
        password="Fveamc0HjomZGodM9WdH3nI63fHycClX"
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a simple query to test the connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print("PostgreSQL version:", version)

    # Close the cursor and connection
    cursor.close()
    connection.close()

    print("Successfully connected to the PostgreSQL database.")

except (Exception, psycopg2.Error) as error:
    print("Error connecting to the PostgreSQL database:", error)