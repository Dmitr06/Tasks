'''Напишите программу, которая определит количество различных комбинаций американских
 монет(1 цент, 5 центов, 10 центов, 25 и 50 центов), которые могут сложиться в определенную сумму.'''

'''In a writing program that determines the number of different combinations of American
  coins (1 cent, 5 cents, 10 cents, 25 and 50 cents) that may change in different situations.'''

def step_num (num_way, step_sum, stack_long):
    stack = stack_long[:]
    a = stack.pop()
    for i in range (0, step_sum // a + 1):
      current_sum = i * a
      if current_sum == step_sum or len(stack) == 1:
        num_way += 1
      elif len(stack) > 1:
        num_way = step_num(num_way, cash - current_sum, stack)
    return num_way

cash = int(input('Input num>0: '))   
print('There are ',step_num(0, cash, [1, 5, 10, 25, 50] ),' ways to produce ',cash,' cents change.')

           
                
        
        