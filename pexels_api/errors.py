class BasePexelError(Exception):
    pass


class EndpointNotExists(BasePexelError):

    def __init__(self, end_point, _enum) -> None:
        options = _enum.__members__.keys()
        self.message = f'Endpoint "{end_point}" not exists. Valid endpoints: {", ".join(options)}'
        super().__init__(self.message)


class ParamNotExists(BasePexelError):

    def __init__(self, name, _enum, param) -> None:
        options = _enum.__members__.keys()
        self.message = f'{param} not exists in {name}. Valid params: {", ".join(options)}'
        super().__init__(self.message)
