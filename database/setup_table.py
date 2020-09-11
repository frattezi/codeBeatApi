import psycopg2

try:
    con = psycopg2.connect(
        database="beats",
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
    )

    print("Database opened successfully")

    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS beats;
        DROP TABLE IF EXISTS users;
        """
    )

    print("Tables dropped")

    create_user_table_command = """
        CREATE TABLE users( 
            user_id serial,
            PRIMARY KEY (user_id), 
            name TEXT NOT NULL, 
            email TEXT NOT NULL)"""

    create_beats_table_command = """
        CREATE TABLE beats( 
            beat_id serial,
            user_id INT NOT NULL,
            data TEXT NOT NULL,
            published_date timestamp DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (beat_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)"""

    cur.execute(create_user_table_command)
    cur.execute(create_beats_table_command)

    con.commit()
    con.close()
    print("Users created")
    print("Beats created")

except Exception as e:
    con.close()
    print(e)

print("Table created successfully")
