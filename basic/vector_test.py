class Vectortest(object):
    # 필드 프로퍼티 -> self로 호출
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': '30세'}

    def ls_create(self):
        # Create: ls 에 '100'을 추가
        self.ls.append('100')
    def ls_read(self):
        # Read: ls 의 목록을 출력
        print(self.ls)
    def ls_update(self):
        # Update: ls와 tinyls 의 결합
        self.ls.extend(self.tinyls)
    def ls_delete(self):
        # Delete: ls 에서 786을 제거
        del self.ls[1]
    def tp_create(self):
        # Create: tp 에 '100'을 추가
        self.tp = self.tp + (100,)
        print(self.tp)
    def tp_read(self):
        # Read: tp 의 목록을 출력
        print(self.tp)
    def tp_merge(self):
        # Update: tp와 tinytp 의 결합
        print(self.tp + self.tinytp)
    def tp_delete(self):
        # Delete: tp 에서 786을 제거
        print('impossible')
    def dt_create(self):
        # Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가
        self.dt['tom'] = '100'
    def dt_read(self):
        # Read: dt 의 목록을 출력
        print(self.dt)
    def dt_update(self):
        # Update: dt와 tinydt 의 결합
        self.dt.update(self.tinydt)
    def dt_delete(self):
        # Delete: dt 에서 'abcd' 제거
        del self.dt['abcd']
        print(self.dt)

    @staticmethod
    def main():
        v = Vectortest()
        while 1:
            m = input('0.exit\n'
                      'List: \n1. create\n2. print\n3. update\n4. delete\n'
                      'Tuple: \n5. create\n6. print\n7. update\n8. delete\n'
                      'Dictionary: \n9. create\n10. print\n11. update\n12. delete\n')
            if m == '0':
                break
            elif m == '1':
                print(v.ls_create())
            elif m == '2':
                v.ls_read()
            elif m == '3':
                v.ls_update()
            elif m == '4':
                v.ls_delete()
            elif m == '5':
                v.tp_create()
            elif m == '6':
                v.tp_read()
            elif m == '7':
                v.tp_merge()
            elif m == '8':
                v.tp_delete()
            elif m == '9':
                v.dt_create()
            elif m == '10':
                v.dt_read()
            elif m == '11':
                v.dt_update()
            elif m == '12':
                v.dt_delete()
            else:
                print('wrong number')
                continue

Vectortest.main()