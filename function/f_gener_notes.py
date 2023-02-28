nota = {
    'sem_1': 9.0,
    'sem_2': 8.0,
    'sem_3': 9.0,
}

def generalMark(nota):

    charge_dict = {    }  # dictionar rec 

    charge_dict["sem_1"] = nota["sem_1"]
    charge_dict["sem_2"] = nota['sem_2']
    charge_dict["sem_3"] = nota['sem_3']
    x = ( nota["sem_1"] + nota["sem_2"] + nota["sem_3"] ) / 3
    charge_dict["gen_exam"] = format(x, '.2f')

    return charge_dict

x = generalMark(nota)

print(x)
