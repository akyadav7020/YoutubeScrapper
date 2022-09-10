import pyodbc

def insert_unique_data(primary_column,table,data):
    try:
        mydb = pyodbc.connect('DRIVER={SQL Server};''SERVER=mydb708.database.windows.net;''DATABASE=my_DB1;''UID=root708;''PWD=root@123')
        cursor = mydb.cursor()
        cursor.execute("select {} from {}".format(primary_column,table)) #primary_key is unique column
        all_values_in_primary_column = (cursor.fetchall())
        all_values_list = set()
        for i in range(len(all_values_in_primary_column)):
            all_values_list.add(all_values_in_primary_column[i][0])
        input_value = data[list(data.keys())[1]] #need to select key carefully

        if input_value not in all_values_list:
            cursor.execute("insert into {} values('{}','{}','{}')".format(table,data['V_link'],data['Title'],data['thumbnail']))
            mydb.commit()
    except Exception as e:
        print("Not able to connect to the SERVER")


def create_unique_table(input_table_name):
    try:
        mydb = pyodbc.connect('DRIVER={SQL Server};''SERVER=mydb708.database.windows.net;''DATABASE=my_DB1;''UID=root708;''PWD=root@123')
        cursor = mydb.cursor()
        cursor.execute("select table_name from information_schema.tables")
        all_tables_name = (cursor.fetchall())
        all_tables_list = set()
        for i in range(len(all_tables_name)):
            all_tables_list.add(all_tables_name[i][0])

        if input_table_name not in all_tables_list:
            cursor.execute("create table {}(video_link varchar(100),title varchar(100), thumbnail_url varchar(100))".format(input_table_name))
            mydb.commit()
    except Exception as e:
        print("Not able to connect to the SERVER")
