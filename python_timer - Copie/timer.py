import time
import playsound
from colorama import Fore

def timertest(): 
  print("Let's go!👊 \n")
  nb_rounds = int(input(Fore.BLUE + 'Nombre de round(s) ? '))
  round_duration = int(input('Combien de minutes pour le round ? '))*60
  round_duration2 = int(input('Combien de secondes pour le round ? '))#*60
  break_duration = int(input('Combien de minutes pour la pause ? '))*60
  break_duration2 = int(input('Combien de secondes pour la pause ? '))#*60

  counter = 0
  print('\n' + Fore.WHITE)
  print(Fore.RED +'Round 1!!' + Fore.GREEN)
  for i in range(nb_rounds):
    counter += 1

    global t1
    t1 = round_duration + round_duration2
    while t1: 
      mins = t1 // 60 
      secs = t1 % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(Fore.RED + timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t1 -= 1
    print(f"Fin du round {counter}!!")
    print('🥊' * 50)
    if t1 == 0 :
        playsound.playsound('boxing_bell2.mp3') # annonce la fin du round

    t2 = break_duration + break_duration2
    while t2: 
      mins = t2 // 60 
      secs = t2 % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(Fore.GREEN +timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t2 -= 1 
      if counter == nb_rounds :
            t2 = 0
    if counter < nb_rounds : 
        print(f"Round {counter + 1 }!!")
        playsound.playsound('boxing_bell2.mp3') #annonce la reprise du round
    elif counter == nb_rounds : 
        print (Fore.YELLOW +'TIIIMMMEEEEE!!!!!')
        playsound.playsound('bell.mp3')         #annonce la fin des sparrings

timertest()