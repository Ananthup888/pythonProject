from blogapplication2.models import users,blogs

session={}
class Login:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=[user for user in users if user.get("username")==username and user.get("password")==password]
        if user:
            session["user"]=user.pop()
            print("login success")
        else:
            print("Invalid credentilas")

def logout():
    if "user"in session:
        session.pop("user")
    else:
        print("operation not allowed")



class Postlist:
    def get(self,*args,**kwargs):
        if "user" in session:
            return blogs
        else:
            return "You must login"
    def post(self,*args,**kwargs):
            newpost=kwargs.get("data")
            if "user" in session:
                id=session["user"]["id"]
                newpost["userId"]=id
                blogs.append(newpost)
                print("print post has been created")
            else:
                print("you must login")
 
auth=Login()
auth.post(username="nikil",password="Password@123")
# print("session before logout")
# print(session)
# logout()
# print("session after logout")
# print(session)
posts=Postlist()
print(posts.get())
newpost= {"postId": 9, "title": "goomorning", "content": "content"}
posts.post(data=newpost)