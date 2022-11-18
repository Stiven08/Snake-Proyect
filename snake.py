"""Importamos las librerías necesarias en este caso importamos turtle  la cual nos va a permitir desarrollar toda la parte gráfica y funcionalidad.""" 
from turtle import Turtle

"""
En esta sección del codigo definimos las variables predeterminadas las cuales se usarán posteriormente en la funcionalidad de esta clase.
"""
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)] #Esta variable define la posición inicial de los tres primeros segmentos.
MOVE_DISTANCE = 20 #Esta variable define la distancia en la que se van a mover los objetos.

"""
Estas variables (UP,DOWN,LEFT,RIGTH) tienen un dato entero, el cual es la dirección en grados, por lo tanto Up tiene como valor "90 grados" el cual sería la dirección dirigida hacia arriba, Down tiene como valor "270 grados" el cual seria la direccion dirigida hacia abajo, Left tiene como valor "180 grados" el cual seria la direcion dirigida hacia la izquierda, Right tiene como valor "0 grados" el cual seria la direcion dirigida hacia la derecha.
"""
UP = 90 
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake: #En esta linea de codigo creamos la clase  la cuaol va almacenar las funciones y objetos de esta.
    
    def __init__(self):
        """
        Este metodo crea el objeto de la serpiente la cual esta compuesta por la cabeza  y los segmentos que serian la cola de la misma
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        """
        Este metodo crea el cuerpo de la serpiente la  cual  va a tomar los valores de "STARTING_POSITIONS" para inicializarla en una posicion predeterminada
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        """
        Este metodo nos permite crear o añadir segmentos al objeto de la serpiente mediante unos parametros para darle la ubicacion y este conectada a la misma asi mismo asignandoles propiedades que sean iguales al el primer segmento.

        Args:
            position (tuple): Este parametro es una tupla en donde tiene dos datos los cuales son enteros y su funcion es brindar la posicion del nuevo segmento
        """
        new_segment = Turtle("square")
        new_segment.speed(0)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        """
        Este metodo permite llamar la funcion añadir segmento con el fin de proporcionarle la nueva ubicacion que va a tener el nuevo segmento cada vez que la serpiente coma 
        el objeto llamado food, este crecera.
        """
        self.add_segment(self.segments[-1].position())
    def move(self):
        """
        Este metodo de la clase Snake nos permite controlar el movimiento de la serpiente en la ventana en donde cambia su posició en eje x y en eje y.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    """
    Este metodo nos permite darle dirección a la serpiente por medio de las variables creadas anteriormente las cuales proporcionan la dirección por medio de grados, por lo tanto, cada vez que accionemos un boton de flecha (UP,DOWN,LEFT,RIGTH) este redirigirá a la serpiente.
    """    
    def up(self): 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)