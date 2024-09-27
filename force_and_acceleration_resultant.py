import re, os, curses, random

# Vectors must have (Fx, Fy, Fz) format and are float that can be negative.
VECTOR_REGEX = r"^\s*\(?\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)?\s*$"

def main():
    quantity = 5
    vector_retrieve_method = get_user_option()

    vectors = vector_retrieve_method(5)


def validate_vector(input: str):
    return re.match(VECTOR_REGEX, input)

def clear_console():
    os.system('cls') # Only works for windows for now

def log(vectors, mass, force, acceleration):
    log_str = "Vetores utilizados:\n"
    for index, vector in enumerate(vectors):
        log_str += f'{index + 1}: ({vector[0]:.2f}, {vector[1]:.2f}, {vector[2]:.2f})\n'

    log_str += f'Massa: {mass:.2f} kg\n'
    log_str += f'Força resultante: ({force[0]:.2f}, {force[1]:.2f}, {force[2]:.2f})\n'
    log_str += f'Aceleração resultante: ({acceleration[0]:.2f}, {acceleration[1]:.2f}, {acceleration[2]:.2f})\n'

    print(log_str)

    with open('log.txt', 'w') as log_file:
        log_file.write(log_str)

def get_vectors_by_file(quantity):
    pass

def get_vectors_by_input(quantity):
    pass

def get_vectors_randomly(quantity):
    min_value = float(input("Informe o valor mínimo dos vetores que serão gerados: "))
    max_value = float(input("Informe o valor máximo dos vetores que serão gerados: "))

    return [(random.uniform(min_value, max_value), random.uniform(min_value, max_value), random.uniform(min_value, max_value))
               for _ in range(quantity)]

def get_user_option():
    return curses.wrapper(menu)

def menu(console):
    curses.curs_set(0)
    current_option = 0
    options = {
        "Inserir vetores manualmente": get_vectors_by_input,
        "Inserir vetores via arquivo": get_vectors_by_file,
        "Inserir vetores randomicamente": get_vectors_randomly
    }

    while True:
        console.clear()
        for index, option in enumerate(options.keys()):
            option_str = f'>> {option}' if index == current_option else f'   {option}'
            console.addstr(index, 0, option_str)

        key = console.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            dict_key = list(options.keys())[current_option]
            return options[dict_key]

        console.refresh()

if __name__ == '__main__':
    main()