# Do you want delivery ?
# 1. Yes
# 2. No

def inputInt(message):
    try:
        answer = int(input(message))
        return answer
    except:
        print('Error: the answee must be the only of integer value.')

def confirm(question):
    message = f'{question}\n1. Yes\n2. No\n> '
    answer = inputInt(message)
    if answer == 1:
        return True
    elif answer == 2:
        return False

###############  Main program  ##################
delivery = confirm('Do you want delivery ? ')
club_card = confirm('Do you have club card ? ')
print(delivery, club_card)
##################################################            