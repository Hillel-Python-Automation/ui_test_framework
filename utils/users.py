from operator import itemgetter

users = [
    {"name": "valid_user", "email": "yuri.gr.bond@gmail.com", "password": "E5YvjATAPb7@Uz4"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n   User %s is not defined, enter a valid user.\n" % name)
