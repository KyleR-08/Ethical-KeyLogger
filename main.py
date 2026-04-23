import keyboard

file = "keyboard.txt"
print("Iniciando el programa de keyboardlogger, se guardará todo lo que escribas en un archivo llamado keyboard.txt")
print("Presiona escape para salir del programa, y guardar lo que escribió")
while True:
    if keyboard.is_pressed('esc'):
        print("Cerrando programa")
        break   
    else:
        with open(file, "a") as f:
            f.write(keyboard.read_event().name)