class Singlet(object):

    instance = None
    def __new__(cls, val):
        if Singlet.instance is None:
            Singlet.instance = object.__new__(cls)
        Singlet.instance.val = val
        return Singlet.instance
