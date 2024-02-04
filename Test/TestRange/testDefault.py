import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "namecreate" : "TestRangeCreated",
    "nameupdate" : "TestRangeUpdated",
    "nameexist" : "General de alianza",
    "controlcreate" : 2,
    "controlupdate" : 3,
    "descreate" : "Descripción creada",
    "desupdate" : "Descripción modificada"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testDef_addRange(capfd):
    command = f"$addRange [{testData['namecreate']}, "\
              f"{testData['controlcreate']}, {testData['descreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("rango"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testDef_addRange_exist(capfd):
    commands = [f"$addRange[{testData['namecreate']},"\
               f"{testData['controlcreate']},"\
               f"{testData['descreate']}]",
               f"$addRange [{testData['namecreate']}, "\
               f"{testData['controlcreate']}, "\
               f"{testData['descreate']}]",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ]",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ]FILL ",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listRangeId_add(capfd):
    command = f"$listRange:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listRange:id", app.getDatas,
                     Helpers.getStruct("rango", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Rangos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['controlcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testDef_listRangeName_add(capfd):
    command = f"$listRange:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listRange:name", app.getDatas,
                     Helpers.getStruct("rango", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Rangos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['controlcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testDef_updRangeId(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testDef_updRangeId_nameexist(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameexist']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameexist']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"\'{testData['nameexist']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_updRangeName(capfd):
    commands = [f"$updRange:name[{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['desupdate']}]",
                f"$updRange:name [{testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['desupdate']}]",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ] ",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ]FILL",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['desupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testDef_listRange(capfd):
    commands = [f"$listRange",
                f"$listRange ",
                f"$listRangeFILL",
                f"$listRange FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange", app.getDatas,
                         Helpers.getStruct("rango"))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testDef_listRangeId(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ] ",
                f"$listRange:id [ {testData['id']} ]FILL",
                f"$listRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("rango", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testDef_listRangeName(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ] ",
                f"$listRange:name [ {testData['nameupdate']} ]FILL",
                f"$listRange:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("rango", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testDef_listRange_e(capfd):
    commands = [f"$listRange"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange", app.getDatas,
                             Helpers.getStruct("rango"))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listRangeId_e(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:id", app.getDatas,
                             Helpers.getStruct("rango", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listRangeName_e(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("rango", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listRange_e_incomplete(capfd):
    commands = [f"$listRange"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange", app.getDatas,
                             Helpers.getStruct("rango"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listRange** **> e**\n" in out

@pytest.mark.asyncio
async def testDef_listRangeId_e_incomplete(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:id", app.getDatas,
                             Helpers.getStruct("rango", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listRange:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listRangeName_e_incomplete(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("rango", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listRange:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_delRangeId(capfd):
    command = f"$delRange:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("rango", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testDef_addRange_DelName(capfd):
    command = f"$addRange [{testData['namecreate']}, "\
              f"{testData['controlcreate']}, {testData['descreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("rango"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testDef_delRangeName(capfd):
    command = f"$delRange:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:name", app.deleteData,
                       Helpers.delStruct("rango", "name"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testDef_updRangeId_idnoexist(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_updRangeName_namenoexist(capfd):
    commands = [f"$updRange:name[{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['desupdate']}]",
                f"$updRange:name [{testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['desupdate']}]",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ] ",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ]FILL",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['desupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"'{testData['nameupdate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_delRangeId_idnoexist(capfd):
    commands = [f"$delRange:id[{testData['id']}]",
                f"$delRange:id [{testData['id']}]",
                f"$delRange:id [ {testData['id']} ]",
                f"$delRange:id [ {testData['id']} ]FILL",
                f"$delRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_delRangeName_namenoexist(capfd):
    commands = [f"$delRange:name[{testData['namecreate']}]",
                f"$delRange:name [{testData['namecreate']}]",
                f"$delRange:name [ {testData['namecreate']} ]",
                f"$delRange:name [ {testData['namecreate']} ]FILL",
                f"$delRange:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"'{testData['namecreate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listRangeId_idnoexist(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ] ",
                f"$listRange:id [ {testData['id']} ]FILL",
                f"$listRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("rango", ["id"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___rangos___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testDef_listRangeName_namenoexist(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ] ",
                f"$listRange:name [ {testData['nameupdate']} ]FILL",
                f"$listRange:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("rango", ["name"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___rangos___ "\
               "para la consulta realizada.\n" in out