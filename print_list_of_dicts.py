# Define función para imprimir lista de diccionarios
def print_list_of_dicts():
    # Asigna datos de tres personas a tres diccionarios
    first_person = {
        "name": "Alicia",
        "last_name": "Araya",
        "phone_number": 925326109
    }
    
    second_person = {
        "name": "Benjamin",
        "last_name": "Bravo",
        "phone_number": 958777052
    }
    
    third_person = {
        "name": "Carolina",
        "last_name": "Cortés",
        "phone_number": 980573025
    }
    
    # Asigna diccionarios creados a una lista
    list_of_dicts = [first_person, second_person, third_person]
    
    # Imprime lista de diccionarios
    print(list_of_dicts)

# Añade convención
if __name__ == "__main__":
    print_list_of_dicts()