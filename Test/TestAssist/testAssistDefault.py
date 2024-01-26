from messageHandler import MessageHandler
from appHandler import AppHandler
from helpers import Helpers
import pytest
from io import StringIO
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testAddAssist(capfd):  
  message = Message(author="test", content="$addAssist [Avalonicus, defprismaganada, 25-01-2024]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.contMsg("addAssist", app.setData, Helpers.setStruct("asistencia"))
  out, _ = capfd.readouterr()
  assert "La ___asistencia___ ha sido creada con exito" in out

