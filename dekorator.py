def funkcja():
    print('nowa funkcja')


def dekorator(obj):
    return funkcja


@dekorator
def funkcja2():
    print('testing')


funkcja2()