file = input('File name: ').strip().lower()

if file.endswith('gif') or file.endswith('jpg') or file.endswith('jpeg') or file.endswith('png'):
    filename, ext = file.rsplit('.',1)
    if ext == 'jpg':
        print('image/jpeg')
    else:
        print(f'image/{ext}')
elif file.endswith('pdf') or file.endswith('zip'):
    filename, ext = file.rsplit('.',1)
    print(f'application/{ext}')
elif file.endswith('txt'):
    print('text/plain')
else:
    print('application/octet-stream')
