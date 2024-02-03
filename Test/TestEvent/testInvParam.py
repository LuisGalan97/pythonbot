import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addEvent_invalidParams(capfd):
    commands = ["$addEvent[]",
                "$addEvent []",
                "$addEvent[,,,,]",
                "$addEvent [,,,,]",
                "$addEvent[,,,,]FILL",
                "$addEvent[,,,,] FILL",
                "$addEvent[,,,,]]FILL",
                "$addEvent [,,,,]] FILL",
                "$addEvent[[,,,,]FILL",
                "$addEvent [[,,,,] FILL",
                "$addEvent[[,,,,]]FILL",
                "$addEvent [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Puntos, Descripción_]**\n" in out

@pytest.mark.asyncio
async def test_updEventId_invalidParams(capfd):
    commands = ["$updEvent:id[]",
                "$updEvent:id []",
                "$updEvent:id[,,,,]",
                "$updEvent:id [,,,,]",
                "$updEvent:id[,,,,]FILL",
                "$updEvent:id[,,,,] FILL",
                "$updEvent:id[,,,,]]FILL",
                "$updEvent:id [,,,,]] FILL",
                "$updEvent:id[[,,,,]FILL",
                "$updEvent:id [[,,,,] FILL",
                "$updEvent:id[[,,,,]]FILL",
                "$updEvent:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Nombre, Puntos, Descripción_]**\n" in out

@pytest.mark.asyncio
async def test_updEventName_invalidParams(capfd):
    commands = ["$updEvent:name[]",
                "$updEvent:name []",
                "$updEvent:name[,,,,]",
                "$updEvent:name [,,,,]",
                "$updEvent:name[,,,,]FILL",
                "$updEvent:name[,,,,] FILL",
                "$updEvent:name[,,,,]]FILL",
                "$updEvent:name [,,,,]] FILL",
                "$updEvent:name[[,,,,]FILL",
                "$updEvent:name [[,,,,] FILL",
                "$updEvent:name[[,,,,]]FILL",
                "$updEvent:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Puntos, Descripción_]**\n" in out

@pytest.mark.asyncio
async def test_delEventId_invalidParams(capfd):
    commands = ["$delEvent:id[,,,,]",
                "$delEvent:id [,,,,]",
                "$delEvent:id[,,,,]FILL",
                "$delEvent:id[,,,,] FILL",
                "$delEvent:id[,,,,]]FILL",
                "$delEvent:id [,,,,]] FILL",
                "$delEvent:id[[,,,,]FILL",
                "$delEvent:id [[,,,,] FILL",
                "$delEvent:id[[,,,,]]FILL",
                "$delEvent:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:id", app.deleteData,
                           Helpers.delStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def test_delEventName_invalidParams(capfd):
    commands = ["$delEvent:name[,,,,]",
                "$delEvent:name [,,,,]",
                "$delEvent:name[,,,,]FILL",
                "$delEvent:name[,,,,] FILL",
                "$delEvent:name[,,,,]]FILL",
                "$delEvent:name [,,,,]] FILL",
                "$delEvent:name[[,,,,]FILL",
                "$delEvent:name [[,,,,] FILL",
                "$delEvent:name[[,,,,]]FILL",
                "$delEvent:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:name", app.deleteData,
                           Helpers.delStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out

@pytest.mark.asyncio
async def test_listEventId_invalidParams(capfd):
    commands = ["$listEvent:id[,,,,]",
                "$listEvent:id [,,,,]",
                "$listEvent:id[,,,,]FILL",
                "$listEvent:id[,,,,] FILL",
                "$listEvent:id[,,,,]]FILL",
                "$listEvent:id [,,,,]] FILL",
                "$listEvent:id[[,,,,]FILL",
                "$listEvent:id [[,,,,] FILL",
                "$listEvent:id[[,,,,]]FILL",
                "$listEvent:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("evento", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def test_listEventName_invalidParams(capfd):
    commands = ["$listEvent:name[,,,,]",
                "$listEvent:name [,,,,]",
                "$listEvent:name[,,,,]FILL",
                "$listEvent:name[,,,,] FILL",
                "$listEvent:name[,,,,]]FILL",
                "$listEvent:name [,,,,]] FILL",
                "$listEvent:name[[,,,,]FILL",
                "$listEvent:name [[,,,,] FILL",
                "$listEvent:name[[,,,,]]FILL",
                "$listEvent:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("evento", ["name"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out