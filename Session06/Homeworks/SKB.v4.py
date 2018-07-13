#from time import sleep
#import keyboard

game={
    "level1":{
        "map" : {
            "size_x" : 6,
            "size_y" : 6,
        },

        "player" : {
            "x": 4,
            "y": 4,
        },

        "boxes" : [
            {"x":3,"y":1},
            {"x":1,"y":3},
            {"x":2,"y":2}
        ],

        "dests" : [
            {"x":4,"y":1},
            {"x":2,"y":3},
            {"x":3,"y":2}
        ],
        "walls" : []
    },
    "level2":{
        "map" : {
            "size_x" : 7,
            "size_y" : 5,
        },

        "player" : {
            "x": 0,
            "y": 0,
        },

        "boxes" : [
            {"x":1,"y":1},
            {"x":1,"y":3}
            
        ],

        "dests" : [
            {"x":4,"y":1},
            {"x":4,"y":3},
        ],
        "walls" : [
            {"x":3,"y":0},
            {"x":3,"y":1},
            {"x":3,"y":2},
            {"x":3,"y":4},
            {"x":3,"y":5},
        ]

    },
    "level3":{
        "map" : {
            "size_x" : 11,
            "size_y" : 11
        },

        "player" : {
            "x": 4,
            "y": 4,
        },

        "boxes" : [
            
            {"x":3,"y":3},
            {"x":5,"y":4},
            {"x":4,"y":5}
        ],

        "dests" : [
            
            {"x":6,"y":6},
            {"x":6,"y":7},
            {"x":7,"y":6}
        
        ],
        "walls" : [
            {"x":0,"y":3},
            {"x":0,"y":4},
            {"x":0,"y":5},
            {"x":1,"y":2},
            {"x":1,"y":3},
            {"x":1,"y":5},
            {"x":1,"y":7},
            {"x":1,"y":8},
            {"x":1,"y":9},
            {"x":1,"y":10},
            {"x":2,"y":1},
            {"x":2,"y":2},
            {"x":2,"y":5},
            {"x":2,"y":6},
            {"x":2,"y":7},
            {"x":2,"y":10},
            {"x":3,"y":0},
            {"x":3,"y":1},
            {"x":3,"y":10},
            {"x":4,"y":0},
            {"x":4,"y":7},
            {"x":4,"y":10},
            {"x":5,"y":0},
            {"x":5,"y":1},
            {"x":5,"y":2},    
            {"x":5,"y":5},
            {"x":5,"y":6},
            {"x":5,"y":7},
            {"x":5,"y":10},
            {"x":6,"y":2},
            {"x":6,"y":5},
            {"x":6,"y":10},
            {"x":7,"y":1},
            {"x":7,"y":2},
            {"x":7,"y":4},
            {"x":7,"y":5},
            {"x":7,"y":7},
            {"x":7,"y":9},
            {"x":7,"y":10},
            {"x":8,"y":1},
            {"x":8,"y":9},
            {"x":8,"y":8},
            {"x":9,"y":1},
            {"x":9,"y":8},
            {"x":9,"y":7},
            {"x":10,"y":1},
            {"x":10,"y":2},
            {"x":10,"y":3},
            {"x":10,"y":4},
            {"x":10,"y":5},
            {"x":10,"y":6},
            {"x":10,"y":7}
            
        ]
    }
    
}

