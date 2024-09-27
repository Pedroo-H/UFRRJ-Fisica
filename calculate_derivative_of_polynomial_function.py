import os

def main():
    clear_console()
    input_str = input("Insira os coeficientes do polinômio em ordem decrescente de potência, separados por espaços: ")
    coefficients = list(map(int, input_str.split()))

    derivatives = differentiate_polynomial(coefficients)

    log_str = f'Polinômio Original:\n {format_polynomial(coefficients)}\n'
    log_str += f'Derivada do polinômio:\n { format_polynomial(derivatives) if derivatives else "0"}\n'

    print(log_str)
    with open('log.txt', 'w') as log_file:
        log_file.write(log_str)


def differentiate_polynomial(coefficients):
    derivatives = []

    degree = len(coefficients) - 1
    for index in range(degree):
        new_coeff = coefficients[index] * (degree - index)
        derivatives.append(new_coeff)

    return derivatives

def format_polynomial(coefficients):
    formatted_polynomial = ""
    degree = len(coefficients) - 1

    for index, coeff in enumerate(coefficients):
        if coeff == 0:
            continue
        # Add "+" or "-" sign correctly
        if coeff > 0 and index > 0:
            formatted_polynomial += " + "
        elif coeff < 0:
            formatted_polynomial += " - "
            coeff = abs(coeff)

        # Build the polynomial term
        if degree - index > 1:
            formatted_polynomial += f"{coeff}x^{degree - index}"
        elif degree - index == 1:
            formatted_polynomial += f"{coeff}x"
        else:
            formatted_polynomial += f"{coeff}"

    return formatted_polynomial

def clear_console():
    os.system('cls') # Only works for windows for now

if __name__ == '__main__':
    main()