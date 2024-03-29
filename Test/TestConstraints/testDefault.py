import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "ran_id" : "",
    "ran_create" : "TestRangeCreated",
    "ran_update" : "TestRangeUpdated",
    "ran_control" : 2,
    "ran_des" : "Descripción creada",
    "mem_id" : "",
    "mem_create" : "TestMemberCreated",
    "mem_update" : "TestMemberUpdated",
    "mem_datecreate" : "25/01/2100",
    "mem_dateupdate" : "26/01/2100",
    "ev_id" : "",
    "ev_create" : "TestEventCreated",
    "ev_update" : "TestEventUpdated",
    "ev_point" : 5,
    "ev_des" : "Descripción creada",
    "assist_id" : "",
    "assist_date" : "27/01/2100"
}

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()
permissions = Certificates()

@pytest.mark.asyncio
async def testConstraintsDefault_addRange(capfd):
    command = f"$addRange [{testData['ran_create']}, "\
              f"{testData['ran_control']}, {testData['ran_des']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["ran_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['ran_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_addMember(capfd):
    command = f"$addMember [{testData['mem_create']}, "\
              f"{testData['ran_create']}, "\
              f"{testData['mem_datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["mem_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['mem_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_addEvent(capfd):
    command = f"$addEvent [{testData['ev_create']}, "\
              f"{testData['ev_point']}, {testData['ev_des']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["ev_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['ev_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_addAssist(capfd):
    command = f"$addAssist [{testData['mem_create']}, "\
              f"{testData['ev_create']}, "\
              f"{testData['assist_date']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["assist_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['assist_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_updRangeId(capfd):
    command = f"$updRange:id [{testData['ran_id']}, "\
               f"{testData['ran_update']}, "\
               f"{testData['ran_control']}, "\
               f"{testData['ran_des']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("updRange:id", app.updateData,
                       Helpers.updStruct("range", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listMemberId_checkUpdRangeCascade(capfd):
    command = f"$listMember:id [{testData['mem_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['mem_id']}" in out
    assert f"{testData['mem_create']}" in out
    assert f"{testData['ran_update']}" in out
    assert f"{testData['mem_datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testConstraintsDefault_updMemberId(capfd):
    command = f"$updMember:id[{testData['mem_id']} ,"\
               f"{testData['mem_update']}, "\
               f"{testData['ran_update']}, "\
               f"{testData['mem_dateupdate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("updMember:id", app.updateData,
                       Helpers.updStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listAssistId_checkUpdMemberCascade(capfd):
    command = f"$listAssist:id [{testData['assist_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("assist", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Asistencias___** **___encontradas:___**\n" in out
    assert f"{testData['assist_id']}" in out
    assert f"{testData['mem_update']}" in out
    assert f"{testData['ev_create']}" in out
    assert f"{testData['assist_date'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testConstraintsDefault_updEventId(capfd):
    command = f"$updEvent:id[{testData['ev_id']}, "\
               f"{testData['ev_update']}, "\
               f"{testData['ev_point']}, "\
               f"{testData['ev_des']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("updEvent:id", app.updateData,
                       Helpers.updStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listAssistId_checkUpdEventCascade(capfd):
    command = f"$listAssist:id [{testData['assist_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("assist", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Asistencias___** **___encontradas:___**\n" in out
    assert f"{testData['assist_id']}" in out
    assert f"{testData['mem_update']}" in out
    assert f"{testData['ev_update']}" in out
    assert f"{testData['assist_date'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testConstraintsDefault_delRangeId(capfd):
    command = f"$delRange:id [{testData['ran_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("range", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listMemberId_checkDelRangeNone(capfd):
    command = f"$listMember:id [{testData['mem_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['mem_id']}" in out
    assert f"{testData['mem_update']}" in out
    assert "Ninguno" in out
    assert f"{testData['mem_datecreate'].replace('-','/')}" in out
    assert f"{testData['mem_dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testConstraintsDefault_delEventId(capfd):
    command = f"$delEvent:id [{testData['ev_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listAssistId_checkDelEventNone(capfd):
    command = f"$listAssist:id [{testData['assist_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("assist", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Asistencias___** **___encontradas:___**\n" in out
    assert f"{testData['assist_id']}" in out
    assert f"{testData['mem_update']}" in out
    assert "Ninguno" in out
    assert f"{testData['assist_date'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testConstraintsDefault_delMemberId(capfd):
    command = f"$delMember:id [{testData['mem_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listAssistId_checkDelMemberCascade(capfd):
    command = f"$listAssist:id [{testData['assist_id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("assist", ["id"]))
    out, _ = capfd.readouterr()
    assert f"El valor '{testData['assist_id']}' "\
            "ingresado en el campo "\
            "**_ID_** no fue encontrado en la "\
            "base de datos.\n" in out