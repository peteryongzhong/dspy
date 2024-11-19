from datetime import datetime

class Teleprompter:
    def __init__(self):
        self.snapshots = []

    def snapshot(self, student, version: int, complete_time: datetime):
        self.snapshots.append((student, version, complete_time))

    def get_snapshots(self):
        return self.snapshots
 