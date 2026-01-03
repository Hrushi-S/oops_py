from oops_proj import chatbook

# sam = chatbook(username="abc", pwd="xyz", logged_in=False)
# print(sam.username)
# # print(sam.sign_in())


# musk = chatbook(username="elonmusk", pwd="spacex", logged_in=False)
# print(musk.sign_up())
# print(musk.send_message())

# user = chatbook(username="123", pwd="abc", logged_in=False)
# print(user.get_name())
# user.set_name("Agent Y")
# print(user.get_name())


user1 = chatbook(username="user1", pwd="pass1")
print(user1.id)

chatbook.set_id(10)
user2 = chatbook(username="user2", pwd="pass2")
print(user2.id)

user3 = chatbook(username="user3", pwd="pass3")
print(user3.id)
