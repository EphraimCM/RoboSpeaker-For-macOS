import os
print("Welcome to Robo Speaker 1.1")
print("I was Created by Ephraim. I want to help you talk to people.\n Go Ahead...")
while(True):

    inp = input("What do you want to say?\t")
    if (int=="q"):
        os.system("Bye bye Friend")
        break
    command = f"say {inp}"
    os.system(command)