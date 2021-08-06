import sqlite3


def get_conn():
    conn = sqlite3.connect('db.db')
    return conn


def init_db():
    conn = get_conn()
    with conn:
        with open('sql/init_db.sql', 'r') as f:
            init_sql = '\n'.join(f.readlines())
            c = conn.cursor()
            c.execute(init_sql)


def save(id, _url, token):

    sql = f"""
    INSERT INTO urls
    (id, url, token)
    VALUES
    ({id}, '{_url}', '{token}')
    """
    conn = get_conn()
    with conn:
        print(sql)
        conn.cursor().execute(sql)


def find_by_url(url):
    sql = f"""
    SELECT * FROM urls WHERE url = '{url}'
    """
    conn = get_conn()
    with conn:
        cur = conn.cursor()
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        if rows:
            return {
                "id": rows[0][0],
                "url": rows[0][1],
                "token": rows[0][2]
            }


def find_by_token(token):
    sql = f"""
        SELECT * FROM urls WHERE token = '{token}'
        """
    conn = get_conn()
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if rows:
            return {
                "id": rows[0][0],
                "url": rows[0][1],
                "token": rows[0][2]
            }


if __name__ == "__main__":
    init_db()
