#string concatination (how to put strings together)

# youtuber = "sumanth" #string

# #a few ways to do it
# print("subscribe to "+ youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb:")
verb2 = input("verb:")
famous_person = input("famous person: ")

madlib = f"computer programming is so {adj}! it makes me excited all the time because\
    i love to {verb1}. stay hydrated and {verb2} like you are listening to {famous_person}!"
    
print(madlib)