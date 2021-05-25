# 회원가입 로그인 마이페이지 수정 회원탈퇴 id 본명 메일 ??
class Member(object):
    def __init__(self, id, name, mail):
        self.id = id
        self.name = name
        self.mail = mail

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            m = input('1. 회원가입\n2. 로그인\n3. 마이페이지\n4. 정보 수정\n5. 회원탈퇴')
            if m == '1':
                pass
            elif m == '2':
                pass
            elif m == '3':
                pass
            elif m == '4':
                pass
            elif m == '5':
                pass
            else:
                continue

Member.main()