playing=True
level=1
while playing:
    
    playground=[]
    map=game["level{0}".format(level)]["map"]
    player=game["level{0}".format(level)]["player"]
    dests=game["level{0}".format(level)]["dests"]
    boxes=game["level{0}".format(level)]["boxes"]
    walls=game["level{0}".format(level)]["walls"]
    
    for y in range(map["size_y"]):
            playrow=[]
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
                
                wallhere=False
                for wall in walls:
                    if wall["x"]==x and wall["y"]==y:
                        wallhere=True
                
                if playerhere==True:
                    playrow.append("P")
                
                elif Boxhere==True:
                    playrow.append("B")
                
                elif desthere==True:
                    playrow.append("D")
                
                elif wallhere==True:
                    playrow.append("W")

                else:    
                    playrow.append("-")
            playground.append(playrow)

    playinglevel=True
    history=[]
    while playinglevel == True:
        
        for k in range(len(playground)):
            print(*playground[k],sep=" ")

        #inp=input("Input :").lower()
        #sleep(0.1) #cái thứ 2 ngăn nó chạy    
        clicka=False
        clicks=False
        clickw=False
        clickd=False
        undo=False
        #clicking=True
        #while clicking==True:
        #    if keyboard.is_pressed('a'): 
        #        clicka=True
                #input() #Không có cái này nó chạy tới cuối map luôn ...
        #        clicking=False
        
        #    elif keyboard.is_pressed('s'):
        #        clicks=True
                #input()
        #        clicking=False
        #    elif keyboard.is_pressed('d'):
        #        clickd=True
                #input()
        #        clicking=False
        #    elif keyboard.is_pressed('w'):
        #        clickw=True
                #input()
        #        clicking=False
        #    elif keyboard.is_pressed('q'):
        #        playinglevel=False
        #        playing=False
        #        clicking=False
        #    elif keyboard.is_pressed('z'):
        #        undo=True
        #        clicking=False
        yourmove=input("Your move (W, A, S, D, Q to quit and Z to undo) : ").lower()
        if yourmove == "a":
            clicka=True
        elif yourmove =="s":
            clicks=True
        elif yourmove =="d":
            clickd=True
        elif yourmove =="w":
            clickw=True
        elif yourmove=="q":
            playinglevel=False
            playing=False
        elif yourmove == "z":
            undo=True
        dx=0
        dy=0       
        if clicks:
            dy=1
                
        elif clickd:
            dx=1
        
        elif clickw:
            dy=-1
        
        elif clicka:
            
            dx=-1
        elif undo and len(history)>0:
            (dx_undo,dy_undo,push_or_not)=history[len(history)-1]
            if push_or_not=="Push":
                playground[player["y"]][player["x"]]="B"
                playground[player["y"]+dy_undo][player["x"]+dx_undo]="-"
                playground[player["y"]-dy_undo][player["x"]-dx_undo]="P"
                player["y"] -= dy_undo
                player["x"] -= dx_undo
            else:
                playground[player["y"]][player["x"]]="-"
                playground[player["y"]-dy_undo][player["x"]-dx_undo]="P"
                player["y"] -= dy_undo
                player["x"] -= dx_undo
            history.pop(len(history)-1)
            
        
        if 0 <= player["y"]+dy < map["size_y"] \
            and 0 <= player["x"]+dx < map["size_x"]:
                if playground[player["y"]+dy][player["x"]+dx]=="B" :
                        if 0 <= player["y"]+2*dy < map["size_y"] \
                            and 0 <= player["x"]+2*dx < map["size_x"]\
                                and (playground[player["y"]+2*dy][player["x"]+2*dx]=="-" or playground[player["y"]+2*dy][player["x"]+2*dx]=="D"):
                                    playground[player["y"]][player["x"]]="-"
                                    playground[player["y"]+dy][player["x"]+dx]="P"
                                    playground[player["y"]+2*dy][player["x"]+2*dx]="B"
                                    player["y"] += dy
                                    player["x"] += dx
                                    if dx !=0 or dy !=0 :history.append((dx,dy,"Push"))
                elif playground[player["y"]+dy][player["x"]+dx] != "W":
                    playground[player["y"]][player["x"]]="-"
                    playground[player["y"]+dy][player["x"]+dx]="P"
                    player["y"] += dy
                    player["x"] += dx
                    if dx !=0 or dy !=0 :history.append((dx,dy,"NoPush"))
        points=0
        for dest_alpha in dests:
            if playground[dest_alpha["y"]][dest_alpha["x"]] == "B":

                points=points+1           
            elif playground[dest_alpha["y"]][dest_alpha["x"]] == "-":
                playground[dest_alpha["y"]][dest_alpha["x"]]="D"
        if points==len(dests):
            for k in range(len(playground)):
                print(*playground[k],sep=" ")
            print("Level Cleared")
            #sleep(2)
            level += 1
            playinglevel=False
    if level == len(game)+1:
        print("Phá cmn Đảo.")
        playing=False        
