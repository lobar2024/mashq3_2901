#3
#1
# tupl = (1, 2, 3)
# tupl2 = (4, 5, 6)
# neww = []
#
# for i in range(len(tupl)):
#     neww.append(tupl[i] * tupl2[i])
#
# neww = tuple(neww)
# print(neww)

#2
# tupl = 'Hello World!'
# tupll = tupl[::-1]
# print(tupll)

#3
# text = ("Salom", "Python", "dunyo")
# print(''.join(text))

# tupl = (1, 2, 3, 4, 5, 6, 7)
# katta = f'Tupledaki eng katta son: {max(tupl)}'
# kichik = f'Tupledagi eng kichik son: {min(tupl)}'
# print(katta)
# print(kichik)

# tupl = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# toq = []
# juft = []
# for i in range(len(tupl)):
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)
#
# toq = tuple(toq)
# juft = tuple(juft)
# print(f'Tupledagi barcha toq sonlar: {toq}')
# print(f'Tupledagi barcha juft sonlar: {juft}')

# tuplee = 'Hello world Python'
# soz = tuplee.split()
#
# uzuun = max(soz, key=len)
# indeks = soz.index(uzuun)
#
# print("Eng uzun so‘z:", uzuun)
# print("Indeksi:", indeks)

# t1 = (1, 2, 3)
# t2 = ('a', 'b', 'c')
#
# natija = ()
#
# for i in range(len(t1)):
#     natija += (t1[i], t2[i])
#
# print(natija)
