import json 
from pprint import pprint
from core.utils.parser import execute_parsing
from core.description.execution import  execute_describe

def main():
    values = execute_parsing()
    execute_describe(values)

if __name__ == "__main__":
    main()