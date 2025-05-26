class FixedRelationError(TypeError):
    """Исключение, запрещающее переопрделить to у FK."""

    def __init__(self, field_class):
        message = f'Параметр `to` не может быть переопределён для {field_class.__name__}'
        super().__init__(message)
