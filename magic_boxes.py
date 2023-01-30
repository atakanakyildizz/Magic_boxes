from pprint import pprint
ACTION_FILENAME = 'actions.txt'
#ACTION_FILENAME = 'actions-fail_bob.txt'
#ACTION_FILENAME = 'actions-fail_carl.txt'


def readfile(filename):
    try:
        with open(filename) as my_file:
            file = my_file.readlines()
        return file
    except OSError as error:
        print(f"Whops we have aproblem in here\n{error}")


def main():
    file = readfile(ACTION_FILENAME)
    error_counter = 0
    foo = dict()
    errorname = dict()

    for lines in file:
        elements = lines.split(" ")
        elements[-1] = elements[-1].replace("\n", '')
        if elements[1] == "gives":
            if elements[3] in foo:
                foo[elements[3]] = foo[elements[3]] + 1
            elif len(foo) < 42:
                foo[elements[3]] = 1
            else:
                error_counter = error_counter + 1
                errorname[elements[0]] = error_counter

        elif elements[1] == "takes":
            try:
                foo[elements[3]] = foo[elements[3]] - 1
                if foo[elements[3]] == 0:
                    foo.pop(elements[3])
            except KeyError:
                error_counter = error_counter + 1
                errorname[elements[0]] = error_counter

    pprint(foo)
    if len(errorname) != 0:
        print(f"Error -> name, number : {errorname}")


if __name__ == '__main__':
    main()
