import pickle

class UserInfo:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"<UserInfo {self.name} {self.phone}>"

    def __repr__(self):  #  축약형 표현
        # 유저인포를 담고있는 리스트,튜플 (콜렉션)을 출력하였을떄 출력됨
        return f"<UserInfo {self.name}> "

class AddressBook:
    def __init__(self):
        self.book=[]

    def add(self, name, email, phone):
        ui = UserInfo(name,email,phone)
        self.book.append(ui)

    def find_by_name(self,name):
        for ui in self.book:
            if ui.name == name:
                return ui

    # def search_by_name(self,name):
    #     temp_list=[]
    #     for ui in self.book:
    #         if ui.name.find(name) > -1:
    #             temp_list.append(ui)
    #
    #     return temp_list

    def search_by_name(self,name):
        return [ui for ui in self.book if ui.name.find(name) > -1]

    def update(self, name, email, phone):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name} 은/는 목록에 업습니다")
            return
        ui.email = email
        ui.phone = phone

    def remove(self,name):
        ui = self.find_by_name(name)
        if not ui :
            print(f"{name} 은/는 목록에 업습니다")
            return
        
        #값으로 리스트 항목 삭제하기
        self.book.remove(ui)

    def save(self,fpath):

        try:
            with open(fpath,'wb') as file:
                pickle.dump(self.book,file)

        except Exception as e:
            print(f"{fpath} 파일 쓰기에 실패하였습니다.")
            print(e)

    def load(self,fpath):
        try:
            with open(fpath,'rb') as file:
                self.book = pickle.load(file)

        except Exception as e:
            print(f"{fpath} 파일 읽기에 실패하였습니다.")
            print(e)
    def sort_by_name(self, reverse=False):
        self.book.sort(key=lambda u: u.name,reverse=reverse)











    def __str__(self):
        return f"{self.book}"

def main():
    l = [
        UserInfo("홍길동","hong@naver.com","010-1111-2222"),
        UserInfo("고길동","Go@naver.com","010-3333-4444"),
        UserInfo("둘리","222@naver.com","010-5555-6666")
    ]

    ab = AddressBook()
    ab.add("홍길동","hong@naver.com","010-1111-2222")
    ab.add("고길동","Go@naver.com","010-3333-4444")
    ab.add("둘리","222@naver.com","010-5555-6666")

    print(ab.book)

    ui1 = ab.find_by_name("고길동")
    ui2 = ab.find_by_name("호이")
    print(ui1)
    print(ui2)
    ab.update("고길동","go@daum.net","010-7777-8888")

    ui1 = ab.find_by_name("고길동")
    print(ui1)
    ab.update("호이","go@daum.net","010-7777-8888")
    # ab.remove("고길동")
    print(ab)
    li = ab.search_by_name("길동")
    print(li)
    ab.save("ab1.dat",)
    new_ab = AddressBook()
    new_ab.load("ab1.dat")
    print()
    print(new_ab)



    file_name = "book1.dat"
    addr_book = AddressBook()

    # addr_book.add('홍길동','hong@naver.com','010-1111-2222')
    # addr_book.add('박진수','go@daum.net','010-544-4444')
    # print(addr_book)
    # addr_book.save(file_name)

    addr_book2 = AddressBook()
    print(addr_book2)
    addr_book2.load(file_name)

    print(addr_book2)


    print(ab)
    ab.sort_by_name()
    print(ab)

main()