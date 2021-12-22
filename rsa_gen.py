import sys

c = []
c_bin = []
textDec = ""

P = int(sys.argv[1])
Q = int(sys.argv[2])

N = P * Q
M = (P-1)*(Q-1)

d = 3
while d < 20:
    div = str(M/d)

    if(div[int(str(div).find('.'))+1] != 0 ):
        break
    else:
        d += 1

e = 2
while True:
    if( ((e * d) % M) == 1):
        break
    else: 
        e += 1


print("\n P: " + str(P) + " | Q: " + str(Q))
print("\n N: " + str(N) + " | M: " + str(M))
print("\n e: " + str(e) + " | d: " + str(d))
print("\n\n Kpr: (" + str(N) + ", " + str(e) +") | Kpb: (" + str(N) + ", " + str(d) +")" + "\n")


text = "test"
for char in text:
    c.append(ord(char)**e % N)

for char in c:
    textDec += chr(char**d % N)

print("\n Text to crypt: " + text + "\n")
print(" Crypted text: " + str(c) + "\n")
print(" Encrypted text: " + textDec + "\n")
