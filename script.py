# class Dog:
#     def bark(self):
#         print("whoof whoof")

# class Owner:
#     def __init__(self, name, address):
#         self.name = name
#         self.company = address

# class User:
#     def __init__(self, username, email, password):
#         self._username = username
#         self.email = email
#         self.password = password

#     def sayHi(self, user):
#         print(f"Sending {user.username} a message: Hi {user.username}, its {self.username}")

# user1 = User("Animesh", "anim@gmail.com", "zom123")
# user2 = User("Ujjwal", "ujjwal@gmail.com", "ujjwal123")

# user1.sayHi(user2)

def decortor(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper

@decortor
def hello():
    print("Hello World!")

hello()