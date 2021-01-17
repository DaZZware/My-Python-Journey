# Chatbot

print ("Hello, I am Zeon 64. I am a Chatbot. \n" + "I like Animals and love to talk about food")
name = input("What is your name?: ")
print ("Hello ", name,  ", Nice to meet you.")
Year = input("I am not very good at dates. What is the Year?: ")
Year = int(Year)
print ("Yes, I think that is right. Thanks!")
myAge = input("Can you guess my age? - enter a number: ")
print ("Yes you are right. I am", myAge)
myAge = int(myAge)
myAge = myAge + 85
print ("I will be", myAge, "in 85 years \nThat will be the year", Year + myAge)
food = input("I love Chocolate and I also like trying new kinds of food. \nHow about you? What is your favourite food?: ")
print ("I like", food, "too.")
question = 'How often do you eat ' + food +'?:'
howoften = input(question)
print ("Interesting, I wonder if that is good for your health!")
animal = input("My Favourite animal is a Tiger. What is yours?: ")
if animal == 'Tiger':
    print ("Thats the same as mine!")
elif animal == 'tiger':
    print ("That is the same as mine, but its a capital at the start because it is a Name Tiger!")
else:
    print ("I like", animal, "too")
print ("I wonder if a", animal, "likes to eat ", food + '?')
feeling = input("How are you today?: ")
reason = input("Why are you feeling " + feeling + " now?\nPlease tell me: ")
print ("I understand. Thanks for sharing.")
print ("It has been a long day\n I am too tired to talk anymore. We can chat later.""\nGoodbye", name, "It has been nice to chat with you.")


