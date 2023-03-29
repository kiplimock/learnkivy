import datetime as dt

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, 'r')
        self.users = {}

        for line in self.file:
            email, password, username, created = line.strip().split(";")
            self.users[email] = (password, username, created)
        
        self.file.close()
    
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        return -1
    
    def add_user(self, email, password, username):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), username.strip(), Database.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1
    
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        return False
    
    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    def get_date():
        return str(dt.datetime.now()).split(" ")[0]