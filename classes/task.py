class Task:
    valid_status = ["pending", "in progress", "completed"]
    valid_priority = ["low", "mid", "high"]

    def __init__(
        self,
        title: str,
        desc: str = "N/A",
        status: str = "pending",
        priority: str = "mid",
    ) -> None:
        if priority not in Task.valid_priority:
            raise ValueError("The 'priority' must be from 'low', 'mid' or 'high'")
        self.title = title.title()
        self.desc = desc
        self.status = status
        self.priority = priority

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError("'title' must not be empty")
        self._title = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in Task.valid_status:
            raise ValueError(
                "The 'status' must be from 'pending', 'in progress' or 'completed'"
            )
        self._status = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value: str):
        if value not in Task.valid_priority:
            raise ValueError("The 'priority' must be from 'low', 'mid' or 'high'")
        self._priority = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value: str):
        if value:
            self._desc = value
        else:
            raise ValueError("'desc' must not be empty")
