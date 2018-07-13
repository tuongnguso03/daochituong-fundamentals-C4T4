map = {
    "size_x" : 6,
    "size_y" : 6,
}

player = {
    "x": 4,
    "y": 4,
}

boxes = [
    {"x":3,"y":1},
    {"x":1,"y":3},
    {"x":2,"y":2}
]

dests = [
    {"x":4,"y":1},
    {"x":2,"y":3},
    {"x":3,"y":2}
]

dx=0
dy=0

playing=True
while playing :
    for y in range(map["size_y"]):
            for x in range (map["size_x"]):
                
                Boxhere=False
                for box in boxes:
                    if box["x"]==x  and box["y"]==y:
                        Boxhere=True

                playerhere=False
                if x == player["x"] and y == player["y"]:
                    playerhere=True
                
                desthere=False
                for destination in dests:
                    if destination["x"]==x and destination["y"]==y:
                        desthere=True
                
                if playerhere==True:
                    print("P",end=" ")
                
                elif Boxhere==True:
                    print("B",end=" ")
                
                elif desthere==True:
                    print("D",end=" ")
                
                else:    
                    print("-",end=" ")
            print()    

    win=True
    for box in boxes:
        if box not in dests: 
            win=False
    if win   :
        print("win")

        playing=False  
        break
    dx=0
    dy=0
    
    move = input("Your move: ").lower()
    if move == "w":
        dy=-1
        
    elif move == "s":
        dy=1
         
    elif move == "a":
        dx=-1
        
    elif move == "d":
        dx=1
        
    else:
        print("Ezzz") 
        playing=False    
    if 0<= player["x"] + dx <= map["size_x"]-1 \
        and 0 <= player["y"] + dy <= map["size_y"]-1:
            player["x"]+=dx
            player["y"]+=dy

    for box in boxes:
        if box["x"]==player["x"] and box['y']==player['y'] :
            if 0<= box["x"] + dx <= map["size_x"]-1 \
                and 0 <= box["y"] + dy <= map["size_y"]-1:
                    box["x"] +=dx
                    box["y"] +=dy   
            else :
                player["x"]-=dx
                player["y"]-=dy
        if boxes.count(box) > 1:
            player["x"]-=dx
            player["y"]-=dy
            box["x"]-=dx
            box["y"]-=dy


              


