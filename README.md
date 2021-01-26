# Tugas Kecil 1 Strategi Algoritme: Penyelesaian <i>Cryptarithmetic</i> dengan Algoritma <i>Brute Force</i>
Program ini dibuat dalam rangka memenuhi tugas kecil dari mata kuliah IF2211 Strategi Algoritma Semester 2 tahun 2020/2021. Program memiliki fungsi mencari solusi dari suatu persoalan cryptarithmetic dengan menggunakan algoritma <b>Brute Force</b>. 
<br><br>Secara sederhana, pertama program membuka file berisi persoalan cryptarithmetic. Kemudian program <b>membuat himpunan</b> huruf yang muncul dalam persoalan tersebut. Lalu, program menghasilkan <b>permutasi</b> dari 10 digit yang mungkin, kemudian himpunan huruf sebelumnya dibuat <b>mapping</b> ke hasil permutasi tadi. Terakhir, program meng<b>kalkulasi</b> hasil substitusi terhadap operand dan hasil. Jika hasilnya sama, akan ditampilkan mapping yang digunakan, jika tidak, dicari mapping permutasi yang lain hingga seluruh permutasi selesai.

## Cara Menggunakan:
File executable tidak dapat dibuat sehingga program perlu dijalankan menggunakan Command Prompt untuk memastikan berhasil bekerja.<br>
1. Buka folder src, pastikan terdapat cryptarithm_solver.py
2. Buka folder test, pastikan terdapat file uji dengan format soalX.txt (X adalah angka 1 s.d. 10)
3. Buka Command Prompt (pada Windows), lalu ganti direktori ke dalam folder src
4. Eksekusi perintah "py cryptarithm_solver.py"
5. Program akan berjalan secara otomatis hingga seluruh file dalam folder test dibaca

## Tentang Pembuat
Leonardus Brandon Luwianto (13519102) merupakan mahasiswa semester 4 Teknik Informatika ITB pada Januari 2021.
