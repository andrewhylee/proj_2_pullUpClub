from pullupclub.models import Student, PullUpSession

def run():
    for i in range(5):
        stu = Student()
        stu.name = "TestStudent" + str(i)
        stu.nickname = "wetwater%d" % i
        stu.slug = stu.name
        stu.save()

        pus = PullUpSession(student=stu)
        pus.count = i
        pus.save()