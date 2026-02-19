class PQNode:
    
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return self.priority + ": " + self.value