# Laboratorio 1: Simulación de un Robot Móvil Diferencial en Webots

---

## Descripción del laboratorio
El objetivo de este laboratorio es comprender el comportamiento cinemático de un robot móvil diferencial mediante una simulación interactiva. Utilizando el simulador Webots y un robot e-puck, implementamos un controlador en Python para manipular los actuadores (motores de las ruedas izquierda y derecha.

A través de la variación de las velocidades de cada rueda ($v_r$ y $v_l$), logramos controlar el movimiento del robot para que ejecute trayectorias específicas como línea recta, curvas, rotación sobre su propio eje, e incluso figuras geométricas más complejas como un cuadrado.

**Equipo de Trabajo:**
* **Programador:** [Nombre]
* **Experimentador:** [Nombre]
* **Analista:** [Nombre]
* **Documentador:** [Nombre]
* **Integrador:** [Nombre]

---

## Cómo ejecutar la simulación en Webots
Para probar nuestro código en tu propia computadora, sigue estos pasos:

1. **Requisitos previos:** Se debe tener instalado [Webots](https://cyberbotics.com/) y [Python 3.x](https://www.python.org/) en el sistema.
2. **Clonar el repositorio:** Descarga o clona este repositorio en tu computador. Asegúrate de mantener la estructura original, incluyendo la carpeta `controllers` que contiene los códigos.
3. **Abrir el Mundo:**
   * Abre Webots.
   * Ve a `File` > `Open World...` y selecciona el archivo del mundo `epluck.wbt` incluido en este repositorio.
4. **Cargar el Controlador (Elegir Experimento):**
   * En el panel izquierdo (Árbol de Nodos), despliega las opciones del robot `e-puck`.
   * Busca el campo `controller` y haz clic en `Select...`.
   * En la lista se verán los distintos controladores diseñados para cada prueba (ej. `l_linea_recta`, `2_linea_curva`, `3_rotacion`, etc). Selecciona el experimento deseado.
5. **Ejecutar:** * Guarda los cambios en el mundo presionando el ícono del disquete.
   * Presiona el botón de **Reset** (flecha circular) y luego **Play** (triángulo) en la barra superior de Webots para iniciar la simulación.

* *Nota: Para probar otro experimento, simplemente pausa la simulación y repite el paso 4 eligiendo un controlador diferente.*
---

## Análisis de resultados obtenidos

*¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?*

* El robot se desplaza en una línea recta. Esto sucede porque ambas ruedas recorren exactamente la misma distancia en el mismo tiempo. Físicamente, la velocidad lineal del robot será igual a la velocidad de las ruedas, y su velocidad angular (de giro) será cero. Si la velocidad es positiva, avanza; si es negativa, retrocede en línea recta.


*¿Cómo cambia la trayectoria cuando las velocidades son diferentes?*

* La trayectoria deja de ser recta y se convierte en una curva. Al ir a distintas velocidades, una rueda recorre más distancia que la otra en el mismo tiempo. Esto obliga al chasis del robot a pivotar. La regla general es que el robot siempre va a "doblar" hacia el lado de la rueda que va más lento.

*¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?*

* El robot experimenta una rotación en su propio eje (o rotación en el lugar). Si las velocidades tienen la misma magnitud pero signos contrarios (por ejemplo, $v_r = 2.0$ y $v_l = -2.0$), el avance lineal se anula por completo (velocidad lineal = 0). Toda la energía se convierte en velocidad angular, haciendo que el robot gire como un trompo sin moverse de su posición inicial en el tablero.
  
*¿Qué tipo de movimiento permite dibujar un círculo?*

* Para dibujar un círculo se necesita un movimiento de trayectoria curva constante. Esto se logra configurando velocidades que sean diferentes entre sí, pero que se mantengan fijas durante todo el tiempo de ejecución. Al mantener constante la diferencia de velocidad, el radio de giro no cambia, lo que provoca que la curva eventualmente se cierre sobre sí misma formando un círculo. (Mientras mayor sea la diferencia entre las velocidades, más pequeño y cerrado será el círculo).

***Extra**: ¿Qué tipo de control se requiere para dibujar un cuadrado?*

* A diferencia de la línea recta o el círculo, que utilizan velocidades constantes desde el inicio hasta el fin, dibujar un cuadrado requiere un control dinámico basado en secuencias de tiempo. El robot no puede mantener la misma velocidad siempre, sino que debe alternar entre dos estados distintos:
  1. Desplazamiento: Avanzar en línea recta ($v_r = v_l$) durante un tiempo específico para trazar uno de los lados.
  2. Giro: Detener el avance y rotar sobre su propio eje ($v_r = -v_l$) durante una fracción de segundo exacta para lograr un ángulo de 90 grados.

* Este proceso (avanzar y girar) debe programarse en un bucle que se repita exactamente cuatro veces para cerrar la figura geométrica.

*(Nota: Se puede revisar la carpeta `/multimedia` de este repositorio para ver videos del robot completando estos desafíos).*
