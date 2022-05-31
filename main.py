#генератор безопасных паролей
#мини-проект из курса степика для нубов
def generate_password(leng, alph):
  result = ''
  for i in range(leng):
#добавляем символ со случайно сгенерированным индексом
    result += alph[random.randint(0, 10000) % len(alph)]
  return result

def yes_no_valid(yn):
  return yn == 'y' or yn == 'n'
 
def sugg_y_n():
  yn = input()
  while not yes_no_valid(yn):
    print("Please, enter 'y' for YES or 'n' for NO:")
    yn = input()
  if yn == 'y':
    return True
  elif yn == 'n':
    return False
  
def is_valid(ans):
  return ans.isdigit() and int(ans) > 0
  
def sugg():
  answer = input()
  while not is_valid(answer):
    print("Incorrect value! Please, enter integer more than 0:")
    answer = input()
  else:
    ans = int(answer)
  return ans
import random
#списки символов
dig = '1234567890'
up_l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lo_l = 'abcdefghijklmnopqrstuvwxyz'
punk = '!#$%&*+-=?@^_'
chars = ''
#приглашение
print("Hi! How much passwords you are need?")
n = sugg()
#собираем пожелания по паролям
print("Enter the length for passwords:")
leng = sugg()
print("Is digits in password? (y/n)")
yn1 = sugg_y_n()
print("Is uppercase letters in password?")
yn2 = sugg_y_n()
print("Is lowercase letters in password?")
yn3 = sugg_y_n()
print("Is !#$%&*+-=?@^_ in password?")
yn4 = sugg_y_n()
print("Will we add il1Lo0O?")
yn5 = sugg_y_n()
  #обработка ответов для составления алфавита
if yn1:
  chars += dig
if yn2:
  chars += up_l
if yn3:
  chars += lo_l
if yn4:
  chars += punk
if not yn5:
  for c in 'il1Lo0O':
        chars = chars.replace(c, '')
#если вдруг пользователю никакие символы не нужны, прощаемся
if not yn1 and not yn2 and not yn3 and not yn4:
  print("The Alphabet is empty! Restart the programm!")
else:
  for i in range(n):
    print(generate_password(leng, chars))
    