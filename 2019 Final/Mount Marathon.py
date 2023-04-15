n = int(input())
l = list(map(int, input().split()))
cards = []

m = []
for i in l:
    if len(m) == 0:
        m = [i]
    
    elif i <= m[-1]:
        m.append(i)
    else:
        cards.append(m)
        m = [i]
if m:
    cards.append(m)
print(len(cards))