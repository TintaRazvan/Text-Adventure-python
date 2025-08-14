def welcome():
    player=input("What's ypur name adventurer? ")
    print("Welcome top the world of Unknown , ",player)

def entrance():
    print()
    print("You are entering a huge cave")
    print("You are walking a bit and see a light with two tunnels,one one the left and the other one on the right")

def which_direction(choices):
    while True:
        c=", ".join(choices)
        go=input("Which way do you want tot go: "+ c + "?")
        if go== "": continue
        go=go[0].lower()
        if go in choices:
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

def room4():
    print()
    print("There is a posionous gas, You are kiiled as you step in this room")

def room5():
    print()
    print("You are entering a big room with multiple tunnels, ahead it's a key lock ")

def room6():
    print()
    print("You see a torch and other two ways you can go")

def room9():
    print()
    print("room in progress")


welcome()
entrance()
#entering the world
go=which_direction(['e','w'])
if go == 'w':
    room2()
elif go=='e':
    room3()
#inside the room 2
go=which_direction(['n','s','e','w'])
if go=='w':
    room4()
elif go=='e':
    room6()
elif go=='n':
    room9()
elif go=='s':
    room2()
     
    



