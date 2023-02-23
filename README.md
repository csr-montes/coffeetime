# CoffeeTime

CoffeeTime es una aplicación que monitorea la actividad del usuario y realiza una acción si no detecta actividad en un período de tiempo determinado. Esta aplicación está escrita en Python y utiliza la biblioteca de interfaz gráfica de usuario (GUI) de tkinter, la biblioteca de hilos, la biblioteca de automatización de GUI pyautogui y las bibliotecas de entrada del mouse y el teclado de pynput.

## Instalación

Para utilizar CoffeeTime, es necesario tener instalado Python en su versión 3.7 o superior. También es necesario instalar las bibliotecas de tkinter, threading, pyautogui y pynput. Puede hacerlo mediante la siguiente línea de comandos:

    pip install tkinter threading pyautogui pynput 

## Uso

Para utilizar CoffeeTime, ejecute el siguiente comando en una ventana de terminal:

    python coffeetime.py

Al ejecutar la aplicación, aparecerá una ventana con un botón "Activar / Desactivar". Al hacer clic en este botón, la aplicación comenzará a monitorear la actividad del usuario. Si no se detecta actividad durante un minuto, la aplicación registrará la inactividad en un registro y realizará una serie de acciones para simular actividad y evitar que la computadora entre en modo de suspensión.

Para detener la aplicación, simplemente haga clic en el botón "Activar / Desactivar" nuevamente.

## Contribuciones

Las contribuciones a CoffeeTime son bienvenidas. Si desea contribuir, haga lo siguiente:

1.  Fork el repositorio.
2.  Cree una rama con su nueva función (`git checkout -b mi-nueva-funcion`).
3.  Haga sus cambios y pruebas.
4.  Confirme sus cambios (`git commit -am 'Agregando una nueva función'`).
5.  Envíe su rama (`git push origin mi-nueva-funcion`).
6.  Abra una solicitud de extracción en GitHub.

## Contacto

Si tiene preguntas o problemas con CoffeeTime, no dude en ponerse en contacto con el autor a través de GitHub o por correo electrónico.
