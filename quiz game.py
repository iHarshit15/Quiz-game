#welcome message
print("Welcome to the Quiz Game")



#name input from user
name = (input("Enter your name: "))
print("Welcome " + name)



#permission to start
playing = input("Do you want to play? yes/no: ")



#by if statement checking that persmission is granted
if playing.lower() != "yes" :
    quit()
    
print("lets play!!")




#set the initial score count 0
score = 0


#here the question will display and if user give right answer that will add 1 score else it print "incorrect" and move to next question
Answer = input("which is the oldest operating system? ")
if Answer.lower() == "unix" :
        print("Correct!!")
        score += 1
else :
        print("Incorrect")


    
Answer = input("what is the latest operating system of windows? ")
if Answer.lower() == "windows 11":
        print("Correct!!")
        score += 1
else :
        print("Incorrect!")

    
    
Answer = input("what is the latest operating system of mac? ")
if Answer.lower() == "monterey" :
        print("Correct!!")
        score += 1
else :
        print("Incorrect!")
    

Answer = input("what does CPU stand for? ")
if Answer.lower() == "central processing unit":
        print("Correct!!")
        score += 1

else:
        print("Incorrect!")
    
    
Answer = input("what does GPU stand for? ")
if Answer.lower() == "graphic processing unit" : 
        print("Correct!!")
        score += 1
else:
        print("Incorrect!")



#here if the user get 3 or more than 3 score then he will win else lose
if score >= 3 :
    print("yayy you win!!")
    input("Press Enter for result")
    print("Your score is " + str(score) + " out of 5")
    print("Thanks for playing!!")
else:
    print("You Lose, Try Again")