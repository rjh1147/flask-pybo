import cx_Oracle

connection = cx_Oracle.connect(user="admin", password="!$Khu20022002", dsn="dboracle_high")
#oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@' + cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
#oracle_connection_string = 'oracle+cx_oracle://admin:!$Khu20022002@dboracle_high'
cursor = connection.cursor()

# Create a table

cursor.execute("""begin
                     execute immediate 'drop table pytab';
                     exception when others then if sqlcode <> -942 then raise; end if;
                  end;""")
cursor.execute("create table pytab (id number, data varchar2(20))")

# Insert some rows

rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cursor.executemany("insert into pytab(id, data) values (:1, :2)", rows)

# connection.commit()  # uncomment to make data persistent

# Now query the rows back
for row in cursor.execute('select * from pytab'):
    print(row)
