from k_amino import Client
import info

def login():
    client = Client(bot=True)
    client.login(email=info.EMAIL, password=info.PASSWORD)
    return client