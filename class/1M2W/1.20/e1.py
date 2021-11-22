dic = {

    "today work" : "python cording",
    "time limit" : "today 12PM",
    "success or failure." : ['O','X']

}

print("today list: ",dic["today work"])
print("limit of time: ",dic["time limit"])
print( "success or failure:",dic[ "success or failure."][0])
print()
dic["tomorrow wake up time"] = ["9:00","9:30","10:00","10:30","11:00"]
print(dic)
t =int(input("choose your wake up time of tomorrow:"))
if t in dic:
    print(dic[t])