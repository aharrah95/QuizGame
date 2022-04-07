print("Welcome to the Quiz Master!")

playing = input("Start a new game? ")

if playing != "Yes":
    print("Exiting Game")
    quit()

print("Excellent! Let's begin!")

answer = input("Question 1. Boris from 'Bendy and the Ink Machine' is an anthropomorphic member of what species? ")
if answer == "Wolf":
    print("Correct!")
else:
    print("Incorrect!")

print("")

answer = input("Question 2. Is Gyarados a Dragon-type Pokemon? ")
if answer == "No":
    print("Correct!")
else:
    print("Incorrect!")

print("")

answer = input("Question 3. What year was the University of St. Thomas (Minnesota) founded? ")
if answer == "1885":
    print("Correct!")
else:
    print("Incorrect!")
