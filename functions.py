# this is a format of defining a function

#static function
def welcome_message_static():
    print("welcome student")
    print('welcome to microdegree family')

# you should call the function to execute it, or else it wont be executed
welcome_message_static()



# you can also define a function with a parameter as shown below (you can add as many parameters as you like)
def welcome_message_dynamic(name, branch):
    print('welcome '+ name)
    print('welcome to '+ branch + ' microdegree family')

welcome_message_dynamic('kishore','mangalore')

def welcome_message_dynamic_with_input(name, branch):
    print('welcome '+ name)
    print('welcome to '+ branch + ' microdegree family')
welcome_message_dynamic_with_input(input('please type your name: '), input('please type your desirred branch: '))



# function with return statement
def car_make(car_name):
    