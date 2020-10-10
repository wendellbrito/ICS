import mysql.connector

class Database(object):
    def __init__(self, user, passwd, host, db):
        self.__conn = mysql.connector.connect(
                user=user, password=passwd, host=host, database=db
        )

    def __concat(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i]
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_format(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += "'" + fields[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str


    def __concat_values(self, fields, values):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i] + " = '" + values[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __query_exec(self, query):
        db_dict = self.__conn.cursor(dictionary=True)
        db_dict.execute(query)
        return db_dict

    def __query_commit(self, query):
        db_dict = self.__query_exec(query)
        self.__conn.commit()
        db_dict.close()
    
    def __query_fetchall(self, query):
        db_dict = self.__query_exec(query)
        db_data = db_dict.fetchall()
        db_dict.close()
        return db_data

    def select(self, table, fields, where_fields = None, where_values = None,
            order_by = None, limit = None, offset = None):
        db_query = "SELECT " + self.__concat(fields) + " FROM " + table
        if (where_fields != None or where_values != None):
            db_query += " WHERE "
            db_query += self.__concat_values(where_fields, where_values) 
            where = True
        if (order_by != None):
            db_query += " ORDER BY " + order_by
        if (limit != None):
            db_query += " LIMIT " + limit
        if (offset != None):
            db_query += " OFFSET " + offset
        return self.__query_fetchall(db_query)

    def insert(self, table, fields, values):
        db_query = "INSERT INTO " + table + " (" 
        db_query += self.__concat(fields) + ") VALUES ("
        db_query += self.__concat_format(values) + ")" 
        self.__query_commit(db_query)

    def delete(self, table, where_fields, where_values):
        db_query = "DELETE FROM " + table + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def update(self, table, set_fields, set_values,
            where_fields, where_values):
        db_query = "UPDATE " + table + " SET " 
        db_query += self.__concat_values(set_fields, set_values) + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

