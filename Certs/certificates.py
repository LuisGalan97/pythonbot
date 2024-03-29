import os
dir = os.path.dirname(os.path.abspath(__file__))
import json

class Certificates:
    def __init__(self):
        adminUser = "test, omegaxis_"
        adminChannel = "test"
        self.createGlobalPermission(adminUser, adminChannel)

    def checkAccess(self, command, author, nameChannel):
        user = str(author)
        channel = str(nameChannel)
        command = command.replace(":", "_")
        filepath = f"{dir}/.Commands/{command}/"
        if os.path.exists(filepath):
            files = os.listdir(filepath)
            for file in files:
                try:
                    with (open(f'{dir}/.Commands/{command}/{file}', "r")
                          as file_json):
                        permission = json.load(file_json)
                    if ((user in permission["user"] or
                        '*' in permission["user"]) and
                        (channel in permission["channel"] or
                        '*' in permission["channel"])):
                        return True
                except Exception as ex:
                    print( "-> Ocurrio un error al intentar leer "\
                           "el permiso "\
                          f"'{command}/{file}' y este ha sido ignorado, "\
                           "por favor verifique que la estructura sea "\
                           "correcta...")
            print(f"-> El usuario '{author}' no dispone de permisos "\
                  f"para emplear el comando '${command}' por el canal "\
                  f"'{channel}'.")
            return False
        else:
            print(f"-> El usuario '{author}' no dispone de permisos "\
                  f"para emplear el comando '${command}' por el canal "\
                  f"'{channel}'.")
            return False

    def createPermission(self, command, user, channel):
        command = command.replace(":", "_")
        filepath = f"{dir}/.Commands/{command}/"
        idPermission = 1
        newPermission = {
            "user" : [item.strip() for item in user.split(',')],
            "channel" : [item.strip() for item in channel.split(',')]
        }
        if os.path.exists(filepath):
            files = os.listdir(filepath)
            exist = False
            for file in files:
                if str(idPermission) == file.replace(".json",""):
                    idPermission+=1
                try:
                    with (open(f'{dir}/.Commands/{command}/{file}', "r")
                          as file_json):
                        permission = json.load(file_json)
                    if newPermission == permission:
                        exist = file
                except Exception as ex:
                    print( "-> Ocurrio un error al intentar leer "\
                           "el permiso "\
                          f"'{command}/{file}' y este ha sido ignorado, "\
                           "por favor verifique que la estructura sea "\
                           "correcta...")
            if not exist:
                with (open(f'{dir}/.Commands/{command}/{idPermission}.json',
                      "w") as file_json):
                    json.dump(newPermission, file_json,
                              ensure_ascii=False, indent=4)
                print( "-> Permiso creado en "\
                      f"'{command}/{idPermission}.json'!")
        else:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with (open(f'{dir}/.Commands/{command}/{idPermission}.json', "w")
                  as file_json):
                json.dump(newPermission, file_json,
                          ensure_ascii=False, indent=4)
            print(f"-> Permiso creado en '{command}/{idPermission}.json'!")

    def createGlobalPermission(self, user, channel):
        self.createPermission("hello", user, channel)
        self.createPermission("help", user, channel)
        self.createPermission("help:diagram", user, channel)
        self.createPermission("help:assist", user, channel)
        self.createPermission("help:event", user, channel)
        self.createPermission("help:member", user, channel)
        self.createPermission("help:range", user, channel)
        self.createPermission("clearAll", user, channel)
        self.createPermission("addAssist", user, channel)
        self.createPermission("updAssist:id", user, channel)
        self.createPermission("delAssist:id", user, channel)
        self.createPermission("listAssist", user, channel)
        self.createPermission("listAssist:id", user, channel)
        self.createPermission("listAssist:member", user, channel)
        self.createPermission("listAssist:event", user, channel)
        self.createPermission("listAssist:date", user, channel)
        self.createPermission("listAssist:member&event", user, channel)
        self.createPermission("listAssist:member&date", user, channel)
        self.createPermission("listAssist:event&date", user, channel)
        self.createPermission("listAssist:member&event&date", user, channel)
        self.createPermission("checkAssist", user, channel)
        self.createPermission("addEvent", user, channel)
        self.createPermission("updEvent:id", user, channel)
        self.createPermission("updEvent:name", user, channel)
        self.createPermission("delEvent:id", user, channel)
        self.createPermission("delEvent:name", user, channel)
        self.createPermission("listEvent", user, channel)
        self.createPermission("listEvent:id", user, channel)
        self.createPermission("listEvent:name", user, channel)
        self.createPermission("addMember", user, channel)
        self.createPermission("updMember:id", user, channel)
        self.createPermission("updMember:name", user, channel)
        self.createPermission("delMember:id", user, channel)
        self.createPermission("delMember:name", user, channel)
        self.createPermission("listMember", user, channel)
        self.createPermission("listMember:id", user, channel)
        self.createPermission("listMember:name", user, channel)
        self.createPermission("listMember:range", user, channel)
        self.createPermission("listMember:date", user, channel)
        self.createPermission("listPointMember", user, channel)
        self.createPermission("listPointMember:id", user, channel)
        self.createPermission("listPointMember:name", user, channel)
        self.createPermission("listPointMember:range", user, channel)
        self.createPermission("listPointMember:event", user, channel)
        self.createPermission("listPointMember:id&event", user, channel)
        self.createPermission("listPointMember:name&event", user, channel)
        self.createPermission("listPointMember:range&event", user, channel)
        self.createPermission("listAllPointMember", user, channel)
        self.createPermission("listAllPointMember:id", user, channel)
        self.createPermission("listAllPointMember:name", user, channel)
        self.createPermission("listAllPointMember:range", user, channel)
        self.createPermission("listAllPointMember:event", user, channel)
        self.createPermission("listAllPointMember:id&event", user, channel)
        self.createPermission("listAllPointMember:name&event", user, channel)
        self.createPermission("listAllPointMember:range&event", user, channel)
        self.createPermission("addRange", user, channel)
        self.createPermission("updRange:id", user, channel)
        self.createPermission("updRange:name", user, channel)
        self.createPermission("delRange:id", user, channel)
        self.createPermission("delRange:name", user, channel)
        self.createPermission("listRange", user, channel)
        self.createPermission("listRange:id", user, channel)
        self.createPermission("listRange:name", user, channel)