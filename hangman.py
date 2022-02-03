
import random
name = input("enter any name______")
print("hello",name,"dear aapka welcome h hmare game me")
def hangman():
    word_list=("india","delhi","laptop","hangman")
    word=random.choice(word_list)
    word_length=len(word)
    # turns=6
    guessmade=[]
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    for _ in range (word_length):
        guessmade+="_"
    print(guessmade)
    turns=10
    game=False
    while not  (game):
        guess_type=input("enter the guess")
        for i in range(word_length):
            priya=(word[i])
            if priya==guess_type:
                guessmade[i]=priya
        if guess_type not in word:
            turns-=1
            if turns==9:
                print("9 turns left!!!")
                print("-----------------")
            if turns==8:
                print("8 turns left!!!")
                print("---------------")
                print("o")
            if turns==7:
                print("7 turns left!!!")
                print("-------------")
                print("o")
                print("|")
            if turns==6:
                print("6 turns left!!!")
                print("---------------")
                print("o")
                print("|")
                print("/ \ ")
            if turns==5:
                print("5 turns left!!!")
                print("-------------")
                print("  o")
                print("  |")
                print("  /\   ")
            if turns==4:               
                print("4 turns left!!!")
                print("  \o")
                print("   |   ")
                print("   /\ ")
            if turns==3:
                print("3 turns left!!!")
                print("   \o/ ")
                print("    |   ")
                print("    /|\ ")
            if turns==2:
                print("2 turns left!!!")
                print("  \o/--|")
                print("   |  ")
                print("   /|\   ")
            if turns==1:
                print("1 turns left!!!")
                print("|--\o/--|")
                print("    |")
                print("   /|\   ")
        print(guessmade)
        if turns==0:
            print("your chance is finished")
            print("defeat")
            break
        if "_" not in guessmade:
            print("you are winner")
            break
hangman()