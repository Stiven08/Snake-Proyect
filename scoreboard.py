from turtle import Turtle

"""
En esta sección del codigo estamos creando las variables predeterminadas las cuales se usaran posteriormente.
Estas variables cuentan con la función de proporcionar las propíedades del formato de fuente de nuestros textos en la aplicación.
"""
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    
    """
    Estamos creando la clase Scoreboard en la cual estamos heredando de la clase Turtle para poder acceder a los objetos y a los metodos alojados en esta clase.
    
    Turtle (class): Estamos heredando de esta clase tanto sus metodos como sus objetos, para posteriormente usarla dentro de nuestra clase Food.
    """
    def __init__(self):
        """
        Este metodo crea el objeto que nos va a mostrar el texto  del marcador"Score" actual el cual se crea una variable inicializada en cero, que permitirá llevar el contador del marcador cada vez que la serpiente colisione con el objeto food este se aumentará.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        """
        Este metodo permitirá actualizar el marcador en tiempo real.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        """
        Este metodo se muestra cuando el juego termina y a su vez visualiza el mensaje de juego terminado.
        """
        self.goto(0, 0)
        self.write("GAME OVER",
        align=ALIGNMENT, font=FONT)
    def increase_score(self):
        """
        Este metodo incrementa los puntos del marcador cada vez que la serpiente colisiona con el objeto food.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()