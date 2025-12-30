from oops_proj import chatbook

sam = chatbook(username="abc", pwd="xyz", logged_in=False)
print(sam.username)
print(sam.sign_in())


# musk = chatbook(username="elonmusk", pwd="spacex", logged_in=False)
# print(musk.sign_up())
# print(musk.send_message())
