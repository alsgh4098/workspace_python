from pkg.module_class import CalcClass
# 계산기 클래스 임폴트

import pkg.module_def as md
# 의미없는 함수 임폴트(클래스 아님)



# from pkg.module_class import CalcClass
# 모듈에서 클래스를 불러와서 사용.
Cal = CalcClass(3)
print("Cal.__dict__")
print(Cal.__dict__)
print(Cal.add(3,7))
print(Cal.div(5,8))
print(Cal.mul(9,3))

# import pkg.module_def as md
# 모듈에서 함수만 불러와서 사용
print(md.add(3,5))

# 클래스를 올려놓는(메모리에) 변수 = 인스턴스(객체)
# 인스턴스 = 클래스()의 의미는
# 인스턴스에 클래스의 기능을 부여하겠다.

ox100 = CalcClass(5)
print(ox100.add(1,1))
print("ox100.__dict__")
print(ox100.__dict__)
#인스턴스 메서드 : self를 파라미터로 갖고있는 메서드
#사용법은 생성자를 통해 주소를 호출한(객체를 할당한)
#인스턴스를 사용하면 된다.
ox200 = CalcClass(1)


# 파이썬 오버로딩
# 불러온 모듈 module_class에 가보면
# 파라미터값을 다르게 받는 add2라는 메소드가 두개있는걸 알수 있다.
# 두 개의 add2중 밑에걸로 위에 add2메소드가 덮어써지기 때문에
# 오버로딩이 안된다.
# 오버로딩과 비슷하게 사용하고 싶은 경우에는
# 메소드 하나를 만들고 받는 파라미터를 가변인자로 받게 한 다음
# 받은 가변인자의 타입이나 값에 따라서 다른 출력값을 리턴할 수 있게 만들어 주면 된다.
# 파이썬에서는 클래스의 변수명 메소드명을 딕셔너리로 변수또는 메소드명을 키값으로 구분한다.
# https://abipictures.tistory.com/713

Cal.add2(1,2,5)
print("*"*200)

# 메소드 오버라이딩
# 부모클래스에 있는 메소드를 그대로 사용하지 않고
# 자식클래스에서 같은 이름의 메소드를 생성해서 재정의해서 사용할 수가있다.
Cal.instanceMethod()
#메소드 오버라이딩해서 사용.
