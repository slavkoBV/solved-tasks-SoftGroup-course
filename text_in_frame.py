def text_in_frame(s):
    s += ' in the frame'
    res = s.split()
    str_width = max(len(i) for i in res)
    print('{0:*^{1}}'.format('*', str_width * 3))
    for line in res:
        print('{0:<{2}}{1:^{2}}{0:>{2}}'.format('*', line, str_width))
    print('{0:*^{1}}'.format('*', str_width * 3))


message = 'Доброго дня, Україно!'
text_in_frame(message)
