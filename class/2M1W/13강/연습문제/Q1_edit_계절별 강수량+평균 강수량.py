from matplotlib import pyplot

year = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
rain_fall = [[256.9,256.5,264.3,215.9,223.2,312.8,118.6,368.1,173.9],
[1053.6,770.6,567.5,599.8,387.1,446.2,609.7,586.5,493.0],
[225.5,363.5,231.2,293.1,247.7,381.6,172.5,351.2,448.4],
[45.6,139.3,59.9,76.9,109.1,108.1,75.6,66.5,168.1]]

total_avg = []
for k in range(len(year)):
    a = 0
    for i in range(4):
        a += rain_fall[i][k]
    b = round(a/12,2)    
    total_avg.append(b)
""" print(total_avg) """

rain_stock = []
for i in range(4):
    rain_stock.append([0]*len(year))

for i in range(len(year)):
    rain_stock[0][i] = 0
    rain_stock[1][i] = rain_stock[0][i] + rain_fall[0][i]
    rain_stock[2][i] = rain_stock[1][i] + rain_fall[1][i]
    rain_stock[3][i] = rain_stock[2][i] + rain_fall[2][i]



pyplot.bar(year,rain_fall[1],width = 0.5,color = 'orange',label = 'Summer',bottom=rain_stock[1])
pyplot.bar(year,rain_fall[2],width = 0.5,color = 'yellow',label = 'Fall',bottom=rain_stock[2])
pyplot.bar(year,rain_fall[3],width = 0.5,color = 'green',label = 'Winter',bottom=rain_stock[3])

pyplot.xlabel('Year')
pyplot.xticks(year)
pyplot.ylabel('Average Rain Fall')
pyplot.ylim(0,1600)

pyplot.legend(loc='upper left')

pyplot.twinx()
pyplot.plot(year,total_avg,color = 'blue',label = 'Rain Fall Average of Year')
pyplot.ylim(0,160)
pyplot.xlabel('Year')
pyplot.ylabel('Average Fall Rain of year')
pyplot.title('Weather Graph')
pyplot.legend(loc='upper right')

pyplot.show()


