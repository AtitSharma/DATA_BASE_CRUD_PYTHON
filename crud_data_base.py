import psycopg2
hostname='localhost'
database='demo'
username='atitsharma'
pwd='root'
port_id=5432
conn=None
cur=None

conn=psycopg2.connect(  
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id  
    )
cur=conn.cursor()
conn.commit()

    
class Main:

    def __init__(self):
        pass
    
    def create_table(self):
        values=self.__dict__.keys()
        table_name=self.__class__.__name__
        table_name=table_name.lower()
        new_values=[str(i) for i in values]
        my_string=''
        for i in new_values:
            my_string+=f'{i} varchar(20)'
            my_string+=','
        create_script='''
        CREATE TABLE IF NOT EXISTS {0}({1})
        '''.format(table_name,my_string[:-1])
        cur.execute(create_script)
        conn.commit()
        
    
    def insert(self,**data):
        datas=self.__dict__.values()
        my_datas_values=[str(i) for i in datas]
        my_datas_keys=[str(i) for i in self.__dict__.keys()]
        table_name=self.__class__.__name__.lower()
        keys_string=''
        for i in my_datas_keys:
            keys_string+=i
            keys_string+=','
        values_string=''
        for j in my_datas_values:
            values_string+=f"'{j}'"
            values_string+=","
        try:     
            insert_script='INSERT INTO {0}({1}) VALUES({2});'.format(table_name,keys_string[:-1],values_string[:-1])
        except Exception as e:
            print(e)
            print("Make sure to create table first")
            
        cur.execute(insert_script)
        conn.commit()
    
    def update(self,**newdata):
        
        pass
    
    def delete(self):
        values=self.__dict__
        id=values.get('id')
        table_name=self.__class__.__name__.lower()
        id=f"'{id}'"
        delete_script='DELETE FROM {0} WHERE id={1};'.format(table_name,id)
        cur.execute(delete_script)
        conn.commit()
    
    
    @classmethod
    def drop_table(cls):
        table_name=cls.__name__.lower()
        drop_table_script='DROP TABLE {0};'.format(table_name)
        try:    
            cur.execute(drop_table_script)
            conn.commit()
        except Exception as e:
            print(e)
            print(f"No table with name {table_name}")
            
        


class Student(Main):
    def __init__(self,id,name,grade):
        super().__init__()
        self.id=id
        self.name=name
        self.grade=grade
        
s=Student(2,"StitSharma",15)
s.create_table()
# s.insert()
# 
s.delete()


if cur is not None:
    cur.close()
if conn is not None:
    conn.close()
       