import os

header = """
   _ \\ _ _|   _ \\   ____|   _ \\      __  /  ____|   _ \\    _ \\  
  |   |  |   |   |  __|    |   |        /   __|    |   |  |   | 
  ___/   |   ___/   |      __ <        /    |      __ <   |   | 
 _|    ___| _|     _____| _| \\_\\     ____| _____| _| \\_\\ \\___/  

"""

options = """Options:
    1. Save requirements
    2. Install requirements
    3. Exit
"""


def save_requirements():
    """Save requirements to requirements.txt"""
    os.system('pip freeze > requirements.txt')


def install_requirements():
    """Install requirements from requirements.txt"""
    os.system('pip install -r requirements.txt')


def dialog():
    """Dialog to choose what to do"""
    print(f'''{header}{options}''')
    choice = input('Enter your choice: ')
    if choice == '1':
        save_requirements()
    elif choice == '2':
        install_requirements()
    elif choice == '3':
        exit()
    else:
        print('Wrong choice')
        dialog()


if __name__ == '__main__':
    dialog()
