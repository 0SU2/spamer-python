import keyboard
import time

ENTER = "enter"
ESC = "esc"
SALIR = False
NOMBRE_ARCHIVO = "archivo.txt"

def salir() -> None:
  global SALIR
  SALIR = False
  print("Saliendo del programa...")

def envia_mensaje(msj: str="" ) -> None:
   keyboard.write(msj)
   keyboard.press(ENTER)
   print(f"ENVIADO: {msj=}")
  

def main() -> None:
  keyboard.add_hotkey(ESC, lambda: salir())
  print("Esperando....")
  time.sleep(5)
  
  while SALIR != False:
     with open(NOMBRE_ARCHIVO, "r") as archivo:
        for line in archivo:
           for palabra in line.split():
              time.sleep(0.1)
              if SALIR:
                 salir()
              envia_mensaje(palabra.strip())
              
if __name__ == "__main__":
   main()

