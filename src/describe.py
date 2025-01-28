#!/usr/bin/env python3

import json 
import sys
from pprint import pprint
from core.utils.parser import execute_parsing
from core.description.operation import execute_describe


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: ./describe.py DATA_SET_NAME")
        sys.exit(1)
    execute_describe(sys.argv[1])