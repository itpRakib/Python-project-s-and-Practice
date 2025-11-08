print("Welcome to the Quiz Game!")

playing = input('Do you want to play? ' )

if playing.lower() != 'yes':
    quit()

print("Great! Let's start the game :)")
score = 0   

# Question 1

answer = input('What does CPU stand for? ')

if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

if answer.lower() == 'Central Processing Unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

# Question 2

answer = input('What does GPU stand for? ')

if answer.lower() == 'Graphics Processing Unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphics Processing Unit'.")


# Question 3

answer = input('What does RAM stand for? ') 

if answer.lower() == 'Random Access Memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Random Access Memory'.")

#  Question 4

answer = input('What does PSU stand for? ') 

if answer.lower() == 'Power Supply Unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 'Power Supply Unit'.")

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score/4) * 100) + '%.')


