def which_direction():
    while True:
        go=input("Which way do you want tot go, left or right? ")
        if go== "": continue
        go=go[0].lower()
        if go in ['l','r']:
            return go
        else:
            print("I don't understand.Try again")

def room2():
    print()
    print("You crawl through into a small space, it's quite dark")

def room3():
    print()
    print("You crawl through the tunnel and stumble, you see")
    print("immediately below you a huge hole and fall to your death!")

player=input("What's ypur name adventurer? ")
print()
print("Welcome top the world of Unknown , ",player)
print("You are entering a huge cave")
print("You are walking a bit and see a light with two tunnels,one one the left and the other one on the right")

go=which_direction()
if go == 'l':
    room2()
elif go=='r':
    room3()


