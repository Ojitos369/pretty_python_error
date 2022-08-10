from tools import show_error

def main():
    try:
        number_1 = int(input('Ingrese el primer numero: '))
        number_2 = int(input('Ingrese el segundo numero: '))
        result = number_1 / number_2
        print(f'El resultado es: {result}')
    except Exception as e:
        error = show_error(e, send_email = True)
        print(error)
        raise e


if __name__ == '__main__':
    main()
    