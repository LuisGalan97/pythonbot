import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()
permissions = Certificates()

@pytest.mark.asyncio
async def testRangeParams_addRange_invalidParams(capfd):
    commands = ["$addRange[]",
                "$addRange []",
                "$addRange[,,,,]",
                "$addRange [,,,,]",
                "$addRange[,,,,]FILL",
                "$addRange[,,,,] FILL",
                "$addRange[,,,,]]FILL",
                "$addRange [,,,,]] FILL",
                "$addRange[[,,,,]FILL",
                "$addRange [[,,,,] FILL",
                "$addRange[[,,,,]]FILL",
                "$addRange [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("range"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_updRangeId_invalidParams(capfd):
    commands = ["$updRange:id[]",
                "$updRange:id []",
                "$updRange:id[,,,,]",
                "$updRange:id [,,,,]",
                "$updRange:id[,,,,]FILL",
                "$updRange:id[,,,,] FILL",
                "$updRange:id[,,,,]]FILL",
                "$updRange:id [,,,,]] FILL",
                "$updRange:id[[,,,,]FILL",
                "$updRange:id [[,,,,] FILL",
                "$updRange:id[[,,,,]]FILL",
                "$updRange:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_updRangeName_invalidParams(capfd):
    commands = ["$updRange:name[]",
                "$updRange:name []",
                "$updRange:name[,,,,]",
                "$updRange:name [,,,,]",
                "$updRange:name[,,,,]FILL",
                "$updRange:name[,,,,] FILL",
                "$updRange:name[,,,,]]FILL",
                "$updRange:name [,,,,]] FILL",
                "$updRange:name[[,,,,]FILL",
                "$updRange:name [[,,,,] FILL",
                "$updRange:name[[,,,,]]FILL",
                "$updRange:name [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_delRangeId_invalidParams(capfd):
    commands = ["$delRange:id[,,,,]",
                "$delRange:id [,,,,]",
                "$delRange:id[,,,,]FILL",
                "$delRange:id[,,,,] FILL",
                "$delRange:id[,,,,]]FILL",
                "$delRange:id [,,,,]] FILL",
                "$delRange:id[[,,,,]FILL",
                "$delRange:id [[,,,,] FILL",
                "$delRange:id[[,,,,]]FILL",
                "$delRange:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_delRangeName_invalidParams(capfd):
    commands = ["$delRange:name[,,,,]",
                "$delRange:name [,,,,]",
                "$delRange:name[,,,,]FILL",
                "$delRange:name[,,,,] FILL",
                "$delRange:name[,,,,]]FILL",
                "$delRange:name [,,,,]] FILL",
                "$delRange:name[[,,,,]FILL",
                "$delRange:name [[,,,,] FILL",
                "$delRange:name[[,,,,]]FILL",
                "$delRange:name [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_listRangeId_invalidParams(capfd):
    commands = ["$listRange:id[,,,,]",
                "$listRange:id [,,,,]",
                "$listRange:id[,,,,]FILL",
                "$listRange:id[,,,,] FILL",
                "$listRange:id[,,,,]]FILL",
                "$listRange:id [,,,,]] FILL",
                "$listRange:id[[,,,,]FILL",
                "$listRange:id [[,,,,] FILL",
                "$listRange:id[[,,,,]]FILL",
                "$listRange:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("range", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testRangeParams_listRangeName_invalidParams(capfd):
    commands = ["$listRange:name[,,,,]",
                "$listRange:name [,,,,]",
                "$listRange:name[,,,,]FILL",
                "$listRange:name[,,,,] FILL",
                "$listRange:name[,,,,]]FILL",
                "$listRange:name [,,,,]] FILL",
                "$listRange:name[[,,,,]FILL",
                "$listRange:name [[,,,,] FILL",
                "$listRange:name[[,,,,]]FILL",
                "$listRange:name [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("range", ["name"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out