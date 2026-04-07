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

# v_r != v_l -> trayectoria circular
vr = 4.0  # Rueda exterior (rápida)
vl = 3.0  # Rueda interior (lenta)

left_motor.setVelocity(vl)
right_motor.setVelocity(vr)

# Bucle principal de ejecución
while robot.step(timestep) != -1:
    pass