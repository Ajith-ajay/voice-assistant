from handle_operation import handle_operations
from utils import takeCommand,wishMe,username
import os

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
    
    while True:
        
        query = takeCommand().lower()
        if query == "None":
            continue
        """
        All the commands said by user will be 
        stored here in 'query' and will be
        converted to lower case for easily 
        recognition of command 
        """
        handle_operations(query)