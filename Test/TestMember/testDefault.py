import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "namecreate" : "TestMemberCreated",
    "nameupdate" : "TestMemberUpdated",
    "nameexist" : "Avalonicus",
    "rancreate" : "General de alianza",
    "ranupdate" : "General",
    "ranoexist" : "Range-[noexist]",
    "prinnoexist" :"Principal-[noexist]",
    "datecreate" : "25/01/2100",
    "dateupdate" : "26/01/2100"
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
async def testMemberDefault_addMember(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_exist(capfd):
    commands = [f"$addMember[{testData['namecreate']},"\
                f"{testData['rancreate']},"\
                f"{testData['datecreate']}]",
                f"$addMember [{testData['namecreate']}, "\
                f"{testData['rancreate']}, "\
                f"{testData['datecreate']}]",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ]",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ]FILL",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("member"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_add(capfd):
    command = f"$listMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_add(capfd):
    command = f"$listMember:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_nameExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameexist']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameexist']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"\'{testData['nameexist']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember(capfd):
    commands = [f"$listMember",
                f"$listMember ",
                f"$listMemberFILL",
                f"$listMember FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember", app.getDatas,
                         Helpers.getStruct("member"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ] ",
                f"$listMember:id [ {testData['id']} ]FILL",
                f"$listMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ] ",
                f"$listMember:name [ {testData['nameupdate']} ]FILL",
                f"$listMember:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ] ",
                f"$listMember:range [ {testData['ranupdate']} ]FILL",
                f"$listMember:range [ {testData['ranupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] ",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]FILL",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember_e(capfd):
    commands = [f"$listMember"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("member"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_e(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("member", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_e(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_e(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_e(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("member",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember_eIncomplete(capfd):
    commands = [f"$listMember"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("member"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listMember** **> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_eIncomplete(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("member", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_eIncomplete(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_eIncomplete(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:range** **[**{testData['ranupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_eIncomplete(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("member",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listMember:date** "\
                   "**[**" + \
                   testData['datecreate'] + ", " + \
                   testData['datecreate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_rangeNoExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['ranoexist']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['ranoexist']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_rangeNoExist(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranoexist']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranoexist']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_principalNoExist(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, "\
              f"{testData['prinnoexist']}, "\
              f"{testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    assert f"El valor '{testData['prinnoexist']}' "\
            "ingresado en el campo "\
            "**_Principal_** no fue encontrado en la "\
            "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_principalNoExist(capfd):
    commands = [f"$updMember:id[{testData['id']},"\
                f"{testData['nameupdate']},"\
                f"{testData['ranupdate']},"\
                f"{testData['prinnoexist']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, "\
                f"{testData['prinnoexist']}, "\
                f"{testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['prinnoexist']}' "\
                "ingresado en el campo "\
                "**_Principal_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_principalNoExist(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},"\
                f"{testData['prinnoexist']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, "\
                f"{testData['prinnoexist']}, "\
                f"{testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['prinnoexist']} , "\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['prinnoexist']}' "\
                "ingresado en el campo "\
                "**_Principal_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_principalAutoRef(capfd):
    commands = [f"$updMember:id[{testData['id']},"\
                f"{testData['nameupdate']},"\
                f"{testData['ranupdate']},"\
                f"{testData['nameupdate']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, "\
                f"{testData['nameupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['nameupdate']}' "\
                "ingresado en el campo "\
                "**_Principal_** no puede hacer referencia "\
                "al mismo ___integrante___ que desea "\
                "actualizar.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_principalAutoref(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},"\
                f"{testData['nameupdate']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, "\
                f"{testData['nameupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['nameupdate']}' "\
                "ingresado en el campo "\
                "**_Principal_** no puede hacer referencia "\
                "al mismo ___integrante___ que desea "\
                "actualizar.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberId(capfd):
    command = f"$delMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_delName(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberName(capfd):
    command = f"$delMember:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delMember:name", app.deleteData,
                       Helpers.delStruct("member", "name"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_principal(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, "\
              f"{testData['nameexist']}, "\
              f"{testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_addPrincipal(capfd):
    command = f"$listMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['nameexist']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_addPrincipal(capfd):
    command = f"$listMember:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['nameexist']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_principal(capfd):
    commands = [f"$updMember:id[{testData['id']},"\
                f"{testData['nameupdate']},"\
                f"{testData['rancreate']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['nameupdate']}, "\
                f"{testData['rancreate']}, "\
                f"{testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , "\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_updIdPrincipal(capfd):
    command = f"$listMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['nameupdate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert f"{testData['dateupdate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_updIdPrincipal(capfd):
    command = f"$listMember:name [{testData['nameupdate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['nameupdate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert f"{testData['dateupdate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_principal(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},"\
                f"{testData['nameexist']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, "\
                f"{testData['nameexist']},"\
                f"{testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameexist']},"\
                f"{testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameexist']},"\
                f"{testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , "\
                f"{testData['nameexist']},"\
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_updNamePrincipal(capfd):
    command = f"$listMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['nameupdate']}" in out
    assert f"{testData['ranupdate']}" in out
    assert f"{testData['nameexist']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_updNamePrincipal(capfd):
    command = f"$listMember:name [{testData['nameupdate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['nameupdate']}" in out
    assert f"{testData['ranupdate']}" in out
    assert f"{testData['nameexist']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberId_principal(capfd):
    command = f"$delMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_rangeNoExist(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['ranoexist']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, permissions, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    assert f"El valor '{testData['ranoexist']}' "\
            "ingresado en el campo "\
            "**_Rango_** no fue encontrado en la "\
            "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_idNoExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['id']}' "\
                "ingresado en el campo "\
                "**_ID_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_nameNoExist(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['nameupdate']}' "\
                "ingresado en el campo "\
                "**_Nombre_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberId_idNoExist(capfd):
    commands = [f"$delMember:id[{testData['id']}]",
                f"$delMember:id [{testData['id']}]",
                f"$delMember:id [ {testData['id']} ]",
                f"$delMember:id [ {testData['id']} ]FILL",
                f"$delMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['id']}' "\
                "ingresado en el campo "\
                "**_ID_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberName_nameNoExist(capfd):
    commands = [f"$delMember:name[{testData['namecreate']}]",
                f"$delMember:name [{testData['namecreate']}]",
                f"$delMember:name [ {testData['namecreate']} ]",
                f"$delMember:name [ {testData['namecreate']} ]FILL",
                f"$delMember:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['namecreate']}' "\
                "ingresado en el campo "\
                "**_Nombre_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_idNoExist(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ] ",
                f"$listMember:id [ {testData['id']} ]FILL",
                f"$listMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['id']}' "\
                "ingresado en el campo "\
                "**_ID_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_nameNoExist(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ] ",
                f"$listMember:name [ {testData['nameupdate']} ]FILL",
                f"$listMember:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['nameupdate']}' "\
                "ingresado en el campo "\
                "**_Nombre_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_rangeNoExist(capfd):
    commands = [f"$listMember:range[{testData['ranoexist']}]",
                f"$listMember:range [{testData['ranoexist']}]",
                f"$listMember:range [ {testData['ranoexist']} ] ",
                f"$listMember:range [ {testData['ranoexist']} ]FILL",
                f"$listMember:range [ {testData['ranoexist']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_dateNoExist(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] ",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]FILL",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___integrantes___ "\
               "para la consulta realizada.\n" in out