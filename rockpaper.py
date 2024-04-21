import random
rock=''' 
 _______
---' ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
  _______
---' ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
 _______
---' ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image_lst=[rock,paper,scissors]
u_score=0
u_com=0
while True:
    user_choice=int(input("What do you choose?Type 0 for Rock,1 for paper or 2 for Scissors"))
    if user_choice>=3 or user_choice<0:
        print("Invalid Choice ! You Lose ")
    else:
        print("You Choose:")
        print(image_lst[user_choice])
        computer_choice=random.randint(0,2)
        print("Computer Choose:")
        print(image_lst[computer_choice])
        if user_choice==0 and computer_choice==2 :
            print("You Win!")
            u_score+=1
        elif computer_choice==0 and user_choice==2:
            print("You Lose!")
            u_com+=1
        elif(computer_choice>user_choice):
            print("You Lose!")
            u_com += 1
        elif user_choice>computer_choice:
            print("You Win!")
            u_score += 1
        elif(computer_choice==user_choice):
            print("It is a draw")
        ch=input("Do you want to continue")
        if ch=="yes":
            continue
        else:
            print(f"Computer score{u_com}")
            print(f"Your Score{u_score}")
            if u_com>u_score:
                print(f"You Lose")
            elif u_score>u_com:
                print(f"You win")
            elif u_score==u_com:
                print("Score Level")
            exit()

000