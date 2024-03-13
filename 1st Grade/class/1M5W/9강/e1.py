""" fid  = open("python.txt","r")
result = fid.read()
print(result)
fid.close() """

fid = open("Output.txt",'w')
fid.write('This is the final result')
fid.close()
print()
fid = open('Output.txt','a')
value = 'Final result is 100'
fid.write(value)
fid.close()

fid  = open("Output.txt","r")
result = fid.read()
print(result)
fid.close()