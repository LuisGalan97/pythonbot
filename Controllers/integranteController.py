import sys
sys.path.insert(1, './Models')
from integranteModel import IntegranteModel
sys.path.insert(1, './Services')
from integranteService import IntegranteService
sys.path.insert(1, './DB')
from database import Database

class IntegranteController:
    def __init__(self, db : Database):
        self.__service = IntegranteService(db)

    def getIntegrantes(self):
        integrantes = self.__service.selectAll()
        if integrantes:
            data = []
            for integrante in integrantes:
                data.append(
                    {
                        "id" : integrante.getId(),
                        "name" : integrante.getName(),
                        "rango_id" : integrante.getRangoId(),
                        "datecreate" : integrante.getDateCreate(),
                        "dateupdate" : integrante.getDateUpdate()
                    })
            return data
        else:
            return False

    def getIntegrante(self, id):
        integrante = self.__service.select(id)
        if integrante:
            data = {
                "id" : integrante.getId(),
                "name" : integrante.getName(),
                "rango_id" : integrante.getRangoId(),
                "datecreate" : integrante.getDateCreate(),
                "dateupdate" : integrante.getDateUpdate()
            }
            return data
        else:
            return False
    
    def createIntegrante(self, name, rango_id, datecreate):
        integrante = IntegranteModel(None, name, rango_id, datecreate, None)
        result = self.__service.insert(integrante)
        if result:
            return True
        else:
            return False
    
    def updateIntegrante(self, id, name, rango_id, dateupdate):
        integrante = IntegranteModel(id, name, rango_id, None, dateupdate)
        result = self.__service.update(integrante)
        if result:
            return True
        else:
            return False
    
    def deleteIntegrante(self, id):
        result = self.__service.delete(id)
        if result:
            return True
        else:
            return False
    