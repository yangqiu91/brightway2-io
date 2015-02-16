class InvalidPackage(Exception):
    """bw2package data doesn't validate"""
    pass


class UnsafeData(Exception):
    """bw2package data comes from a class that isn't recognized by Brightway2"""
    pass


class UnsupportedExchange(Exception):
    """This exchange uncertainty type can't be rescaled automatically"""
    pass
