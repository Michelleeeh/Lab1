from controller import Robot

# Inicializar el objeto Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Configurar los motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Posición infinita para controlar por velocidad
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# v_r = -v_l -> rotación
vr = 2.0   # Rueda derecha hacia adelante
vl = -2.0  # Rueda izquierda en reversa

left_motor.setVelocity(vl)
right_motor.setVelocity(vr)

# Bucle principal de ejecución
while robot.step(timestep) != -1:
    pass