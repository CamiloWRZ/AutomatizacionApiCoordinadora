from screenpy import Actor
from screenpy_requests.actions import SendPOSTRequest

class SendRequest:

    @staticmethod
    def using(url: str, json: dict, type: str) -> "SendRequest":
        return SendRequest(url, json, type)
    
    def perform_as(self, the_actor: Actor) -> None:

        if self.type == 'post':
            the_actor.attempts_to(
                SendPOSTRequest.to(self.url).with_(
                    json=self.json
                )
            )
    
    def __init__(self, url: str, json: dict, type: str) -> None:
        self.url = url
        self.json = json
        self.type = type
