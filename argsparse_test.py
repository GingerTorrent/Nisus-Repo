
from argparse import ArgumentParser
from argparse import ArgumentTypeError

def check_weight(value):
    weight = int(value)
    if weight > 200 or weight <= 20:
        msg = "Very strange weight value: {0}".format(value)
        raise ArgumentTypeError(msg)
    return value

def main():
    parser = ArgumentParser()
    group_required = parser.add_argument_group('required arguments')
    group_required.add_argument('--name', required=True, type=str, choices=['Robert', 'Marta'], help="User's name")
    group_required.add_argument('--surname', required=True, type=str, help="User's surname")
    group_required.add_argument('--age', required=True, type=int, help="User's age")
    group_required.add_argument('--weight', required=True, type=check_weight, help="User's weight")
    group_optional = parser.add_argument_group('optional arguments')
    group_optional.add_argument('--petname', required=False, type=str, help="User's pet name")
    used_args = vars(parser.parse_args())

    user_name = used_args["name"]
    user_surname = used_args["surname"]
    user_age = used_args["age"]
    user_weight = used_args["weight"]
    user_petname = used_args["petname"]

    print(f"My name is {user_name} {user_surname}. I am {user_age} years old and I weigh {user_weight} kilograms.")
    if user_petname is None:
        print("I hate animals.")
    else:
        print(f"My pet's name is {user_petname}.") 

if __name__ == '__main__':
    main()


