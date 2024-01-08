import os
import sqlite3 as sql

class Database:
    def __init__(self, dbName):
        self.conn = None
        self.dbName = dbName
        self.exist = True if os.path.exists("./DB/"+dbName) else False
        self.success = self.start_connection()
                       
    def getExist(self):
        return self.exist
    
    def getSuccess(self):
        return self.success

    def getDBName(self):
        return self.dbName

    def removeDB(self):
        try:
            os.remove("./DB/"+self.dbName)
            print(f"-> La base de datos '{self.dbName}' se ha eliminado correctamente.")
            return True
        except Exception as ex:
            print(f"-> Error al intentar eliminar la base de datos '{self.dbName}' : '{str(ex)}'.")
            return False

    def check_connection(self):
        try:
            self.conn.execute("SELECT 1")
            return True
        except Exception as ex:
            return False

    def start_connection(self):
        try:
            if not self.check_connection():
                self.conn = sql.connect("./DB/"+self.dbName)
                self.cursor = self.conn.cursor()
                print(f"-> La conexion con la base de datos '{self.dbName}' fue inicializada con exito.")
                return True
            else:
                print(f"-> La conexion con la base de datos '{self.dbName}' ya existe.")
                return True
        except Exception as ex:
            print(f"-> Error al intentar conectar con la base de datos '{self.dbName}' : '{str(ex)}'.")
            return False
    
    def close_connection(self):
        try:
            if self.check_connection():
                self.conn.close()
                print(f"-> Desconectado satisfactoriamente de la base de datos '{self.dbName}'.")
                return True
            else:
                print(f"-> Ya se encuentra desconectado de la base de datos '{self.dbName}'.")
                return True
        except Exception as ex:
            print(f"-> Error al intentar desconectar de la base de datos '{self.dbName}' : '{str(ex)}'.")
            return False

    def execute_script(self, script):
        try: 
            if self.check_connection():
                with open(script) as file:
                    sql_script = file.read()
                self.cursor.executescript(sql_script)
                self.conn.commit()
                print(f"-> El script '{script}' se ha cargado satisfactoriamente en la base de datos '{self.dbName}'.")
                return True
            else:
                print(f"-> No fue posible cargar el script '{script}' debido a una ausencia de conexion con la base de datos '{self.dbName}'.")
                return False
        except Exception as ex:
            print(f"-> Error al intentar cargar el script '{script}' en la base de datos '{self.dbName}' : '{str(ex)}'.")
            return False

    def execute_query(self, query):
        try:
            if self.check_connection():
                self.cursor.execute(query)
                self.conn.commit()
                result = self.cursor.fetchall()
                print(f"-> La consulta '{query.split()[0]}' se ha realizado satisfactoriamente en la base de datos '{self.dbName}'.")
                return True if not result else result
            else: 
                print(f"-> No fue posible realizar la consulta '{query.split()[0]}' debido a una ausencia de conexion con la base de datos '{self.dbName}'.")
                return False
        except Exception as ex:
            print(f"-> Error al intentar realizar la consulta '{query.split()[0]}' en la base de datos '{self.dbName}' : '{str(ex)}'.")
            return False

db = Database("avalon.db")
if db.getSuccess():
    if not db.getExist():
        if db.execute_script("./SQL/avalon-lite.sql") and db.execute_script("./SQL/data.sql"):
            print(f"-> Nueva base de datos '{db.getDBName()}' creada satisfactoriamente.")
        else:
            print(f"-> Ocurrio un error al intentar crear la base de datos '{db.getDBName()}'.")
            db.close_connection()
            db.removeDB()
    else:
        print("-> No se han realizado modificaciones al contenido actual de la base de datos.")