# 회원가입 로그인 마이페이지 수정 회원탈퇴 id 본명 메일 ??
class Member(object):
    id = ''
    pw = ''
    mail = ''
    name = ''

    def __str__(self):
        return self.url

    def join(self):
        pass

    def login(self):
        pass

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    @staticmethod
    def main():
        member = Member()
        while 1:
            m = input('1. 회원가입\n2. 로그인\n3. 마이페이지\n4. 정보 수정\n5. 회원탈퇴')
            if m == '1':
                id = ''
                pw = ''
                mail = ''
                name = ''
                member.join()
            elif m == '2':
                id = ''
                pw = ''
                member.login()
            elif m == '3':
                id = ''
                member.mypage()
            elif m == '4':
                id = ''
                pw = ''
                mail = ''
                name = ''
                member.update()
            elif m == '5':
                id = ''
                pw = ''
                mail = ''
                name = ''
                member.remove()
            else:
                continue

Member.main()
