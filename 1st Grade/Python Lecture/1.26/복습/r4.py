s = []
while True:
    score = int(input())
    if score == 0:
        break
    s.append(score)
    
print(s)
total = 0
for i in range(len(s)):
    total += s[i]
print('Avg = %.2f'%float(total/int(len(s))))

#정답
