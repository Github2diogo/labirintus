import pyqrcode
from PIL import Image

links = [
    ['p01', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5544323,-46.7335794/@-23.5555837,-46.736493,17z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p02', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5545155,-46.7337982/@-23.5565832,-46.7357722,742m/data=!3m1!1e3!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p07', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5561517,-46.7342338/@-23.5588162,-46.7350565,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p11', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5560493,-46.734741/@-23.5564283,-46.7356274,417m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p12', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas+-+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5563595,-46.7344886/@-23.5569176,-46.7365861,18z/data=!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p15', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5554921,-46.7349495/@-23.5585487,-46.7352429,17z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p19', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5550687,-46.7353877/@-23.555701,-46.7360732,331m/data=!3m1!1e3!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p20', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.55484,-46.7349755/@-23.5581921,-46.737604,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p31', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5565414,-46.735914/@-23.5564726,-46.7375719,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p36', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5564144,-46.7366186/@-23.5586899,-46.7358166,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p37', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5564144,-46.7366186/@-23.5586899,-46.7358166,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p39', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5568837,-46.7368973/@-23.5571172,-46.7384363,417m/data=!3m1!1e3!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p46', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5566737,-46.7380651/@-23.5565888,-46.7373517,18z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347515!2d-23.5568168!1m0!3e0'],
    ['p48', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5573294,-46.7382472/@-23.55868,-46.7388268,16z/data=!3m1!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347515!2d-23.5568168!1m0!3e0'],
    ['p50', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5576312,-46.7379747/@-23.5569057,-46.7374868,417m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p53', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5575263,-46.7388136/@-23.5570542,-46.73935,833m/data=!3m1!1e3!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p54', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5583535,-46.7386303/@-23.5586898,-46.7392567,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p55', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5577738,-46.7395187/@-23.5570542,-46.73935,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p56', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5585727,-46.7397616/@-23.5573909,-46.739448,833m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p59', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5580927,-46.7409367/@-23.5586898,-46.7402364,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p62', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5576249,-46.7409148/@-23.5586898,-46.7402333,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ['p65', 'https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5582795,-46.7416122/@-23.5586898,-46.7406517,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
    ]

# pra quando não precisamos gerar todos os QR codes
# links = [
#     ['p54','https://www.google.com.br/maps/dir/IPT+-+Instituto+de+Pesquisas+Tecnol%C3%B3gicas,+Av.+Prof.+Almeida+Prado,+532+-+Butant%C3%A3,+S%C3%A3o+Paulo+-+SP,+05508-901/-23.5583535,-46.7386303/@-23.5586898,-46.7392567,1667m/data=!3m2!1e3!4b1!4m9!4m8!1m5!1m1!1s0x94ce56111f23979f:0x4efc1ff99667559c!2m2!1d-46.7347373!2d-23.5568084!1m0!3e0'],
# ]

for link in links:
    qrobj = pyqrcode.create(link[1])


    with open('' + link[0] + '.png', 'wb') as f:
        qrobj.png(f, scale=3)

    # Abre a imagem .png a ser inserida como logo no qr code criado
    img = Image.open('' + link[0] + '.png')
    img = img.convert("RGBA")
    width, height = img.size
    logo = Image.open('logo.png')

    # Tamanho que o logo vai ter
    logo_size = 72

    # Posicao onde o logo será inserido xmin, ymin, xmax, ymax
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # redimensionamos o logo conforme calculado
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # fazemos a inserção
    img.paste(logo, (xmin, ymin, xmax, ymax))

    img.show()
    img.save('' + link[0] + '.png')
    #img.save('./tmp/'+str(nome_arquivo)+'.png')
    
