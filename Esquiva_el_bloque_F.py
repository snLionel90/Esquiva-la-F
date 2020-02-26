
import pygame, sys
import random
import ctypes #importa los pop up
 #------------------------------------------------------------
#Declaracion de las constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
AMARILLO = (240, 200, 20)
 #------------------------------------------------------------
#DECLARACION DE FUNCIONES 
def objeto(pos_x,pos_y):
     canvas.blit(imagen_vehiculo,(pos_x,pos_y))

def bloque(bloque_x,bloque_y,bloque_ancho,bloque_alto):
    canvas.blit(bloque_imagen,(bloque_x,bloque_y,bloque_ancho,bloque_alto))

def bloque_choca():
    if bloque_inicio_y + bloque_alto > y:
        if (x + imagen_vehiculo.get_width() > bloque_inicio_x and x < bloque_inicio_x +bloque_ancho):
            return True
    return False   

def dibujaBordes():
    pygame.draw.line(canvas,AMARILLO,(ANCHO_VENTANA,45),(0,45),3)

def chash():
    global he_chocado
    print ('Te has chocado,pero Has esquivado...' +str(esquivados) +' F')
    he_chocado = True
 #------------------------------------------------------------
#DECLARACION DE VARIABLES
tiempo = pygame.time.Clock()
he_chocado = False
imagen_vehiculo = pygame.image.load('imagenes/ovni.png')
bg = pygame.image.load('imagenes/background.jpg')
bloque_imagen =pygame.image.load('imagenes/misil.png')
 #------------------------------------------------------------
#posicion del vehiculo
x = (ANCHO_VENTANA -imagen_vehiculo.get_width())//2
y = ALTO_VENTANA -imagen_vehiculo.get_height()
incremento_x = 0
incremento_y =0
esquivados = 0
 #------------------------------------------------------------
#posicion del bloque 1
bloque_velocidad =7
bloque_alto = bloque_imagen.get_height()
bloque_ancho = bloque_imagen.get_width()
bloque_inicio_y = -bloque_alto
bloque_inicio_x = random.randrange(0, 800)
 #------------------------------------------------------------
#Iniciamos la ventana
pygame.init()
#Inserto el sonido
pygame.mixer.music.load('./sonidos/techno001.ogg')
pygame.mixer.music.play()

canvas = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption('Esquiva la F, by Lionel Sanchez ')
 #------------------------------------------------------------
#bucle while, eventos de colision y desplazamiento
while not he_chocado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            he_chocado =True
        # si se pulsa una tecla el vehiculo se mueve
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                incremento_x =-5        
            if evento.key == pygame.K_RIGHT:
                incremento_x =5              
            if evento.key == pygame.K_UP:
                incremento_y = -5
            if evento.key == pygame.K_DOWN:
                incremento_y = 5  

        #si se deja de pulsar o se suelta una tecla el vehiculo se detiene
        if evento.type ==pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                incremento_x =0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                incremento_y =0

    # Direccion del vehiculo por la pantalla
    if ((x + incremento_x >=0) and 
        (x+incremento_x +imagen_vehiculo.get_width()
        < ANCHO_VENTANA)):
            x= x+incremento_x

    if ((y + incremento_y >=0) and 
        (y+incremento_y +imagen_vehiculo.get_height()
        < ALTO_VENTANA)):
            y= y+incremento_y
     #------------------------------------------------------------
    #ACTUALOZA EL BLOQUE
    bloque_inicio_y +=bloque_velocidad
    if bloque_inicio_y > ALTO_VENTANA:
        bloque_inicio_y = -bloque_alto
        bloque_inicio_x = random.randrange(0,720)
        esquivados +=1
        bloque_velocidad +=1
               
    if bloque_choca():    
        pygame.mixer.music.load('./sonidos/golpe.ogg')
        pygame.mixer.music.play()
        imagen_vehiculo = pygame.image.load('imagenes/ovni2.png')       
    #mustra un mensaje pop up 
        ctypes.windll.user32.MessageBoxW(0,'Te has chocado con una F.\n\n Has esquivado :' +str(esquivados) + ' F', "GAME OVER", 16)
        chash()
    #------------------------------------------------------------
    #canvas.fill(GRIS)
    canvas.blit(bg, [0,0])
    dibujaBordes()
    #Con las Fuentes e insertamos un texto
    fuente = pygame.font.Font('fonts/Aaah_Speed.ttf', 25) #importa una fuente, del sistema o una personalizada, y su tamaño
    fuente1 = pygame.font.Font('fonts/pixel.ttf',15)
     #------------------------------------------------------------
    #para luego imprimirla en pantalla
    texto1 = fuente.render("ESQUIVA LA F",2, (255, 25, 25)) #texto que imprime en pantalla un texto, y su color
    texto2 = fuente1.render('F evitadas:',2,(255, 25, 25))
    texto3 = fuente1.render(str(esquivados),2,(255, 25, 25)) #imprime por pantalla la cantidad de bloques f esquivados

    #Posiciones del texto en pantalla
    canvas.blit(texto1,[150,14])
    canvas.blit(texto2,[(ANCHO_VENTANA-200),14])
    canvas.blit(texto3,[(ANCHO_VENTANA-50),14])

    bloque (bloque_inicio_x,bloque_inicio_y,bloque_ancho,bloque_alto)#tamaño del bloque en pantalla

    objeto (x,y) #objeto en pantalla
    pygame.display.update()
    tiempo.tick(60)
 
pygame.quit()
sys.exit(0)
