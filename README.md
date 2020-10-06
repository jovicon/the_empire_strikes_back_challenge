# The Empire strikes back challenge
**The Empire strikes back challenge**   
**VueJs + FastAPI Version**  

![Continuous Integration and Delivery](https://github.com/jovicon/the_empire_strikes_back_challenge/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)

## Description:
Necesitamos tu ayuda para poder derrocar al imperio el cual ha dominado la galaxia durante
30 años y hemos formado una alianza, en donde estamos
reclutando tripulaciones para que nos apoyen en esta guerra. Tu deber como developer
será ayudarnos con la implementación de un software el cual tendrá como objetivo
mantener un orden, ya que hoy en día no se tiene un conteo de cuántas tripulaciones
existen.  

<br>

### BACK
Usando un framework (en Python o Javascript/typescript) con el que te sientas más
cómodo, deberás crear un servicio que recibirá y devolverá información de tripulaciones.

<br>

1. **Asegurarse de crear un servicio REST que contenga los siguientes endpoints:**

<br>

* **Crear una tripulación,** para ellos se tendrá que guardar en una base de datos (libre elección) la siguiente información:  
   ID de la tripulación  
   Nombre de la tripulación  
   Cantidad de tripulantes  
   Modelo de la nave espacial  
   Costo de la nave espacial  
   Velocidad máxima de la nave espacial  

<br>

* **Listar tripulaciones,** importante:  
   Deberás crear una paginación para este endpoint
<br>

* **Se podrá buscar por nombre de tripulación**
<br>

* **Obtener una tripulación con la información detallada (dado un ID)**
<br>

* **Eliminar una tripulación (dado un ID)**
<br>

* **Editar una tripulación (dado un ID)**
<br>

2. Tests unitarios con coverage de código > 80

<br>

3. Crear documentación para cada endpoint del servicio

<br>

Ten en cuenta que este servicio a futuro utilizará servicios externos, 
y puede que se necesite hacer cambios a futuro, 
por ende necesitamos que sea los más escalable y flexible posible.

#### BONUS
* Dockerizar
* Cree un microservicio para lo anterior y conéctelo usando docker-compose
<br>

### FRONT
Para el desarrollo del Front, podrás utilizar entre Angular 2+, Vue.js o React, siéntete libre
de utilizar la librería UI open source que más te acomode.  


1. La primera pantalla deberá listar el nombre de todas las tripulaciones existentes, con
un límite de 6 tripulaciones por página.

2. Cada tripulación tendrá las opciones de editar, detalle y eliminar, en los casos de
editar y mostrar información se deberá mostrar una modal.

3. En la parte superior de la pantalla, deberás tener una barra de búsqueda, la cual
buscará una tripulación dado el nombre, sería ideal que fuera Live Search.

4. Deberás implementar un botón para agregar una nueva tripulación.
Cada cambio se debe ver reflejado en la lista de tripulación.

#### BONUS
* Dockerizar
* Styled Components
* Hooks

En la página 3, hemos dejado un ejemplo guía de como podría ser el diseño.
Una vez terminado, envíanos el link del repositorio público para que podamos revisarlo y por
favor no olvides crear un README con la instrucciones para levantar el proyecto.
Éxito!!
<br>

## Solution:  

Las tecnologias Jedi seleccionadas para enfrentar el reto son las siguientes:

### Backend: 

**FastAPI**
1. Es un Framework fuertemente inspirado en Flask 
2. Toma ventaja sobre Python type para validacion de datos
3. Es rapido, gracias a soportar "async mode"
4. Full compatibilidad con OpenAPI y JSON
5. Tiene excelente documentacion 

<br>