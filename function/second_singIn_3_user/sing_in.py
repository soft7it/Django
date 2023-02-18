'''
    Create a function called signIn()
    This function should take two parameters: username and password
    This function should also contain a local variable: a list of dictionaries which holds the correct username and password for 3 users
    The function should loop through the list of 3 users and in case the username and password parameters does not correspond to any of the users - return None, else - return the dictionary that represents that user
'''

def signIn(username, password):
    # List of 3 users and their corresponding passwords
    users = [
        {"username": "Andrei", "password": "vorobei"},
        {"username": "Valera", "password": "pepene"},
        {"username": "Anastasia", "password": "usturoi"}
    ]

    # Loop through the list of users and check if the given username and password match
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(user)
            return user
    # If no match is found, return None
    return None
