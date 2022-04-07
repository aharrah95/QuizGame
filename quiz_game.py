print("Welcome to the Quiz Master!")

playing = input("Start a new game? ")

if playing != "Yes":
    print("Exiting Game")
    quit()

print("Excellent! Let's begin!")
score = 0

answer = input("Question 1. Boris from 'Bendy and the Ink Machine' is an anthropomorphic member of what species? ")
if answer == "Wolf":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 2. Is Gyarados a Dragon-type Pokemon? ")
if answer == "No":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 3. What year was the University of St. Thomas (Minnesota) founded? ")
if answer == "1885":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 4. What band duo performed the hit songs 'Stressed Out', and 'Heathens'? ")
if answer == "twenty one pilots":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 5. Who is the creator behind the massively popular game 'Five Nights at Freddy's''? ")
if answer == "Scott Cawthon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 6. What home game console had the number '64' in it's title, predating the Nintendo 64? ")
if answer == "Commodore 64":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 7. True or false: tomatoes are a vegetable? ")
if answer == "False":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 8. What movie ended with the infamous 'man in the woodchipper', and later became a series on "
               "FX? ")
if answer == "Fargo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 9. What Coen Brothers movie has a restaurant based on it in Cedar Rapids, IA? ")
if answer == "The Big Lebowski":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("")

answer = input("Question 10. True or false: Chica will let you feed her pizza slices in Five Nights at Freddy's VR's "
               "'Parts & Services'' minigame? ")
if answer == "True":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%!")
