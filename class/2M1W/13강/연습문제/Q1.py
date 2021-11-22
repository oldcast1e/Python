from matplotlib import pyplot

month = ('1','2','3','4','5','6','7','8','9','10','11','12')
avg_temp = [0.5,2.0,6.7,12.7,18.6,21.7,24.4,25.2,20.5,15.0,10.0,3.5]

pyplot.bar (month,avg_temp,width=0.4,color = 'blue',label = 'Average Tempt')
pyplot.xlabel('Month')
pyplot.ylabel('Temp')
pyplot.title('Transform of Temperature')
pyplot.legend(loc = 'upper right')
pyplot.show()