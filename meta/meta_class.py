class SingletonType(type):
    """
    Meta-classes allow you to deeply modify the behaviour of Python classes.

    """

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance
