import math


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.inbox = []
        self.outbox = []
        self.key = {
            "privateKey": None,
            "exchanged_key": None,
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

    def set_privateKey(self, key_exchanger, x):
        private_key = math.pow(key_exchanger.get_g(), x)%key_exchanger.get_q()
        self.key["privateKey"] = private_key

    def set_exchanged_key(self, key_exchanger, sender_id):
        private_key = self.key['privateKey']
        for inbox in self.inbox:
            if inbox["recipient"] == sender_id:
                k2= inbox["message"]
                exchanged_key = math.pow(k2, private_key)
                self.key["exchanged_key"] = exchanged_key

class Chanel:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.activate = False
        self.logs = []

    def get_id(self):
        return self.id

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

    def get_chanel(self, chanel_id):
        for chanel in self.chanels_list:
            if chanel.get_id() == chanel_id:
                return chanel

    def add_user(self, User):
        self.users_list.append(User)
        print("User {} is added to network!".format(User.get_name()))

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

class Diffie_Hellman:
    def __init__(self, q, g):
        #q is a large prime number and g is generator of Zq-star
        # q and g are public in chanel
        self.q = q
        self.g = g

    def get_q(self):
        return self.q
    def get_g(self):
        return self.g

    def public_key_computer(self, x):
        public_key = math.pow(self.g, x)%self.q
        return public_key

    def exchange_key(self, k1, k2):
        exchanged_key = math.pow(k1, k2)%self.q
        return exchanged_key

dh = Diffie_Hellman(13, 2)
user1 = User(101, "Alice")

user1.set_privateKey(dh, 5)
print(user1.key)

"""
network1 = Network("Steel factory")


user1 = User(101, "Alice")
user2 = User(102, "Bob")

network1.add_chanel(1001, "Managers' section")
network1.add_user(user1)
network1.add_user(user2)

chanel = network1.get_chanel(1001)
network1.send(chanel, user1, user2, "Hello")

print(chanel.see_logs())
print(user1.outbox)
print(user2.inbox)
"""