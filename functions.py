class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.inbox = []
        self.outbox = []
        self.key = {
            "privateKey": None,
            "publicKey": None,
        }

    #Each user is known by id and name in the Network
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Chanel:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.activate = False
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)

    def see_logs(self):
        return self.logs

class Network:
    def __init__(self, name):
        print("Network {} is created!".format(name))
        self.name = name
        self.chanels_list = []

    def add_chanel(self, id, chanel):
        cur_chanel = Chanel(id, chanel)
        cur_chanel.activate = True
        self.chanels_list.append(cur_chanel)

