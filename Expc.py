def get_valid_float(prompt: str, error_message: str, positive_only: bool =True) -> float:
  while True:
    try:
      value = float(input(prompt))
      if positive_only and value <=0:
        print(error_message)
      else: return value
    except ValueError:
      print('Invalid Input. Please Enter a Number.')

def positive_number_of_people(promt: str, error_message: str) -> int:
   while True:
    try:
       positive_people = int(input(promt))
       if positive_people <1:
          print(error_message)
       else: return positive_people
    except ValueError:
       print('Number of people must be positive.')

def get_splitting_choice()-> str:
   while True:
      splitting_choice = input('Would you like to have an even or uneven split? (even/uneven): ').strip().lower()
      if splitting_choice in ['even', 'uneven']:
       return splitting_choice
      else:
       print('Invalid input')

def get_custom_split(number_of_people : int, total_expense : float)-> list:
   custom_split = []
   for i in range(number_of_people):
     while True:
        try:
           amount = float(input(f'Please enter the amount for person {i+1} : $ '))
           if amount<1:
            print('Please input a positive value.')
           else: 
            custom_split.append(amount)
           break
        except ValueError:
         print('Invalid value. Please enter a valid number.')
   if round(sum(custom_split), 2) != round(total_expense, 2):
    raise ValueError(f'The amounts do not add up to the total expense of {total_expense:,.2f}. Please try again')
   return custom_split
   
def custom_split_percentage(number_of_people : int, total_expense : float)-> list:
   split_percentage = []
   for i in range(number_of_people):
      while True:
         try:
            percentage = float(input(f'Please enter the percentage per person(%) {i+1} : '))
            if percentage <0:
               print('Percentage must be positive.')
            else:
               split_percentage.append(percentage)
               break
         except ValueError:
            print('Invalid percentage. Please enter a valid percentage.')
   if round(sum(split_percentage), 2) !=100:
    raise ValueError(f'The percentage do not add up to 100. Please try again.')
   split_amounts = [(percentage / 100) *  total_expense for percentage in split_percentage]
   return split_amounts

def calculate_expenses(total_expense : float, number_of_people : int, splitting_choice : str, currency : str):
    if splitting_choice == 'even':
     each_person_share : float = total_expense / number_of_people
     print(f'Total expense: {currency}{total_expense:,.2f}')
     print(f'Number of people: {number_of_people}')
     print(f'Each person should pay: {currency}{each_person_share:,.2f}')
    elif splitting_choice == 'uneven':
     splitting_type = input('Would you like to split by amounts or percentage? (amounts/percentage): ').strip().lower()
     if splitting_type == 'amounts':
       custom_split = get_custom_split(number_of_people, total_expense)
       print(f'Total expense: {currency}{total_expense:,.2f}')
       for i, amount in enumerate(custom_split, 1):
          person_percentage = (amount/ total_expense) *  100
          print(f'Person {i} should pay: {currency}{amount:,.2f} ({person_percentage:.2f}%)')
     elif splitting_type == 'percentage':
       split_percentage = custom_split_percentage(number_of_people, total_expense)
       print(f'Total expense: {currency}{total_expense:,.2f}')
       for i, percentage in enumerate(split_percentage, 1):   
          person_amount = percentage
          print(f'Person {i} should pay: {currency}{person_amount:,.2f}')

def main() -> None:
    try:
        total_expense = get_valid_float('Please enter your total expense: $', 'Total expense must be a positive number.')
        number_of_people = positive_number_of_people('Please enter the number of people: ', 'Number of people must be over one and a number.')
        splitting_choice = get_splitting_choice()
        calculate_expenses(total_expense, number_of_people, splitting_choice, currency = '$')
    except ValueError as e:
        print(f'Error: {e}')
        return

if __name__ == '__main__' :
  main()
    
    


    