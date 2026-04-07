# Laboratorio 1: Simulación de un Robot Móvil Diferencial en Webots

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
2. **Clonar el repositorio:** Descarga o clona este repositorio en tu computador.
3. **Abrir el Mundo:**
   * Abre Webots.
   * Ve a `File` > `Open World...` y selecciona el archivo del mundo `.wbt` incluido en este repositorio (o crea un nuevo mundo y añade un robot `e-puck`).
4. **Cargar el Controlador:**
   * En el panel izquierdo (Árbol de Nodos), despliega las opciones del robot `e-puck`.
   * Busca el campo `controller`, haz clic en `Select...` y elige nuestro archivo de Python (`[Nombre de tu archivo de controlador].py`).
5. **Ejecutar:** * Guarda los cambios presionando el ícono del disquete.
   * Presiona el botón de **Reset** (flecha circular) y luego **Play** (triángulo) en la barra superior de Webots para iniciar la simulación.

---

## Resultados obtenidos
Durante la experimentación, modificamos las velocidades de las ruedas y observamos los siguientes comportamientos cinemáticos:

* **Movimiento Recto ($v_r = v_l$):** Al asignar la misma velocidad a ambos motores (Ej. $v_r = 2.0$, $v_l = 2.0$), el robot avanzó en una línea recta perfecta, ya que el desplazamiento en ambos lados es idéntico.
* **Trayectoria Curva ($v_r \neq v_l$):** Al asignar [explica brevemente los valores que usaron, ej: una velocidad mayor a la rueda derecha], el robot describió un arco, girando siempre en dirección hacia la rueda más lenta.
* **Rotación en el lugar ($v_r = -v_l$):** Al establecer velocidades de igual magnitud pero con signos opuestos (Ej. $v_r = 2.0$, $v_l = -2.0$), el robot giró sobre su propio eje sin desplazarse, logrando un radio de giro igual a cero.
* **Desafío Cuadrado:** Implementamos un bucle basado en el tiempo interno del simulador. Logramos que el robot dibujara un cuadrado alternando un movimiento recto de [X] segundos con una rotación de 90 grados que duró exactamente [X] segundos.

*(Nota: Se puede revisar la carpeta `/multimedia` de este repositorio para ver capturas de pantalla y videos del robot completando estos desafíos).*
