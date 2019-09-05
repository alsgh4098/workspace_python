class car() :
    car_price = 14000
    def add(self):
        self.car_price = 0
        print(self.car_price)
    def print_main_name(self):
        print(__name__)

# 메인함수를 지정하는 방법
# 이 파일은 클래스파일로 사용할것이기때문에
# 클래스문 외에 다른 문장들은 이 클래스를 임폴트할 다른 파일에서 실행되면 안된다.
# if __name__ == "__main__" : 문으로 해결해 줄 수있다.




# if __name__ == "__main__" :
#     print("sasdasd")
#
#
# print("asdasdasdasdasd")