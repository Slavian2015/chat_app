from typing import Optional


class ServiceError(RuntimeError):
    message: str = ''

    def __init__(self, details: Optional[str] = None) -> None:
        msg = f'{self.message}: {details}' if details else self.message
        super().__init__(msg)