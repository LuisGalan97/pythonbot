import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from eventoModel import EventoModel

class EventoService:
    def __init__(self, db : Database):
        self.db = db

    def select(self, id):
        self.db.start_connection()
        data = self.db.execute_query("SELECT * FROM eventos WHERE id = ?", (id,))
        self.db.close_connection()
        if isinstance(data, list):
            for row in data:
                evento = EventoModel(row[0], row[1], row[2], row[3])
            return evento
        else:
            return False

    def selectAll(self):
        self.db.start_connection()
        data = self.db.execute_query("SELECT * FROM eventos")
        self.db.close_connection()
        if isinstance(data, list):
            eventos = []
            for row in data:
                eventos.append(EventoModel(row[0], row[1], row[2], row[3]))
            return eventos
        else:
            return False

    def insert(self, evento : EventoModel):
        self.db.start_connection()
        data = self.db.execute_query("INSERT INTO \
        eventos (name, points, description) \
        VALUES (?, ?, ?)", 
        (evento.getName(), evento.getPoints(), evento.getDescription(),))
        self.db.close_connection()
        return(data)

    def update(self, evento: EventoModel):
        self.db.start_connection()
        data = self.db.execute_query("UPDATE eventos \
        SET name = ?, points = ?, description = ? \
        WHERE id = ?", 
        (evento.getName(), 
         evento.getPoints(), 
         evento.getDescription(), 
         evento.getId(),))
        self.db.close_connection()
        return(data)

    def delete(self, evento: EventoModel):
        self.db.start_connection()
        data = self.db.execute_query("DELETE FROM eventos \
        WHERE id = ?", 
        (evento.getId(),))
        self.db.close_connection()
        return(data)
