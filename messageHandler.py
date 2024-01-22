import sys
import discord
sys.path.insert(1, './DF')
from dataframe import DataFrame
sys.path.insert(1, './Helpers')
from helpers import Helpers

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client

    async def inMsg(self):
        if self.__message.author == self.__client.user:
            return

    async def helpMsg(self):
        msg = self.__message.content
        messages = []
        #messages.append("**Lista de comandos**\n")
        if msg.startswith("$help:assist"):
         #---------------------------------Asistencias----------------------------------------
            messages.append("**_Asistencias:_**\n")
            messages.append("Las asistencias hacen referencia a una serie de registros de todas las participaciones, "\
            "en las cuales los integrantes de ⚜Avalon⚜ han podido hacer parte, "\
            "para actividades o eventos tales como ataques, defensas, AVAs, entre otros. Por tanto una asistencia "\
            "por defecto contiene informacion de un integrante y evento asociado, junto con la fecha del suceso en cuestion\n")
            messages.append(f"{Helpers.genMsg('addAssist [Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('updAssist:id [ID, Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('delAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event [Integrante, Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event [Integrante, Evento] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&date [Integrante, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&date [Integrante, Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event&date [Evento, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event&date [Evento, Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event&date [Integrante, Evento, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event&date [Integrante, Evento, Fecha 1, Fecha 2] > e', 'asistencia')}")
        elif msg.startswith("$help:event"):
             #-----------------------------------Eventos----------------------------------------
            messages.append("**_Eventos:_**\n")
            messages.append("Las eventos corresponden a una lista con informacion de las actividades "\
            "que ⚜Avalon⚜ ha decidido puntuar para poder premiar a sus integrantes, "\
            "por aporte y participacion, involucrando ataques, defensas, AVAs, entre otros.\n")
            messages.append(f"{Helpers.genMsg('addEvent [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:id [ID, Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:name [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:name [Nombre]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent > e', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID] > e', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre] > e', 'evento')}")
        elif msg.startswith("$help:member"):
            #----------------------------------Integrantes----------------------------------------
            messages.append("**_Integrantes:_**\n")
            messages.append("Los integrantes son una serie de registros en los cuales se encuentran "\
            "listados y referenciados todos los miembros de la alianza ⚜Avalon⚜, junto con informacion "\
            "complementaria tales como un rango asignado y la fecha de ingreso.\n")
            messages.append(f"{Helpers.genMsg('addMember [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:id [ID, Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:name [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2] > e', 'integrante')}")
        elif msg.startswith("$help:range"): 
            #-------------------------------------Rangos----------------------------------------
            messages.append("**_Rangos:_**\n")
            messages.append("Las rangos disponen registros con informacion de los diferentes "\
            "rangos asignables a los integrante o miembros de la alianza ⚜Avalon⚜.\n")
            messages.append(f"{Helpers.genMsg('addRange [Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:id [ID, Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:name [Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:name [Nombre]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange > e', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID] > e', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre] > e', 'rango')}")           
        if array:
            array = []
            length = 0
            for i in range(len(messages)):
                length = length + len(messages[i])
                if length >= 2000:
                    await self.__message.channel.send(''.join(array))
                    array = []
                    length = len(messages[i])
                    array.append(messages[i])
                    if i == len(messages) - 1:
                        await self.__message.channel.send(''.join(array))
                elif i == len(messages) - 1:
                    array.append(messages[i])
                    await self.__message.channel.send(''.join(array))
                else:
                    array.append(messages[i])

    async def dFMsg(self, command, method, struct):
        msg = self.__message.content
        if msg.find(':') != -1 and command.find(':') != -1 and msg.startswith(f"${command}"):
            if msg.find('&') != -1 and command.find('&') != -1 and msg.startswith(f"${command}"):
                msgpos = msg.find('&') + 1
                cmdpos = command.find('&') + 1
                if msg.find('&', msgpos) != -1 and command.find('&', cmdpos) != -1 and msg.startswith(f"${command}"):
                    msg = True
                elif not msg.startswith(f"${command}&") and command.find('&', cmdpos) == -1 and msg.startswith(f"${command}"):
                    msg = True
                else:
                    msg = False
            elif not msg.startswith(f"${command}&") and command.find('&') == -1 and msg.startswith(f"${command}"):
                msg = True
            else:
                msg = False
        elif not msg.startswith(f"${command}:") and command.find(':') == -1 and msg.startswith(f"${command}"):
            msg = True
        else:
            msg = False
        if msg:
            content = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {content}"
            result = method(request, struct)
            if isinstance(result, list):
                if request.find('>') != -1:
                    excelreq = content.lower()
                    excelreq = excelreq[excelreq.find(']')+1:excelreq.find('e')+2].replace(' ','')
                    if excelreq == ">e":
                        strContent = content[content.find('[')+1:content.find(']')].split(",")
                        strContent = "_".join(data.strip() for data in strContent)
                        if command.find(':') != -1:
                            fileName = f"{command.split(':')[0]}{command.split(':')[1].capitalize()}{strContent}"
                        else:
                            fileName = f"{command}{strContent}"
                        df = DataFrame(fileName, result)
                        if df.getSuccess():
                            discordFile = discord.File(df.getDirectory())
                            await self.__message.channel.send(f"**_{list(struct['controller'].keys())[0].capitalize()}s_** "\
                                                              f"**_encontrad{'a' if list(struct['controller'].keys())[0][0] == 'a' else 'o'}s:_**")
                            await self.__message.channel.send(file=discordFile)
                            if not df.deleteFrame():
                                await self.__message.channel.send("Error al intentar eliminar el excel, "\
                                                                  "por favor consulte con el administrador.")
                        else:
                            await self.__message.channel.send("Error al intentar crear el excel, "\
                                                              "por favor consulte con el administrador.")
                    else:
                        parameters = f"**[**{content[content.find('[')+1:content.find(']')]}**]** "
                        await self.__message.channel.send("Se ha detectado el uso del operador **>** despues del comando "\
                                                          "inicial, si desea obtener los datos en un archivo de excel, "\
                                                          "debe completar el comando ingresadolo de la siguiente forma:\n"\
                                                         f"$**{command}** {parameters if command.find(':') != -1 else ''} **> e**")
                else:
                    array = []
                    title = f"**_{list(struct['controller'].keys())[0].capitalize()}s_** "\
                            f"**_encontrad{'a' if list(struct['controller'].keys())[0][0] == 'a' else 'o'}s:_**"
                    length = len(title)
                    array.append(title)
                    for i in range(len(result)):
                        tempdict = f"* {', '.join([f'**_{key}_** : _{value}_' for key, value in result[i].items()])}"
                        length = length + len(tempdict) + 1
                        if length >= 2000:
                            await self.__message.channel.send('\n'.join(array))
                            array = []
                            length = len(tempdict) + 1
                            array.append(tempdict)
                            if i == len(result) - 1:
                                await self.__message.channel.send('\n'.join(array))
                        elif i == len(result) - 1:
                            array.append(tempdict)
                            await self.__message.channel.send('\n'.join(array))
                        else:
                            array.append(tempdict)

            elif isinstance(result, str):
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send("Error en la base de datos, "\
                                                  "por favor consulte con el administrador.")

    async def contMsg(self, command, method, struct):
        msg = self.__message.content
        msg = msg[:msg.find('[')].strip() if msg.find('[') != -1 else msg.strip()
        if msg == f"${command}":
            request = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {request}"
            result = method(request, struct)
            if result:
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send("Error en la base de datos, "\
                                                  "por favor consulte con el administrador.")