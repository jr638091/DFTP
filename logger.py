

class Logger:
    """
        Los modos para el logger se definen como 3 bit:\n
        El primer es para guardar el nombre de la funcion que se invoca\n
        El segundo es para guardar los parametros que se le pasan a la funcion\n
        El tercero es para guardar el __str__ del resultado de la funcion
    """

    def __init__(self, mode, *files):
        self.mode = mode
        self.files = files

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            to_log = []

            if self.mode[0] == '1':
                to_log.append("\tFunction Name -->>  " + func.__code__.co_name)

            if self.mode[1] == '1':
                to_log.append("\tArguments of -->>  " + str(args) + "   KWARGS -->>  " + str(kwargs))

            r = func(*args, **kwargs)

            if self.mode[2] == '1':
                to_log.append("\tResult of -->>  " + str(r))

            if len(to_log) > 0:
                for i in self.files:
                    file = open(i, "a")
                    file.write('\n')
                    file.write(str(func) + " log begin")
                    for j in to_log:
                        file.write("\n")
                        file.write(j)
                    file.write('\n')
                    file.write(str(func) + " log end")
                    file.close()

            return r
        return wrapper
