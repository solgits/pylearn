class MyClass:
    data = 'python'
    def __init__(self) :
        self._data = 'korea'
    
    def instance_method(self) :
        print('instance' , self._data)

    @classmethod
    def class_method(cls) :
        print('class' , cls.data)

    @staticmethod
    def static_method() :
        print('static', MyClass.data)


s = MyClass()
s.instance_method()
s.class_method()
MyClass.class_method()
MyClass.static_method()


class My: 
    def __init__(self) :
        self._name = "korea"
        print('My')
    def get_name(self) :
        print('self._name' , self._name)

class SubMy(My) :
    def __init__(self):
        super().__init__()
        print('SubMy')

    def sub_print(self) : 
        print('sub_print' , self.get_name())
        return self._name


s = SubMy();
print('*' * 30)
print(s._name)
print('메소드', s.get_name())
print('sub check' , s.sub_print())
print('-' * 30)
s.get_name()
s.sub_print()
