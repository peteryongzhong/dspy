from datetime import datetime

class Teleprompter:
    def __init__(self):
        self.snapshots = []

    def snapshot(self, student, version: int, timestamp: datetime):
        self.snapshots.append((student, version, timestamp))

    def get_snapshots(self):
        return self.snapshots
