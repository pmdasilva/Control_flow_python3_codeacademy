def first_comp():
  first_statement = True  # A Terra gira em torno do Sol
  if first_statement:
      first_statement = "Yes"
  else:
      first_statement = "No"


def second_comp():
  second_statement = False  # A Lua NÃO é feita de queijo
  if second_statement:
      second_statement = "Yes"
  else:
      second_statement = "No"


def third_comp():
  third_statement = False  # Isso é opinião, não fato
  if third_statement:
      third_statement = "Yes"
  else:
      third_statement = "No"


first_comp()
second_comp()
third_comp()

### Fluxo de controel em python:

1 == 1     # Evaluates to True as the operands are the same 

1 != 1     # Evaluates to False as the operands are the same 

2 != 4     # Evaluates to True as the operands are different 

3 == 5     # Evaluates to False as the operands are different
 
'7' == 7   # Evaluates to False as the operands are different types


### Operadoes Relacionais II

> maior que


>= maior ou igual a


< menor que


<= menor ou igual a

### Operadores booleanos: &(AND), (||)OR, (!)NOT

and = ambas comdições precisam ser vedadeira para serem TRUE caso contrario FALSE:

or = Compara ambas condições e se alguma for verdadeira retura TRUE caso contrario FALSE

not = Inverte os valores de um valor booleano de TRUE para FALSE ou de FALSE para TRUE:

#### exemplos Operador AND:

(1 + 1 == 2) and (2 + 2 == 4)   # True

(1 > 9) and (5 != 6)            # False

(1 + 1 == 2) and (2 < 1)        # False

(0 == 10) and (1 + 1 == 1)      # False

#### Exemplos operador OR:

True or (3 + 4 == 7)    # True

(1 - 1 == 0) or False   # True

(2 < 0) or True         # True

(3 == 8) or (3 > 4)     # False

#### Exemplo operador NOT:

not 1 + 1 == 2  # False

not 7 < 0       # True

def compar_first(): 
  first_expression = 2 * 2 == 2 + 2
  if first_expression:
    first_expression = True
  else:
    first_expression = False
    

def compar_second(): 
  second_expression = 3 + 3 != 3 * 3 

  if second_expression:
    second_expression = True
  else:
    second_expression = False
    

def compar_third(): 
  third_expression = 3 * 3 == '9'

  if third_expression:
    third_expression = True
  else:
    third_expression = False
    

compar_first()
compar_second()
compar_third()

my_baby_bool = 'true'
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

# Working with statement AND
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa >= 2):
  print("You meet the requirements to graduate!")

# Working with statement OR
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >=2):
  print("You have met at least one of the requirements.")

# Working with statement NOT

statement_one = not (4 + 5 <= 9)
statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if credits <= 120:
  print("You do not have enough credits to graduate.")
elif gpa <= 2:
  print('"Your GPA is not high enough to graduate."')

#Working with statement NOT

statement_one = not False
statement_two = not True

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

grade = 86

if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
elif grade > 60:
    print("D")
else:
    print("F")