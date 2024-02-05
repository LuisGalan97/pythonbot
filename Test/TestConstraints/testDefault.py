import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
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
    "mem_datecreate" : "25-01-2100",
    "mem_dateupdate" : "26-01-2100",
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testConstraintsDefault_addRange(capfd):
    command = f"$addRange [{testData['ran_create']}, "\
              f"{testData['ran_control']}, {testData['ran_des']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["ran_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['ran_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listRangeId(capfd):
    command = f"$listRange:id [{testData['ran_id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listRange:id", app.getDatas,
                     Helpers.getStruct("range", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Rangos___** **___encontrados:___**\n" in out
    assert f"{testData['ran_id']}" in out
    assert f"{testData['ran_create']}" in out
    assert f"{testData['ran_control']}" in out
    assert f"{testData['ran_des']}" in out

@pytest.mark.asyncio
async def testConstraintsDefault_addMember(capfd):
    command = f"$addMember [{testData['mem_create']}, "\
              f"{testData['ran_create']}, "\
              f"{testData['mem_datecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["mem_id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['mem_id']}\'.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listMemberId(capfd):
    command = f"$listMember:id [{testData['mem_id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['mem_id']}" in out
    assert f"{testData['mem_create']}" in out
    assert f"{testData['ran_create']}" in out
    assert f"{testData['mem_datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testConstraintsDefault_updRangeId(capfd):
    commands = [f"$updRange:id [{testData['ran_id']}, "\
                f"{testData['ran_update']}, "\
                f"{testData['ran_control']}, "\
                f"{testData['ran_des']}]"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testConstraintsDefault_listMemberId_checkUpdCascade(capfd):
    command = f"$listMember:id [{testData['mem_id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['mem_id']}" in out
    assert f"{testData['mem_create']}" in out
    assert f"{testData['ran_update']}" in out
    assert f"{testData['mem_datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out