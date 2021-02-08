import pymysql

def get_columns(cursor, table_schema, table_name):
    sql = '''select column_name from information_SCHEMA.COLUMNS where table_schema="{}" and table_name = "{}"'''.format(table_schema, table_name)
    cursor.execute(sql)
    raw_columns = cursor.fetchall()
    return set(map(lambda a: next(iter(a.values())), raw_columns))


def main():
    user_name, password, host, port = "username", "password", "dbhost", 8888
    schema, table_name, charset = "dbschema", "tablename", "utf8"

    database = pymysql.connect(user=user_name, passwd=password, host=host, port=port, db=schema, charset=charset)
    cursor = database.cursor(pymysql.cursors.DictCursor)

    columns = get_columns(cursor, schema, table_name)
    print(columns)

if __name__ == "__main__":
    main()
