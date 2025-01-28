print(" Welcome to my computer quiz game")

playing = input("Are you interested in playing?")
if playing.lower() != "yes":
    quit()

print("Okay! Let's get it going champ :)")
score = 0

answer = input("What does SaaS stand for? ")
if answer.lower() == "software as a service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PaaS stand for? ")
if answer.lower() == "platform as a service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does InfaaS stand for? ")
if answer.lower() == "infrustructure as a service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")