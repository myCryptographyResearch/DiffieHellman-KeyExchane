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

    def add_inbox(self, recipient, message):
        self.inbox.append({"recipient": recipient, "message": message})

    def add_outbox(self, sender, message):
        self.outbox.append({"sender": sender, "message": message})

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
        self.users_list = []

    def add_chanel(self, id, chanel):
        cur_chanel = Chanel(id, chanel)
        cur_chanel.activate = True
        self.chanels_list.append(cur_chanel)
        print("Channel {} is added to network!".format(chanel))

    def add_user(self, id, name):
        cur_user = User(id, name)
        self.users_list.append(cur_user)
        print("User {} is added to network!".format(name))

    def send(self, chanel, sender, recipient, message):
        if chanel in self.chanels_list:
            if sender in self.users_list and recipient in self.users_list:
                sent = {"sender": sender.get_id(), "recipient": recipient.get_id(), "message":message, "status": True}
                chanel.add_log(sent)
                sender.add_outbox(recipient.get_id(), message)
                recipient.add_inbox(sender.get_id(), message)
            else:
                chanel.add_log({"erroe": "Invalid sender or recipient", "status": False})
        else:
            print({"erroe": "Invalid Chanel"})



network1 = Network("Hospital")