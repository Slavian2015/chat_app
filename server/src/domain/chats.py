import datetime


class Message:
    def __init__(self, client_id: str | int = 'server', message: str | None = None) -> None:
        self.sender = client_id
        self.message = message
        self.datetime = datetime.datetime.now()
        self.time = self.datetime.strftime("%H:%M")
