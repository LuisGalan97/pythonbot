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
async def testAssistParams_addAssist_invalidParams(capfd):
    commands = ["$addAssist[]",
                "$addAssist []",
                "$addAssist[,,,,]",
                "$addAssist [,,,,]",
                "$addAssist[,,,,]FILL",
                "$addAssist[,,,,] FILL",
                "$addAssist[,,,,]]FILL",
                "$addAssist [,,,,]] FILL",
                "$addAssist[[,,,,]FILL",
                "$addAssist [[,,,,] FILL",
                "$addAssist[[,,,,]]FILL",
                "$addAssist [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Evento, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_updAssistId_invalidParams(capfd):
    commands = ["$updAssist:id[]",
                "$updAssist:id []",
                "$updAssist:id[,,,,]",
                "$updAssist:id [,,,,]",
                "$updAssist:id[,,,,]FILL",
                "$updAssist:id[,,,,] FILL",
                "$updAssist:id[,,,,]]FILL",
                "$updAssist:id [,,,,]] FILL",
                "$updAssist:id[[,,,,]FILL",
                "$updAssist:id [[,,,,] FILL",
                "$updAssist:id[[,,,,]]FILL",
                "$updAssist:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Integrante, Evento, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_delAssistId_invalidParams(capfd):
    commands = ["$delAssist:id[,,,,]",
                "$delAssist:id [,,,,]",
                "$delAssist:id[,,,,]FILL",
                "$delAssist:id[,,,,] FILL",
                "$delAssist:id[,,,,]]FILL",
                "$delAssist:id [,,,,]] FILL",
                "$delAssist:id[[,,,,]FILL",
                "$delAssist:id [[,,,,] FILL",
                "$delAssist:id[[,,,,]]FILL",
                "$delAssist:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistId_invalidParams(capfd):
    commands = ["$listAssist:id[,,,,]",
                "$listAssist:id [,,,,]",
                "$listAssist:id[,,,,]FILL",
                "$listAssist:id[,,,,] FILL",
                "$listAssist:id[,,,,]]FILL",
                "$listAssist:id [,,,,]] FILL",
                "$listAssist:id[[,,,,]FILL",
                "$listAssist:id [[,,,,] FILL",
                "$listAssist:id[[,,,,]]FILL",
                "$listAssist:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("assist", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistMember_invalidParams(capfd):
    commands = ["$listAssist:member[,,,,]",
                "$listAssist:member [,,,,]",
                "$listAssist:member[,,,,]FILL",
                "$listAssist:member[,,,,] FILL",
                "$listAssist:member[,,,,]]FILL",
                "$listAssist:member [,,,,]] FILL",
                "$listAssist:member[[,,,,]FILL",
                "$listAssist:member [[,,,,] FILL",
                "$listAssist:member[[,,,,]]FILL",
                "$listAssist:member [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("assist", ["member"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistEvent_invalidParams(capfd):
    commands = ["$listAssist:event[,,,,]",
                "$listAssist:event [,,,,]",
                "$listAssist:event[,,,,]FILL",
                "$listAssist:event[,,,,] FILL",
                "$listAssist:event[,,,,]]FILL",
                "$listAssist:event [,,,,]] FILL",
                "$listAssist:event[[,,,,]FILL",
                "$listAssist:event [[,,,,] FILL",
                "$listAssist:event[[,,,,]]FILL",
                "$listAssist:event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("assist", ["event"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistDate_invalidParams(capfd):
    commands = ["$listAssist:date[]",
                "$listAssist:date []",
                "$listAssist:date[,,,,]",
                "$listAssist:date [,,,,]",
                "$listAssist:date[,,,,]FILL",
                "$listAssist:date[,,,,] FILL",
                "$listAssist:date[,,,,]]FILL",
                "$listAssist:date [,,,,]] FILL",
                "$listAssist:date[[,,,,]FILL",
                "$listAssist:date [[,,,,] FILL",
                "$listAssist:date[[,,,,]]FILL",
                "$listAssist:date [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistMemberEvent_invalidParams(capfd):
    commands = ["$listAssist:member&event[]",
                "$listAssist:member&event []",
                "$listAssist:member&event[,,,,]",
                "$listAssist:member&event [,,,,]",
                "$listAssist:member&event[,,,,]FILL",
                "$listAssist:member&event[,,,,] FILL",
                "$listAssist:member&event[,,,,]]FILL",
                "$listAssist:member&event [,,,,]] FILL",
                "$listAssist:member&event[[,,,,]FILL",
                "$listAssist:member&event [[,,,,] FILL",
                "$listAssist:member&event[[,,,,]]FILL",
                "$listAssist:member&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Evento_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistMemberDate_invalidParams(capfd):
    commands = ["$listAssist:member&date[]",
                "$listAssist:member&date []",
                "$listAssist:member&date[,,,,]",
                "$listAssist:member&date [,,,,]",
                "$listAssist:member&date[,,,,]FILL",
                "$listAssist:member&date[,,,,] FILL",
                "$listAssist:member&date[,,,,]]FILL",
                "$listAssist:member&date [,,,,]] FILL",
                "$listAssist:member&date[[,,,,]FILL",
                "$listAssist:member&date [[,,,,] FILL",
                "$listAssist:member&date[[,,,,]]FILL",
                "$listAssist:member&date [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistEventDate_invalidParams(capfd):
    commands = ["$listAssist:event&date[]",
                "$listAssist:event&date []",
                "$listAssist:event&date[,,,,]",
                "$listAssist:event&date [,,,,]",
                "$listAssist:event&date[,,,,]FILL",
                "$listAssist:event&date[,,,,] FILL",
                "$listAssist:event&date[,,,,]]FILL",
                "$listAssist:event&date [,,,,]] FILL",
                "$listAssist:event&date[[,,,,]FILL",
                "$listAssist:event&date [[,,,,] FILL",
                "$listAssist:event&date[[,,,,]]FILL",
                "$listAssist:event&date [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAssistParams_listAssistMemberEventDate_invalidParams(capfd):
    commands = ["$listAssist:member&event&date[]",
                "$listAssist:member&event&date []",
                "$listAssist:member&event&date[,,,,]",
                "$listAssist:member&event&date [,,,,]",
                "$listAssist:member&event&date[,,,,]FILL",
                "$listAssist:member&event&date[,,,,] FILL",
                "$listAssist:member&event&date[,,,,]]FILL",
                "$listAssist:member&event&date [,,,,]] FILL",
                "$listAssist:member&event&date[[,,,,]FILL",
                "$listAssist:member&event&date [[,,,,] FILL",
                "$listAssist:member&event&date[[,,,,]]FILL",
                "$listAssist:member&event&date [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Evento, Fecha 1, Fecha 2_]**\n" in out