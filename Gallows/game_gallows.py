import random

dict = ("apple", "orange", "mandarin", "watermelon", "strawberry")
text = '''                  Game Gallows
Rules: 1. You need to guess the word on the topic of fruits
       2. You can be mistaken only 5 times 
       3. By '*' denotes letters that you haven't guessed
       4. All letters of the word are small 
       
If you want to start the game, press - '1'
If you want exit the game, press - '0'  '''
print (text)

while True:
    choice = input()
    if choice == "1":
        break
    elif choice == "0":
        break
    else:
        print("You need to press - '1' or '0'. Please try again")


if choice == "1":
    word = dict[random.randint(0, 4)]
    print ("Word you need to guess:", end = " ")
    check = []
    for i in range (0, len(list(word))):
        check.append("*")
    print(''.join(check))
    print("\n")
    mistake = 0
    while mistake < 5:
        mis = False
        print ("Write a letter: ")
        letter = input()
        for i in range (0, len(list(word))):
            if letter == list(word)[i]:
                check[i] = letter
                mis = True
        if mis:
            if check == list(word):
                print("Congratulations! You won!")
                break
            else:
                print("You guessed the letter")
                print(''.join(check))
        else:
            mistake += 1
            print("This letter isn't in the word")
            print("Number of mistakes: " + str(mistake) + " of 5")
            print(''.join(check))
    if mistake == 5:
        print("You lost!")
    else:
        raise SystemExit
else:
    raise SystemExit

