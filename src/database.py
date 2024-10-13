import sqlite3

class SQLDatabase():
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("rules.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS rules (
                uuid VARCHAR(36) PRIMARY KEY,
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
        self.conn.commit()
    
    def insertRuleIntoDB(self, rule_data):
        self.cursor.execute(
            '''
            INSERT INTO rules (uuid, rule_name, source_dir, dest_dir, file_attribute, comparison_operator, comparison_value, action_to_take) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (rule_data['uuid'], rule_data['ruleName'], rule_data['sourceDir'], 
             rule_data['destDir'], rule_data['fileAttribute'], rule_data['comparisonOperator'], 
             rule_data['comparisonValue'], rule_data['actionToTake'])
        )
        self.conn.commit()
    
    def updateRuleInDB(self, rule_data):
        self.cursor.execute(
            '''
            UPDATE rules 
            SET rule_name=?, source_dir=?, dest_dir=?, file_attribute=?, comparison_operator=?, comparison_value=?, action_to_take=? 
            WHERE uuid=?
            ''',
            (rule_data['ruleName'], rule_data['sourceDir'], rule_data['destDir'], rule_data['fileAttribute'], rule_data['comparisonOperator'], rule_data['comparisonValue'], rule_data['actionToTake'], rule_data['uuid'])
        )
        self.conn.commit()
    
    def deleteRuleFromDB(self, rule_uuid):
        self.cursor.execute(
            'DELETE FROM rules WHERE uuid=?',
            (rule_uuid,)
        )
        self.conn.commit()
    
    def closeDB(self):
        if self.conn:
            self.conn.close()

    def loadDataFromDB(self):
        self.cursor.execute('SELECT * FROM rules')
        rows = self.cursor.fetchall()
        return [
            {
                'uuid': row[0],
                'ruleName': row[1],
                'sourceDir': row[2],
                'destDir': row[3],
                'fileAttribute': row[4],
                'comparisonOperator': row[5],
                'comparisonValue': row[6],
                'actionToTake': row[7],
            }
            for row in rows
        ]