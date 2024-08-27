import json
import random
import sys
import textwrap

def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
    
def print_wrapped_text(text, width=70):
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)
    
def get_name(data):
    return data["name"]

def get_why(data):
    return data["why"]

def get_what(data):
    return data["what"]

def get_fact(data):
    return random.choice(data["fact"])

def main():
    if len(sys.argv) != 2:
        print("Usage: python index.py /option")
        sys.exit(1)

    option = sys.argv[1].strip('/')

    data = read_json('data.json')

    option_funcs = {
        "name": get_name,
        "why": get_why,
        "what": get_what,
        "fact": get_fact
    }

    if option in option_funcs:
        res = option_funcs[option](data)
        print_wrapped_text(res, width=100)
    else:
        print(f"Option '{option}' not found.")

if __name__ == "__main__":
    main()