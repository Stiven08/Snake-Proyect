from turtle import Turtle
import random
class Food(Turtle):
    """
    Estamos creando la clase Food en la cual estamos heredando de la clase Turtle para poder acceder a los objetos y a los metodos alojados en esta clase.
    
    Args:
        Turtle (class): Estamos heredando de esta clase tanto sus metodos como sus objetos, para posteriormente usarla dentro de nuestra clase Food.
    """
    def __init__(self):
        
        """
        Este metodo nos permite crear el objeto llamado Food, en el cual estamos proporcionandole propiedades de la clase Turtle de la cual estamos heredando, esto nos permite crear visualmente un objeto Food dentro de nuestra ventana.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        
        """
        Este metodo nos permite cada vez que la serpiente colisione con el objeto food, este cambie la ubicación dentro de nuestra ventana de forma aleatoria por medio de un eje x y un eje y.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

