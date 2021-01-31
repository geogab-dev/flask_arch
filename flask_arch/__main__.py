from flask_arch.gen_arch import generate_flask_arch
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Template generator for Flask projects.')

    parser.add_argument('command', choices=['init'],  help='Generate the template of choice.')
     
    #For future use
    #parser.add_argument('-t','--tags', nargs='*', metavar='tag', help='Add optional tags to your template.')
    args = parser.parse_args()

    return args

def main():
    args = get_args()

    function_table = {
        'init': generate_flask_arch,
    }

    function_table[args.command]()

main()
