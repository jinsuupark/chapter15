class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age)+"살"+self.name+"입니다.")
        
    def __str__(self):
        return f"{self.age} 살 {self.name} 입니다"

kim =Human("김상형",29)
print(kim)
lee = Human("이승우",25)
print(lee)

print(kim.name)
kim.age = 21

kim.intro()
name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))

park = Human(name,age)
print(park)