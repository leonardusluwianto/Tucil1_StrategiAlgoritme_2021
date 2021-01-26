import os
import time

# Fungsi untuk mengonversi kata menjadi bilangan
def kata_ke_angka(kata, huruf_dict):
    total_nilai = 0
    faktor = 1

    for huruf in reversed(kata):
        total_nilai += faktor * huruf_dict[huruf]
        faktor *= 10
    
    return total_nilai

# Fungsi untuk menghitung permutasi dari array digit
def permutasi(digitList, ID_bawah, ID_atas):
    if ID_bawah == ID_atas:
        yield digitList
    else:
        for i in range(ID_bawah, ID_atas + 1):
            digitList[ID_bawah], digitList[i] = digitList[i], digitList[ID_bawah]
            yield from permutasi(digitList, ID_bawah + 1, ID_atas)
            digitList[ID_bawah], digitList[i] = digitList[i], digitList[ID_bawah]

# Fungsi untuk memeriksa apakah ada kata yang huruf pertamanya memiliki nilai subtitusi sama dengan 0
def hurufPertamaTidakNol(listHurufPertama, subtitusi):
    nilai = True
    for huruf in listHurufPertama:
        if subtitusi[huruf] == 0:
            nilai = False
            break
    return nilai

def solve_cryptarithmetic(file_name):
    # BUKA FILE
    file_sample = open(file_name, 'r')
    Lines = file_sample.readlines() 

    # MEMASUKKAN HURUF PER BARIS DALAM FILE KE LIST
    waktu_mulai = time.time()

    container = []              
    container_teks = []         
    huruf_pertama = set()    

    for line in Lines:
        container_teks.append(''.join(c for c in line if c.isalnum()))
        teks = list([val for val in line.strip() if val.isalpha()])
        container.append(teks)
        if (len(teks) > 0):
            huruf_pertama.update(teks[0])

    container_hurufPertama = list(huruf_pertama)

    # MEMBUAT HIMPUNAN HURUF DALAM FILE
    char_set = set()

    i = 0

    for i in range(len(container)):
        char_set.update(container[i])

    list_char_set = list(char_set)

    # MENAMPILKAN SOAL
    print('Soal:')
    i = 0
    for i in range(len(container_teks)):
        if (i < len(container_teks) - 3):
            print(container_teks[i] + ' + ', end = '')
        elif (i == len(container_teks) - 3):
            print(container_teks[i] + ' = ', end = '')
        elif (i == len(container_teks) - 1):
            print(container_teks[i])

    # MENAMPIILKAN SOLUSI
    print('\nSolusi: ')

    digits = list(range(10))
    panjangDigit = len(digits)

    total_test = 0

    waktu_komputasi_pertama = time.time()

    for nilaiPermutasi in permutasi(digits, 0, panjangDigit - 1):
        sol = dict(zip(list_char_set, nilaiPermutasi))

        total_test += 1

        if hurufPertamaTidakNol(container_hurufPertama, sol) == True:
            total_operand = 0
            j = 0
            container_subtitusi = []

            for j in range(len(container_teks) - 2):
                container_subtitusi.append(kata_ke_angka(container_teks[j], sol))
                total_operand += container_subtitusi[j]

            hasil_jumlah = kata_ke_angka(container_teks[-1], sol)

            if total_operand == hasil_jumlah:
                k = 0
                for k in range(len(container_subtitusi)):
                    if k != len(container_subtitusi) - 1:
                        print(str(container_subtitusi[k]) + ' + ', end = '')
                    else:
                        print(str(container_subtitusi[k]), end = '')
                print(' = ' + str(hasil_jumlah) + ' {} #TEST: {} #TIME: {:.5f}'.format(sol, total_test, time.time() - waktu_komputasi_pertama))

    waktu_selesai = time.time()

    # INFORMASI TAMBAHAN
    print('\nJumlah Total Test: ' + str(total_test))
    print('Komputasi Pertama: {:.5f}'.format(waktu_komputasi_pertama - waktu_mulai))
    print('Total Waktu Komputasi: {:.5f}'.format(waktu_selesai - waktu_komputasi_pertama))
    print('Total Waktu Eksekusi Program: {:.5f}'.format(waktu_selesai - waktu_mulai))

if __name__ == '__main__':
    current_dirr = os.path.dirname(__file__)
    parent_dirr = os.path.split(current_dirr)[0]
    file_path = os.path.join(parent_dirr, 'test')
    
    for file_name in os.scandir(file_path):
        solve_cryptarithmetic(file_name)
        print()



