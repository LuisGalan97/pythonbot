import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMember_invalidParams(capfd):
    commands = ["$listPointMember[]",
                "$listPointMember []",
                "$listPointMember[,,,,]",
                "$listPointMember [,,,,]",
                "$listPointMember[,,,,]FILL",
                "$listPointMember[,,,,] FILL",
                "$listPointMember[,,,,]]FILL",
                "$listPointMember [,,,,]] FILL",
                "$listPointMember[[,,,,]FILL",
                "$listPointMember [[,,,,] FILL",
                "$listPointMember[[,,,,]]FILL",
                "$listPointMember [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberId_invalidParams(capfd):
    commands = ["$listPointMember:id[]",
                "$listPointMember:id []",
                "$listPointMember:id[,,,,]",
                "$listPointMember:id [,,,,]",
                "$listPointMember:id[,,,,]FILL",
                "$listPointMember:id[,,,,] FILL",
                "$listPointMember:id[,,,,]]FILL",
                "$listPointMember:id [,,,,]] FILL",
                "$listPointMember:id[[,,,,]FILL",
                "$listPointMember:id [[,,,,] FILL",
                "$listPointMember:id[[,,,,]]FILL",
                "$listPointMember:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberName_invalidParams(capfd):
    commands = ["$listPointMember:name[]",
                "$listPointMember:name []",
                "$listPointMember:name[,,,,]",
                "$listPointMember:name [,,,,]",
                "$listPointMember:name[,,,,]FILL",
                "$listPointMember:name[,,,,] FILL",
                "$listPointMember:name[,,,,]]FILL",
                "$listPointMember:name [,,,,]] FILL",
                "$listPointMember:name[[,,,,]FILL",
                "$listPointMember:name [[,,,,] FILL",
                "$listPointMember:name[[,,,,]]FILL",
                "$listPointMember:name [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberRange_invalidParams(capfd):
    commands = ["$listPointMember:range[]",
                "$listPointMember:range []",
                "$listPointMember:range[,,,,]",
                "$listPointMember:range [,,,,]",
                "$listPointMember:range[,,,,]FILL",
                "$listPointMember:range[,,,,] FILL",
                "$listPointMember:range[,,,,]]FILL",
                "$listPointMember:range [,,,,]] FILL",
                "$listPointMember:range[[,,,,]FILL",
                "$listPointMember:range [[,,,,] FILL",
                "$listPointMember:range[[,,,,]]FILL",
                "$listPointMember:range [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberEvent_invalidParams(capfd):
    commands = ["$listPointMember:event[]",
                "$listPointMember:event []",
                "$listPointMember:event[,,,,]",
                "$listPointMember:event [,,,,]",
                "$listPointMember:event[,,,,]FILL",
                "$listPointMember:event[,,,,] FILL",
                "$listPointMember:event[,,,,]]FILL",
                "$listPointMember:event [,,,,]] FILL",
                "$listPointMember:event[[,,,,]FILL",
                "$listPointMember:event [[,,,,] FILL",
                "$listPointMember:event[[,,,,]]FILL",
                "$listPointMember:event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberIdEvent_invalidParams(capfd):
    commands = ["$listPointMember:id&event[]",
                "$listPointMember:id&event []",
                "$listPointMember:id&event[,,,,]",
                "$listPointMember:id&event [,,,,]",
                "$listPointMember:id&event[,,,,]FILL",
                "$listPointMember:id&event[,,,,] FILL",
                "$listPointMember:id&event[,,,,]]FILL",
                "$listPointMember:id&event [,,,,]] FILL",
                "$listPointMember:id&event[[,,,,]FILL",
                "$listPointMember:id&event [[,,,,] FILL",
                "$listPointMember:id&event[[,,,,]]FILL",
                "$listPointMember:id&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberNameEvent_invalidParams(capfd):
    commands = ["$listPointMember:name&event[]",
                "$listPointMember:name&event []",
                "$listPointMember:name&event[,,,,]",
                "$listPointMember:name&event [,,,,]",
                "$listPointMember:name&event[,,,,]FILL",
                "$listPointMember:name&event[,,,,] FILL",
                "$listPointMember:name&event[,,,,]]FILL",
                "$listPointMember:name&event [,,,,]] FILL",
                "$listPointMember:name&event[[,,,,]FILL",
                "$listPointMember:name&event [[,,,,] FILL",
                "$listPointMember:name&event[[,,,,]]FILL",
                "$listPointMember:name&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberRangeEvent_invalidParams(capfd):
    commands = ["$listPointMember:range&event[]",
                "$listPointMember:range&event []",
                "$listPointMember:range&event[,,,,]",
                "$listPointMember:range&event [,,,,]",
                "$listPointMember:range&event[,,,,]FILL",
                "$listPointMember:range&event[,,,,] FILL",
                "$listPointMember:range&event[,,,,]]FILL",
                "$listPointMember:range&event [,,,,]] FILL",
                "$listPointMember:range&event[[,,,,]FILL",
                "$listPointMember:range&event [[,,,,] FILL",
                "$listPointMember:range&event[[,,,,]]FILL",
                "$listPointMember:range&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Evento, Fecha 1, Fecha 2_]**\n" in out