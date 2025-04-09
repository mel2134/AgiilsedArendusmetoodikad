from Task import Task
def test_mark_done():
     task = Task("Testi ülesan")
     task.mark_done()
     assert task.status == "done"
     