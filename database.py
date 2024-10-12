import sqlite3

def create_connection():
    conn = sqlite3.connect("rules.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY,
            rule_name TEXT,
            source_dir TEXT,
            dest_dir TEXT,
            file_attribute TEXT,
            comparison_operator TEXT,
            comparison_value TEXT,
            action_to_take TEXT
        );
        '''
    )
    conn.commit()
    conn.close()