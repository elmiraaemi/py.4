import imp


import instaloader
import getpass
f=open("folowers.txt","r")
old_followers=[]
for line in f:
    old_followers.append(line)
f.close()
l=instaloader.Instaloader()
username=input("username : ")
password=getpass.getpass("password")
l.login(username,password)
print("don")
profile=instaloader.profile.from_username(l.context,"elmiraaemi")
new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower)
for old_follower in old_followers :
    if old_follower not in new_followers:
        print(old_follower)
f=open("folloer.txt","w")
for follower in new_followers:
    f.write(follower+"\n")    
f.close()        