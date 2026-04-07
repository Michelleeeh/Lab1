from controller import Robot

# 1. Inicialización básica
robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# 2. Configuración de Tiempos
tiempo_recto = 3.0  # Segundos que el robot avanzará recto
tiempo_giro = 1.5  # Segundos que el robot rotará

# 3. Variables para controlar la secuencia
estado = "recto"        # El robot empieza avanzando
lados_completados = 0   # Contador de lados del cuadrado
tiempo_inicio = robot.getTime()

# 4. Bucle principal
while robot.step(timestep) != -1:
    tiempo_actual = robot.getTime()
    tiempo_transcurrido = tiempo_actual - tiempo_inicio

    # Frena al hacer 4 lados
    if lados_completados >= 4:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        continue # El robot se queda quieto para siempre

    # Lógica de la secuencia
    if estado == "recto":
        left_motor.setVelocity(2.0)
        right_motor.setVelocity(2.0)
        
        # Si ya pasó el tiempo de avanzar recto, cambia a girar
        if tiempo_transcurrido >= tiempo_recto:
            estado = "giro"
            tiempo_inicio = robot.getTime() # Reiniciamos el cronómetro
            
    elif estado == "giro":
        # Rotación en el lugar (v_r = -v_l)
        left_motor.setVelocity(-1.5)
        right_motor.setVelocity(1.5)
        
        # Si ya pasó el tiempo de girar, completa un lado y vuelve a recto
        if tiempo_transcurrido >= tiempo_giro:
            estado = "recto"
            lados_completados += 1          # Sumamos un lado al contador
            tiempo_inicio = robot.getTime() # Reiniciamos el cronómetro

