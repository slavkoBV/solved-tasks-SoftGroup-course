key = 13
f = open('test_file.txt', 'rb')
z = open('encode_file.txt', 'wb')
for symbol in f.read():
    z.write(bytes([symbol ^ key]))
f.close()
z.close()

f = open('encode_file.txt', 'rb')
z = open('decoded_file.txt', 'wb')
for symbol in f.read():
    z.write(bytes([symbol ^ key]))
f.close()
z.close()
