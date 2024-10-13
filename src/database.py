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
            id VARCHAR(36) PRIMARY KEY,
            rule_name VARCHAR(255),
            source_dir VARCHAR(255),
            dest_dir VARCHAR(255),
            file_attribute VARCHAR(255),
            comparison_operator VARCHAR(10),
            comparison_value TEXT,
            action_to_take TEXT
        );
        '''
    )
    conn.commit()
    conn.close()