from mvc.controller import Controller


control = Controller()
while control.choice not in ('Q', 'q'):
    control.manager()
else:
    print('Bye')
