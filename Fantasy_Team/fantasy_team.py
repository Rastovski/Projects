import csv
import random

budget = 100
cost = 0


top_eleven = []
subs=[]
top_ids=[]
subs_ids=[]
sub_score=0
players=[]
fantasy_team = []
score=0

no_players = 15
pos_limits = {"FW": 3, "MID": 5, "DEF":5, "GK":2}

pos_chosen = {"FW": 0, "MID": 0, "DEF":0, "GK":0}

def print_all():
    
    global sub_score, top_ids, subs_ids
    sub_score = 0
    top_ids = []
    subs_ids = []
    top_eleven.sort(key=lambda x: int(x[0]))
    subs.sort(key=lambda x: int(x[0]))

    print("##################################################################################################")
    print("Starting eleven:")
    for i in top_eleven:
        top_ids.append(i[0])
        print(i)

    print("##################################################################################################")
    print("Substitutes: ")
    for i in subs:
        subs_ids.append(i[0])
        sub_score += float(i[4])
        print(i)

    print("##################################################################################################")
    print(f"11: {top_ids} SCORE: {score-sub_score}")
    print(f"4: {subs_ids} SCORE: {sub_score}")
    print("##################################################################################################")

    
    with open('solution.txt', 'w') as f:
        f.write(','.join(top_ids))
        f.write('\n')
        f.write(','.join(subs_ids))
        
    f.close()
    
def starting_subs():

    global top_eleven, subs, fantasy_team
    
    forward = [x for x in fantasy_team if x[1]=="FW"]
    defendr = [x for x in fantasy_team if x[1]=="DEF"]
    gk = [x for x in fantasy_team if x[1]=="GK"]

    top_eleven.append(gk[0])
    top_eleven.append(forward[0])
    top_eleven.extend(defendr[:3])
    
    for player in fantasy_team:
        position = player[1]
        if(position != "GK" and len(top_eleven)<11):
                if player not in top_eleven:
                    top_eleven.append(player)
        else:
            if(player not in top_eleven):
                subs.append(player)

def dodaj_igraca(igrac):
    
    global fantasy_team, cost, score, pos_chosen

    if(check(igrac[3])):
        if((budget-cost) >= float(igrac[5])):
                            if(igrac not in fantasy_team):
                                fantasy_team.append(igrac)
                                pos_chosen[igrac[1]] = pos_chosen[igrac[1]] + 1
                                cost = cost + float(igrac[5])
                                score = score + float(igrac[4])


##############################################
#START GRASP

def construction():
    global fantasy_team, cost, score, pos_chosen
    cost=0
    score=0
    fantasy_team = []
    pos_chosen = {"FW": 0, "MID": 0, "DEF":0, "GK":0}

    forward = [x for x in players if x[1]=="FW"]
    cf = {"min": float(forward[-1][4])/float(forward[-1][5]),"max": float(forward[0][4])/float(forward[0][5])}
    
    mid = [x for x in players if x[1]=="MID"]
    cm = {"min": float(mid[-1][4])/float(mid[-1][5]),"max": float(mid[0][4])/float(mid[0][5])}
    
    defendr = [x for x in players if x[1]=="DEF"]
    cd = {"min": float(defendr[-1][4])/float(defendr[-1][5]),"max": float(defendr[0][4])/float(defendr[0][5])}
    
    gk = [x for x in players if x[1]=="GK"]
    cg = {"min": float(gk[-1][4])/float(gk[-1][5]),"max": float(gk[0][4])/float(gk[0][5])}
    
    while(len(fantasy_team)<15):
        if(budget-cost < float(players[-1][5])):
            cost=0
            score=0
            fantasy_team = []
            pos_chosen = {"FW": 0, "MID": 0, "DEF":0, "GK":0}
        
        if(pos_chosen["FW"]<pos_limits["FW"]):
            polje=[x for x in forward if float(x[4])/float(x[5]) <= cf["min"]+1*(cf["max"]-cf["min"]) ]
            igrac=random.choice(polje)
            dodaj_igraca(igrac)
        elif(pos_chosen["DEF"]<pos_limits["DEF"]):
            polje=[x for x in defendr if float(x[4])/float(x[5]) <= cd["min"]+1*(cd["max"]-cd["min"])]
            igrac=random.choice(polje)
            dodaj_igraca(igrac)
        elif(pos_chosen["MID"]<pos_limits["MID"]):
            polje=[x for x in mid if float(x[4])/float(x[5]) <= cm["min"]+1*(cm["max"]-cm["min"]) ]
            igrac=random.choice(polje)
            dodaj_igraca(igrac)
        elif(pos_chosen["GK"]<pos_limits["GK"]):
            polje = [x for x in gk if float(x[4])/float(x[5]) <= cg["min"]+1*(cg["max"]-cg["min"]) ]
            igrac=random.choice(polje)
            dodaj_igraca(igrac)
        

def local():
    global top_eleven, subs, fantasy_team, cost, score
    top_eleven = []
    subs = []
    starting_subs()
    copy_elev = top_eleven.copy()
    igrac=[]
    s=[]
    for i in range(11):
        
        neighbors = [x for x in players if top_eleven[i][1]==x[1]]
        
        for j in neighbors:
            if(float(j[4])>float(top_eleven[i][4])):
               
                if((budget-cost+float(top_eleven[i][5]))>float(j[5])):
                    if(j not in fantasy_team):
                        indeks = fantasy_team.index(top_eleven[i])
                        igrac=fantasy_team.pop(indeks)
                        if(check(j[3])):
                            top_eleven.pop(i)
                            top_eleven.insert(i, j)
                            fantasy_team.insert(indeks, j)
                            cost = cost - float(igrac[5]) + float(j[5])
                            score = score - float(igrac[4]) + float(j[4])
                        else:
                            fantasy_team.insert(indeks, igrac)
    return fantasy_team     

def check_for_better(best, new): #provjerava novu grupu igraca za svaku iteraciju
    b_score = sum([float(x[4]) for x in best])
    n_score = sum([float(x[4]) for x in new])
    if(n_score > b_score):
        return True
    return False

def GRASP():
    global fantasy_team
    sbest = []
    snew=[]
    for r in range(10):
        construction()
        snew = local()
        if(check_for_better(sbest, snew)):
            sbest = snew.copy()
    fantasy_team=sbest

#END GRASP
#########################################################

def check(team): #Provjera postoje li vec 3 igraca iz istog tima
    num = [x for x in fantasy_team if x[3]==team]
    if(len(num)==3):
        return False
    return True


def pick_players(position): #izaberi igrace
    global cost, score, fantasy_team, pos_chosen
    for player in players:
        if(check(player[3])):
            if(player[1]==position):
                if(pos_chosen[position] < pos_limits[position]):
                    if((budget-cost) >= float(player[5])):
                        if(player not in fantasy_team):
                            fantasy_team.append(player)
                            pos_chosen[position] = pos_chosen[position] + 1
                            cost = cost + float(player[5])
                            score = score + float(player[4])
                           
        else:
            continue

instance = open("./2022_instance1.csv","r") 
reader = csv.reader(instance)

for player in reader:
    players.append(player)


players.sort(key=lambda cost: float(cost[4])/float(cost[5]), reverse=True)

for i in ["FW", "DEF", "MID" , "GK"]:
    pick_players(i)

fantasy_team.sort(key=lambda points: float(points[4]), reverse=True)

#UNCOMMENT FOR GREEDY
#starting_subs()


#UNCOMMENT FOR GREEDY + GRASP
#local()

#UNCOMMENT FOR GRASP ALGORITHM
#GRASP()

print_all()