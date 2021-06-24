class C:
    def LearnAndCode(self):
        print("Learning C programming")

class Cpp:
    def LearnAndCode(self):
        print("Learning C++ programming")
        
class Golang:
    def LearnAndCode(self):
        print("Learning Golang programming")
        
class Programmer:
    def Coding(self,language):
        language.LearnAndCode()

def main():

    cobj = C()
    cpobj = Cpp()
    gobj = Golang()

    obj = Programmer()
    obj.Coding(cobj)
    obj.Coding(cpobj)
    obj.Coding(gobj)

if __name__ == "__main__":
    main()