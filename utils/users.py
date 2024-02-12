from operator import itemgetter

from utils.util import get_number

users = [
    {"name": "validuser", "email": f"yuri.gr.bond+{get_number()}@gmail.com", "password": "E5YvjATAPb7@Uz4"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n   User %s is not defined, enter a valid user.\n" % name)
