while True:
    hissedegeri=float(input("lütfen alacağınız hissenin değerini giriniz"))
    hisseadet=float(input("lütfen almak istediğiniz adet sayısını belirleyiniz"))
    alinandeğer=hissedegeri*hisseadet
    print("tebrikler,",alinandeğer,"değerinde hisse aldınız")
    print("şimdi ise hissenizin gelecekteki değerini hesaplayalım")
    hisseartangünsayisi=int(input("lütfen hissenizin değiştiği gün sayısını söyleyiniz"))
    hisseartismiktari=float(input("lütfen hissenizin günlük değişim miktarını yüzde olarak söyleyiniz.Ornek(5)"))
    i=0
    hisseyenideger=alinandeğer
    while i<hisseartangünsayisi:
        i=i+1
        hisseyenideger=hisseyenideger+(hisseyenideger*(hisseartismiktari/100))
        
        
    kazanc = hisseyenideger - alinandeğer
    print("hissenizin",hisseartangünsayisi,"gün sonraki degeri=",hisseyenideger)
    print("TL kazancınız= ",kazanc)
    print("Yüzde kazancınız= ",100*kazanc/alinandeğer)

