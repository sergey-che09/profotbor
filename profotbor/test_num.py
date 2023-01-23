telList = ['8-902-657-09-50;',
           '8(8442) 94-39-54;',
           '9272555572;',
           '(884463) 2-64-71;',
           '8> 903 371 40 73']

newTelList = [ ''.join(filter(str.isdigit, tel)) for tel in telList ]

[print('+7-{}-{}-{}-{}'.format(tel[1:4], tel[4:7], tel[7:9], tel[9:11])) for tel in newTelList]

[print('+7-{}-{}-{}-{}'.format(tel[0:3], tel[3:6], tel[6:8], tel[8:10])) for tel in newTelList]

print(newTelList)