saldo = 0
def awalan():
   pin = '12345'
   pin1 = 0
   count = 0
   while pin1 != pin and (count < 3):
       pin1 = input("Masukkan PIN anda:")
       count = count + 1
       if pin1 == pin:
          print("")
          print("==================================")
          print("PIN anda benar, Selamat datang.")
          print("==================================")
          print("")
       else :
          print("")
          print("===========================")
          print("Mohon maaf PIN anda salah.")
          print("===========================")
          print("")
          if count == 3:
              print("Akun anda kami tahan selama 24 JAM.")
              quit()

def menu():
    print("MENU :")
    print("1. Menu Transfer Tunai")
    print("2. Menu Isi Saldo")
    print("3. Menu Tarik Tunai")
    print("4. Menu Cek Saldo")
    print("5. Exit")
def menutunai():
    print("")
    print("Selamat Datang di Menu Transfer Tunai.")
    print("1. Transfer antar Bank BERSAMA")
    print("2. Transfer antar Bank Luar Negeri")
    print("3. Back")
def menusaldo():
    print("")
    print("Selamat Datang di Menu Isi Saldo.")
    print("1. Isi saldo")
    print("2. Back")
def menutarik():
    print("")
    print("Selamat Datang di Menu Tarik Tunai.")
    print("1. Tarik Tunai")
    print("2. Back")

awalan()
pil_0=""
while (pil_0 != 'n'):
    menu()
    pil = input("Masukkan pilihan anda :")
    if pil == '1':
        menutunai()
        pil2= input("Masukkan Pilihan anda:")
        if pil2 == '1':
           print("")
           print("======================================")
           if saldo < 50000 :
               print("Mohon isi saldo anda terlebih dahulu")
               print("======================================")
               print("")
           else:
               inp2 = int(input("Masukkan nominal transfer yang anda inginkan :"))
               saldo = saldo - inp2
               print("=====================================================================")
               print("Nominal Rp", inp2, "akan ditransfer dan sisa saldo anda Rp", saldo)
               print("=====================================================================")
        elif pil2 == '2':
            print("")
            print("======================================")
            if saldo < 50000 :
               print("Mohon isi saldo anda terlebih dahulu :")
               print("======================================")
               print("")
            else :
                inp3 = input("Masukkan nama bank tujuan anda :")
                inp4 = int(input("Masukkan nominal transfer yang anda inginkan :"))
                saldo = saldo - inp4
                print("================================================================================")
                print("Nominal Rp", inp4, "akan ditransfer ke bank", inp3, "dan sisa saldo Rp", saldo)
                print("================================================================================")
        elif pil2 == '3':
            print("")
            print("================")
            print("Terimakasih")
            print("================")
            print("")
        else :
            print("")
            print("=============================")
            print("Pilihan anda tidak dikenali")
            print("=============================")
            print("")

    elif pil == '2':
        menusaldo()
        pil3 = 0
        pil3 = input("Masukkan pilihan anda:")
        if pil3 == '1':
            inp5 = int(input("Masukkan Saldo yang ingin diisi:"))
            saldo = saldo + inp5
            print("")
            print("======================================")
            print("Saldo anda sekarang adalah", saldo)
            print("======================================")
            print("")
        elif pil3 == '2':
            print("")
            print("================")
            print("Terimakasih")
            print("================")
            print("")
        else :
            print("")
            print("==============================")
            print("Pilihan anda tidak dikenali")
            print("=============================")
            print("")
    elif pil == '3':
        menutarik()
        pil4 = 0
        pil4 = input("Masukkan pilihan anda :")
        if pil4 == '1':
            if saldo < 50000:
                print("Mohon isi saldo terlebih dahulu")
                print("")
            else :
                inp6 = int(input("Masukkan jumlah nominal tarik tunai :"))
                saldo = saldo - inp6
                print("")
                print("================================================================")
                print("Nominal Rp", inp6,"akan ditarik dan sisa saldo anda Rp", saldo)
                print("================================================================")

        elif pil4 == '2':
            print("")
            print("================")
            print("Terimakasih")
            print("================")
            print("")
        else :
            print("")
            print("============================")
            print("Pilihan anda tidak dikenali")
            print("============================")
            print("")
    elif pil == '4':
        print("")
        print("=======================================")
        print ("Saldo anda sekarang adalah", saldo)
        print("=======================================")
        print("")

    elif pil == '5':
        print("")
        print("=======================================")
        print("Terimakasih sudah memakai layanan kami")
        print("=======================================")
        quit()


    else :
        print("")
        print("=============================")
        print("Pilihan anda tidak dikenali")
        print("Harap coba lagi")
        print("============================")
        print("")

    pil_0 = input("Apakah anda ingin melanjutkan? (y/n) :")