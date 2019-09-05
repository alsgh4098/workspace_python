# 08module_class.py
# OOP ( Object Oriented Programming)
# 클래스, 변수 : 값 / 메서드(함수) : 동작
#
# from pkg.module_parent import ParentClass
# # 부모라는 이름의 클래스 임폴트

class CalcClass(ParentClass) :
    default_value = 0
    def __init__(self, prm_grade) : # 파이썬에서 생성자(constructor)는 이렇게 생겼다.
                         # 자바에서는 def CalcClass() 같은 형태로 클래스선언 안에 넣어준다.
                         # 생성자를 사용하는 이유는 인스턴스생성시 각자 영역의 값을 초기화 시켜주기 위해서 사용한다.
        super(CalcClass, self).__init__()
        # ParentClass.__init_()과 같은 의미
        # 상속받은 부모클래스의 생성자를 실행해달라.
        # 부모 클래스에 접근할 때는 super()를 사용한다.

        print("CalcClass가 생성되었습니다.")
        self.grade = prm_grade
    def add2(self, a,b):
        list = []
        list.append(a)
        print(list)
    def add2(self, a,b,c):
        list = []
        list.append(a)
        print(list)

    def add(self, a, b) :
        return (a + b)

    def div(self,a, b) :
        return (a / b)

    def mul(self,a, b) :
        return (a * b)

    # 메소드 오버라이딩
    # 부모클래스에 있는 메소드를 그대로 사용하지 않고
    # 자식클래스에서 같은 이름의 메소드를 생성해서 재정의해서 사용할 수가있다.
    def instanceMethod(self) :
        print("CalcClass instanceMethod")


print(dir())

help(super)
