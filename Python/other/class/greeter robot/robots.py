class Roby:

    def __init__(self,name,master):
        self.name = name
        self.master = master
        self.greet()
        print('Thank you to create me.')

    def greet(self):
        print(\
'''
Hello, my name is {0}.
My master is {1}.
'''.\
format(self.name,self.master))

class Robal(Roby):
    def __init__(self,name,master,age=''):
        self.name = name
        self.master = master
        self.age = age
        self.greet()
        print('Thank you to create me.\n')

    def greet(self):
        print(\
'''
Hello, my name is {0}.
My master is {1}.'''.\
format(self.name,self.master))
        if self.age != '':
            print(\
'My master\'s age is {}'.format(self.age))
        print()


if __name__ == '__main__':
    name = input('enter name >>> ')
    masname = input('enter your name >>> ')
    masage = input('enter your age >> ')
    print('\nenter Q to quit')
    Rob = Robal(name,masname,masage)
    while 1:
        ans = input('>>> ')
        if ans == 'Q':
            break
        elif ans == 'greet':
            Rob.greet()
        else:
            print(\
'''
manu: 'greet', 'Q'
''')
