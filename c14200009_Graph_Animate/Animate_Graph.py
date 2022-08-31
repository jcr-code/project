import pygame
from SD_Graph import graph

# Konstanta
display_width = 800
display_height = 600
radius = 30 #Ukuran lingkaran
speed = 1 # frames per sec makin kecil makin lama

#WARNA
grey = (100, 100, 100)  # Melambangkan belum ditemukan
white = (255, 255, 255)  # edge yang sudah ditermukan atau outline node yang dibuat
yellow = (200, 200, 0)  # Node yang edge nya sedang dituju
red = (200,0,0) # node yang sudah ditemukan
black = (0, 0, 0)  # node yang belum ditemukan
green = (0,201,87) # node yang sudah ditemukan dan seluruh edgenya sudah dituju

#Initialisasi pygame
pygame.init()

#Text Box
font = pygame.font.SysFont('ARIAL', 26)
class TextBox: #Class text untuk menampilkan tulisan
    #Pemanggilan drawing_text menerima data dan juga posisi x dan y sedangkan (255,255,255) adalah warna putih
    def drawing_text(self, msg, x, y):
        text_surface = font.render(msg, True, (255, 255, 255))
        screen.blit(text_surface, (x, y))

    def drawing_timer(self, msg):
        text = font.render(msg, True, (255, 255, 255))
        screen.blit(text, (display_width / 2 - 500, display_height / 2))

def run(isi):
    global screen, edges, clock

    # Membentuk Screen
    screen = pygame.display.set_mode((display_width, display_height))
    # Object waktu dari class time milik pygame dideklarasikan
    clock = pygame.time.Clock()

    # graph nya ditambahkan elemen warna, warna nya dibuat diatas konstant dapat diganti sesuai keinginan
    for element in graph:
      element.extend([grey, black]) #Mengeksten warna pada graph nya jika baru dibuat

    build_edges() #Megenerate edges nya

    draw_graph() # menggambar graphnya terlebih dahulu
    update()
    pygame.time.delay(2000) # menunggu 2 detik dalam milisecond baru dimulai animasinya

    if isi.lower() == 'bfs':
        # Loop menggunakan Algoritma BFS di block jika ingin menampilkan dengan DFS, bisa di unblock jika ingin BFS
        queue = [0]  # Node awal, start dari queue node ini
        while len(queue) > 0:
            n1 = queue.pop(0)  # dequeue node
            current = graph[n1]
            current[3] = white  # node saat ini
            current[4] = yellow
            for n2 in current[2]:
                if graph[n2][4] == black and n2 not in queue:  # belum ditemukan atau dituju
                    queue.append(n2)  # node nya di enqueue
                    # n2 yang ditemukan, warna n2 and edge n1,n2
                    graph[n2][3] = white
                    graph[n2][4] = red
                    edges[edge_id(n1, n2)][1] = white
                    update()
            # Jika sudah complete maka
            current[4] = green  # Warna nodenya diganti dengan warna hijau dan update screennya
            update()

    if isi.lower() == 'dfs':
        # Loop menggunakan Algoritma DFS di block untuk tidak menggunakan DFS di unblock untuk menggunakan DFS
        visited = [False] * 7  # Intinya visited di set sebanyak node yang ada
        DFSUtil(0, visited)

    while 1:  # Menuggu atau loading
        pygame.time.wait(5000) # 5 detik dalam milisecon

def DFSUtil(src, visited):
    global edges
    visited[src] = True
    current = graph[src]
    current[3] = white
    current[4] = yellow
    for n2 in current[2]:
        if graph[n2][4] == black and visited[n2] == False:  # belum ditemukan atau dituju
            graph[n2][3] = white
            graph[n2][4] = red
            edges[edge_id(src, n2)][1] = white
            update()
            DFSUtil(n2, visited)
    # Jika sudah complete maka
    current[4] = green  # Warna nodenya diganti dengan warna hijau dan update screennya
    update()

# untuk menormalisasikan posisi node CONTOH : Node 1 ke Node 2, berarti Node 2 ke Node 1 juga bisa ini harus disamakan dengan di sort dan kembalikan ke bentuk tuple ()
def edge_id(n1, n2): return tuple(sorted((n1, n2)))

def build_edges():
    global edges #Merupakan sebuah dictionary dan di global agar dapat digunakan diluar scopenya
    edges = {} # edgeid: [(n1,n2), color]
    for n1, (_, _, adjacents, _, _) in enumerate(graph):
        for n2 in adjacents:
            eid = edge_id(n1, n2)
            if eid not in edges:
                edges[eid] = [(n1, n2), grey]

def draw_graph():
    global graph, screen, edges

    screen.fill((0, 0, 0,)) #Fill Screennya dengan warna hitam

    for e in edges.values(): # draw edges
        (n1, n2), color = e
        pygame.draw.line(screen, color, graph[n1][1], graph[n2][1], 2)

    for data, xy, _, lcolor, fcolor in graph: # draw nodes
        circle_fill(data, xy, lcolor, fcolor, 25, 2)

def update(): #Seluruh update dalam pygame dimasukkan di sini termasuk menggambar kembali graphnya
  global clock
  draw_graph()
  pygame.display.update()
  clock.tick(speed)

#Pembuatan Circle disini
def circle_fill(data, xy, line_color, fill_color, radius, thickness):
    global screen
    pygame.draw.circle(screen, line_color, xy, radius)
    pygame.draw.circle(screen, fill_color, xy, radius - thickness)
    x = xy[0] - 13
    y = xy[1] - 15
    TextBox().drawing_text(str(data), x, y)

isian = input('Ketik DFS untuk proses DFS atau BFS untuk proses BFS : ')
run(isian)