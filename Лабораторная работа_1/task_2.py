one_symbol = 4
one_stroke = one_symbol * 25
page = one_stroke * 50
book = page * 100
book_mb = book / 1024 / 1024
voluem_ = 1.44
number = voluem_ / book_mb
weight = round(number)
print("Количество книг, помещающихся на дискету:", weight)

