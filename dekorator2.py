def dekorator(obj):
    def inna_funkcja():
        obj()
        print("world")
    return inna_funkcja

@dekorator
def funkcja():
    print("hello")

funkcja()