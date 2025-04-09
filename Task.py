class Task:
    def __init__(self,title,status = "To-do"):
        self.status = status
        self.title = title
    def mark_done(self):
        self.status = "done"