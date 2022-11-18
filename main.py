"""
Importamos las librerías necesarias en este caso importamos turtle  la cual nos va a permitir desarrollar toda la parte gráfica y funcionalidad. 
Así mismo importamos time que nos permitirá contar el tiempo desde la ejecución y nos permitirá controlar el flujo de tiempo de nuestra app.

Importamos los documentos tipo py e importamos sus clases la cuales tienen incluido funcionalidades que nos permitirán que nuestra app funcione correctamente.
"""
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

"""
Esta seccion del codigo  creamos la ventana de la app la cual le definimos la propiedades como el tamaño  el color de fondo  el titulo  de la ventana ó aplicacion asimismo la actualizacion automatica de la ventana.
"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(1)

"""
Se isntansa las clases que importamos anteriormente a una variable para poder acceder a las funcioanlidades que se encuentran en estas clases.
Aqui se define el movimiento de la serpiente y los puntos que se van agregando.
"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen() #Este permite leer las entradas de pantalla/ventana.
"""
Aqui se define el funcionamiento del movimiento de la serpiente por medio del teclado.
Asi mismo estamos accediendo a una funcionalidad de la clase Snake, la cual nos permite controlar la direccion de la cabeza de la serpiente por medio de las flechas del teclado.
"""
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""
Se crea una bandera en "verdadero/True" la cual va a permitir que el juego este encendido, mientras esta bandera permanezca en "verdadero/True" la ejecucion del ju8ego continuará, pero en el caso de que la bandera cambie a "falso/False", el juego se detendra.

Por medio de un ciclo "mientras/while" ejecutamos la funcionalidad del juego.
"""
game_is_on = True
while game_is_on:
    screen.update() #Este metodo nos permite que la ventana permanezca en actualizacion 
    time.sleep(0.1) #Esta funcionalidad nos permite que la actualizacion de la ventana se retrase por el valor indicado, esto quiere decir que nuestro juego fluya de manera controlada.
    snake.move() # Este metodo de la clase Snake nos permite controlar el movimiento de la serpiente en la ventana en donde cambia su posició en eje x y en eje y.
    
    #Detect collision with food.
    """
    La condicion nos permite verificar la distancia entre objeto "head" que pertenece a la clase Snake y el objeto "food" que instancio de la clase Food, en el caso de que el objeto "head" este a una distancia menor a 20 del objeto food este ejecutará 3 metodos de 3 distintas clases.
    """
    if snake.head.distance(food) < 20:
        food.refresh() #Cuando el objeto "head" colisiona con el objeto "food" este se refrescará y reapareserá en otra ubicación dentro de la ventana.
        snake.extend() #Cuando el objeto "head" colisiona con el objeto "food", el objeto Snake crecerá y se creará un nuevo segmento al final del Snake.
        scoreboard.increase_score() #Cuando el objeto "head" colisiona con el objeto "food", este incrementará el resultado actual y le sumaría 1 cada vez que colisione con el objeto food.
        
#Detect collision with wall.
    """
    Aqui se esta definiendo que cuando la cabeza de la serpiente colisione con el limite de las  coordenadas "x" y con el limite de las coordenadas "y", que son las dimensiones de la ventana, este terminará el juego.
    """
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False #Cuando la condición sea verdadera y el objeto "head" colicione con uno de los limites de la ventana, tanto en eje y como en eje x, este cambiará el valor de la bandera creada y quedará en falso, por lo tanto este terminará la ejecución del ciclo.
        scoreboard.game_over() #Cuando la condición se cumpla este ejecutará un mensaje en el centro de la ventana indicando que el juego a terminado.
        
#Detect collision with tail.
    """
    Este ciclo nos permite ingresar a cada elemento de los segmentos de la serpiente, y por medio de condiciones estamos verificando la distancia entre la cabeza de la serpiente y los demás segmentos que le siguen los cuales serían la cola de la serpiente.
    """
    for segment in snake.segments:
        if segment == snake.head:
            #Esta condición verifica que el primer segmento sea la cabeza de la serpiente, y continue funcionando. 
            pass
        elif snake.head.distance(segment) < 10:
            #Esta condición verifica la distancia que hay entre la cabeza de la serpiente y los demas segmentos que le siguen los cuales serian la cola de la serpiente y en el caso de que la distancia sea menor a 10, el juego termina y ejecuta un mensaje de juego terminado.
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick() #Este metodo lo que hace es que cuando se termine la funcionalidad, por medio de un click en la ventana este cierra la ventana, en el caso de que esta función no se llame dentro del codigo una vez finalizada la función de nuestra App, la ventana se cerrará automaticamente.
