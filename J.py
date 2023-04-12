cartas = {}
for i in range(1, 14):
    cartas[i] = 4

n = int(input())
joao = list(map(int, input().split()))
maria = list(map(int, input().split()))

Tj = sum(joao)
Tm = sum(maria)

for i in joao:
    cartas[i] -= 1
for i in maria:
    cartas[i] -= 1

x = list(map(int, input().split()))
for i in x:
    cartas[i] -= 1
    Tj += i
    Tm += i

c = []
for i in cartas:
    if cartas[i] > 0:
        c.append(i)

if Tj > 23 or Tm > 23 or Tj == 23:
    print(-1)
else:
    Tj = 23-Tj+1
    Tm = 23-Tm
    menor = 0
    if Tj < Tm:
        while True:
            if Tj in c:
                menor = Tj
                break
            else:
                Tj += 1
            
            if Tj > 13:
                menor = -1
                break
        print(menor)
    else:
        if Tm in c:
            print(Tm)
        else:
            print(-1)
