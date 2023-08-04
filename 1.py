import base64
import hashlib

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((25 - (ord(char) - ascii_offset)) + ascii_offset)
        else:
            result += char
    return result

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    print("Bienvenido al programa de cifrado y descifrado")

    while True:
        print("\nMenú de Cifrado:")
        print("1. Cifrado César")
        print("2. Cifrado Atbash")
        print("3. Codificación Base64")
        print("4. Hash MD5")
        print("5. Salir")

        choice1 = input("Seleccione un tipo de cifrado (1/2/3/4/5): ")

        if choice1 == '1':
            shift = int(input("Ingrese el valor de desplazamiento para el cifrado César: "))
            message = input("Ingrese el mensaje o código a cifrar: ")
            encrypted_message = caesar_cipher(message, shift)
            print("Mensaje cifrado:", encrypted_message)

        elif choice1 == '2':
            message = input("Ingrese el mensaje o código a cifrar con el cifrado Atbash: ")
            encrypted_message = atbash_cipher(message)
            print("Mensaje cifrado con Atbash:", encrypted_message)

        elif choice1 == '3':
            choice2 = input("¿Desea codificar (E) o decodificar (D) en Base64?: ")
            message = input("Ingrese el mensaje o código: ")

            if choice2.lower() == 'e':
                encoded_message = base64_encode(message)
                print("Mensaje codificado en Base64:", encoded_message)
            elif choice2.lower() == 'd':
                decoded_message = base64_decode(message)
                print("Mensaje decodificado de Base64:", decoded_message)
            else:
                print("Opción no válida")

        elif choice1 == '4':
            message = input("Ingrese el mensaje para generar el hash MD5: ")
            hashed_message = md5_hash(message)
            print("Hash MD5:", hashed_message)

        elif choice1 == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

