def get_todos(filepath="/Users/salvatoreswain/PycharmProjects/Todoapp/files/todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="/Users/salvatoreswain/PycharmProjects/Todoapp/files/todos.txt"):
    """ Write the to-do items list in the text files."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

