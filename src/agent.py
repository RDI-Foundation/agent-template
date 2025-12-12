from a2a.server.tasks import TaskUpdater
from messenger import Messenger


class Agent:
    def __init__(self):
        self._messenger = Messenger()
        # initialize other state here

    async def run(self, input_text: str, updater: TaskUpdater) -> None:
        # implement agent logic here
        raise NotImplementedError("Agent not implemented.")
