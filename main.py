#By: Brant Messenger

print(" --- Digital Root Calculator --- \n")

def checkValidInput(value):
  temp = value
  if temp.isdigit():
    if int(temp) > 9:
      return True
  return False

def shutDown(value):
  if value.lower() == "quit" or value.lower() == "q":
    print("\nCalculator shutting down...")
    quit()
  return False

def calculator():
  print("Please input a multiple-digit number: (q to quit)")
  value = input()

  shutDown(value)

  while(shutDown(value) == False):

    number = value
    while(checkValidInput(number) != True):
      if not number.isdigit():
        print("\nInput is invalid. Please input a multiple-digit number:")
      elif int(number) <= 9:
        print("\nInvalid digit. Please input a multiple-digit number:")
      value = input()
      number = value
      shutDown(value)
      checkValidInput(value)

    total = str(number)

    digital_root = total
    array_calculation = []

    while(len(total) != 1):
      current_value = 0
      for i in list(total):
        array_calculation.append(str(i))
        current_value += int(i)
      total = str(current_value)
      display_calculation = ""
      for n in range(len(array_calculation)):
        if n != len(array_calculation)-1:
          display_calculation += str(array_calculation[n]) + " + "
        else:
          display_calculation += str(array_calculation[n]) + " = " + str(total)
      print("\n" + display_calculation)
      array_calculation = []
      display_calculation = ""

    print("\nThe digital root of {} is {}.".format(digital_root,total))
    print("\nPlease input a multiple-digit number: (q to quit)")
    value = input()
  shutDown(value)

calculator()