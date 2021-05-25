class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = int(input(f'0.Exit\n1.Input\n2.Print URL\n'))
            if menu == 0:
                break
            elif menu == 1:
                wiki = Wikipedia(input(f'Input URL\n'))
            elif menu == 2:
                print(f'URL = {wiki}\n')
            else:
                print('wrong number')
                continue

Wikipedia.main()
