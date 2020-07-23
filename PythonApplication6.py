#Needed to randomly generate world
import random

#Sets up the tiles world will be built from and also variable so you can scale the world tiles.
global var_WorldTilesLen
global arr_WorldTiles
arr_WorldTiles = ["mountain","forest","town","camp","wildlands"]
var_WorldTilesLen = len(arr_WorldTiles) - 1
#This array contains the entire world as a 2d array.
global arr_World
arr_World = []
#The current "line" of world that is being worked on, you can also think of it as the X axis.
global arr_WorldLine
arr_WorldLine = []
#The location of the player at any given moment
global arr_PlayerLocation
#the first number represents X axis (moving left & right), second number represents Y axis (Up & Down movement)
arr_PlayerLocation = [0,0]
#var_PlayerXP currently does fuck all but good to remember

#This is the function that creates the world the character will play in.
def fun_WorldCreation():
    arr_WorldLine = []
    x = 0
    ii = int(input("Input world length"))
    iii = int(input("Input world width"))
    for x in range(0,ii):

        for y in range(0,iii):
            z = arr_WorldTiles[random.randint(0,var_WorldTilesLen)]
            arr_WorldLine.insert(0,z)
        y = 0
        z = ()
        x = x+1
        arr_World.insert(0,arr_WorldLine)
        arr_WorldLine = []
#The first print is just debug so that I can see the full generated world
    print(arr_World)
    f = len(arr_World)
#Prints the world line by line to give a 2d world navigation map effect
    for d in range(0,f):
        print(arr_World[d])

def fun_OverworldMove():
    print("You are in: ",arr_World[arr_PlayerLocation[1]][arr_PlayerLocation[0]])
    print("(U)p,(D)own,(L)eft,(R)ight?")
    var_playermovement = input(str(""))
    var_playermovement = var_playermovement.lower()
    print(arr_PlayerLocation[1])
    print(arr_PlayerLocation[0])

    if var_playermovement == "d":
        #Adds 1 to the correct axis (in this case the X axis which is the second number in the array that stores player position so [1] because python counts from 0 so technically the player has moved one spot)
        arr_PlayerLocation[1] = arr_PlayerLocation[1] + 1
        #Checks if the player's location is greater than the amount of tiles that exist in that dimension and then reverts them to 0 to make it feel like the world is round
        if arr_PlayerLocation[1] == len(arr_World):
            arr_PlayerLocation[1] = 0

    if var_playermovement == "u":
        arr_PlayerLocation[1] = arr_PlayerLocation[1] - 1
        if arr_PlayerLocation[1] < 0:
            arr_PlayerLocation[1] = len(arr_World) - 1

    if var_playermovement == "l":
        arr_PlayerLocation[0] = arr_PlayerLocation[0] - 1
#       if arr_PlayerLocation[0] > len(arr_World[0]) - 1:
#            arr_PlayerLocation[0] = 0
        if arr_PlayerLocation[0] < 0:
            arr_PlayerLocation[0] = len(arr_World[0]) - 1


    if var_playermovement == "r":
        arr_PlayerLocation[0] = arr_PlayerLocation[0] + 1
        if arr_PlayerLocation[0] > len(arr_World[0]) - 1:
            arr_PlayerLocation[0] = 0
    fun_OverworldMove()
#The inputs don't change it wtf

def fun_



fun_WorldCreation()
fun_OverworldMove()