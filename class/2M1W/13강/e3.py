#matplotlib 사용하기
from matplotlib import pyplot

x_name = ('1','2','3','4','5','6','7','8','9','10','11','12')
temp_2018 = [0.5,2.0,6.7,12.7,18.6,21.7,24.4,25.2,20.5,15.0,10.0,3.5]

pyplot.bar(x_name,temp_2018,
    width =0.4,color = 'red',label='temp 2018')
pyplot.xlabel('Month')
pyplot.ylabel('Average Temperature')
pyplot.title("Weather Bar Chart")
pyplot.legend(loc='upper right')
pyplot.show()