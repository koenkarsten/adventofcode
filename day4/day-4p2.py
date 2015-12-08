import hashlib

secret_key = 'iwrupvqb'
counter = 0

while(True):
    counter += 1
    input = '{}{}'.format(secret_key, counter)

    m = hashlib.md5()
    m.update(input)
    result = m.hexdigest()[:6]
    if result == '000000':
        print('{} == {}'.format(counter, result))
        break

