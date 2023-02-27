# HW2:
#   create a function (generalMark) which receives 3 numbers from a dictionary

#   IN{
#      'sem_1' : 9.0
#      'sem_2' : 8.0
#      'exam' : 9.0
#    }

#   OUT{
#      'sem_1' : 9.0
#      'sem_2' : 8.0
#      'exam' : 9.0
#      'gen' : 8.66
#    }

def generalMark(nota):
    sem_1 = nota['sem_1']
    sem_2 = nota['sem_2']  
    sem_3 = nota['sem_3']
    nota_general = (sem_1 + sem_2 + sem_3) / 3 # do math
    # nota['nota_general'] = round(nota_general, 2) # extract only after. last second num
    nota['nota_general'] = format(nota_general, '.2f') # extract only after. last second num

    return nota

nota = {
    'sem_1' : 9.0,
    'sem_2' : 8.0,
    'sem_3' : 9.0,
}

update_nota = generalMark(nota)
print(update_nota)

# generalMark(nota) # second vatiant OUT
# print(nota)
