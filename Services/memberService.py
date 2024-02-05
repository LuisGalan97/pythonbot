from DB.database import Database
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel

class MemberService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "r.id AS rango_id, "\
            "r.nombre AS rango_name, "\
            "r.control AS rango_control, "\
            "r.descripcion AS rango_description, "\
            "i.id, "\
            "i.nombre AS name, "\
            "strftime('%d/%m/%Y', i.fechacreacion) AS datecreate, "\
            "strftime('%d/%m/%Y', i.fechamodificacion) AS dateupdate "\
        "FROM integrantes i "\
        "LEFT JOIN rangos r ON r.id = i.rango_id"
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(self.__selectQuery)
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.id = ?",
                                           (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.nombre = ?",
                                           (target["name"],))
        elif "rango_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.rango_id = ?",
                                           (target["rango_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.fechacreacion BETWEEN "\
                                            "? AND ?",
                                           (target["date_1"],
                                            target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            integrantes = []
            for row in data:
                rango = RangeModel(row[0], row[1], row[2], row[3])
                integrante = MemberModel(row[4], row[5], rango, row[6],
                                             row[7])
                integrantes.append(integrante)
            return integrantes
        else:
            return data

    def insert(self, integrante : MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "integrantes (nombre, rango_id, fechacreacion) "\
        "VALUES (?, ?, ?)",
        (integrante.getName(),
        integrante.getRango().getId(),
        integrante.getDateCreate(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, integrante: MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE integrantes "\
        "SET nombre = ?, rango_id = ?, fechamodificacion = ? "\
        "WHERE id = ?",
        (integrante.getName(),
        integrante.getRango().getId(),
        integrante.getDateUpdate(),
        integrante.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, integrante: MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM integrantes "\
        "WHERE id = ?",
        (integrante.getId(),))
        self.__db.close_connection()
        return data