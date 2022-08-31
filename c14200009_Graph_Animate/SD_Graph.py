# 7 node graph
#Kalau dibuat bentuk Adjadency Matrix saya ambil contoh dari praktikum SD untuk matrix nya bisa dibuat sesuka hati
#   0 1 2 3 4 5 6
# 0 0 1 1 0 0 0 0
# 1 1 0 0 1 0 0 0
# 2 1 0 0 0 0 1 0
# 3 0 1 0 0 1 0 0
# 4 0 0 0 1 0 1 1
# 5 0 0 1 0 1 0 1
# 6 0 0 0 0 1 1 0

#Untuk x, y atau posisi node nya dapat import random juga

graph = [
# Node 0
[ 'S', #Data yang mau diselipkan pada nodenya
  (400, 40), # x,y position Ini yang akan melakukan pengukuran pada layar, jadi bisa di set sesuka hati yang penting tidak menabrak
  (1, 2) # adjacent nodes
],
# Node 1
[ 'A',
  (300, 140),
  (0, 3)
],
#Node 2
[ 'B',
  (500, 140),
  (0, 5)
],
#Node 3
[ 'C',
  (300, 240),
  (1, 4)
],
#Node 4
[ 'G',
  (300, 340),
  (3, 5, 6)
],
#Node 5
[ 'H',
  (500, 240),
  (2, 4, 6)
],
#Node 6
[ 'F',
  (500, 340),
  (4, 5)
]
]