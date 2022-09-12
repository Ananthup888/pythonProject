#list all mobiles

# add a mobile - post - to create

# detail of a specific mobile  - get - to retrive

# update a mobile - put - to update

# delete a mobile  - delete - to delete

class User:

    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
admin =User("Rahul",35,"Admin")
faculity=User("Ajith",25,"Fcaulity")
student=User("Sabir",23,"Student")

class Addcourse(object):
    def __init__(self,user,course_name):
        self.user=user
        self.course_name=course_name
    def print_details(self):
        print(self.course_name)+str(self.user))

    def __str
        return self.course_name
