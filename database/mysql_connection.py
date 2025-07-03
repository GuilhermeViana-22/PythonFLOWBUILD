import mysql.connector


class MySQLConnection:
    """Classe simples para gerenciar conexões com o MySQL."""

    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
        )
        return self.conn

    def execute(self, query: str, params=None):
        if self.conn is None:
            raise RuntimeError("Conexão não iniciada. Chame connect() primeiro.")
        cur = self.conn.cursor(dictionary=True)
        cur.execute(query, params or [])
        return cur

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
