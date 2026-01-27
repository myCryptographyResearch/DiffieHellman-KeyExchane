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