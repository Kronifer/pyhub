from github import Github
import json
import os

try:
    with open("userinfo.json", "r") as file:
        data = json.load(file)
        usrname = data['name']
        passwd = data['password']
except:
    usrname = input("Enter Github username. You only need to do this once. ")
    passwd = input("Enter Github password. You only do this once. ")
    data = {'name': usrname, 'password': passwd}
    with open('userinfo.json', 'w') as file:
        data = json.dump(data, file)

g = Github(usrname, passwd)
os.system('cls' if os.name == 'nt' else 'clear')
inloop = True
while inloop == True:
    choice = input("Enter a command. To see all commands, type 'help'. ")
    if(choice == 'listrepo'):
        repos = g.search_repositories(query='user:' + usrname)
        for repo in repos:
            repo = str(repo)
            seenquote = False
            truereponame = ""
            for element in repo:
                if(element == "\""):
                    seenquote = True
                if seenquote == True:
                    if(element == ")"):
                        pass
                    else:
                        truereponame += element
            print(truereponame)


                
        

