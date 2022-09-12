class Parent:
    def properties(self):
        return {"bike": "passion pro","car": "swift"}

class Child(Parent):
    def properties(self):
        self.context=super().properties()
        self.context["cycle"]="hero"
        return self.context
child=Child()
print(child.properties())









class Editor:
    def functionalities(self):
        return ['create new file',"execute"]
class Pycharm(Editor):
    def functionalities(self):
        specs=super().functionalities()
        specs.append("debug")
        return specs


class Vscode(Editor):
    def functionalities(self):
        specs=super().functionalities()
        specs.append("extensions")
        specs.append("vcs")
        return specs
pyc=Pycharm()
print(pyc.functionalities())
vsc=Vscode()
print(vsc.functionalities())

