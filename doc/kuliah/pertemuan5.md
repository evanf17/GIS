<h2 align="center">MEMBUAT DAN MENGEDIT DATA GEOSPASIAL<br></h2>
<p align="center">
<br>
<img src="../../img/pertemuan5_ilustrasi.JPG" width="200" height="400">
</p><br>
<p align="justify">
<br><br>
<strong>PEMBUKAAN</strong><br>
<b>Latar Belakang Masalah</b><br>
Untuk melanjutkan dari pembahasan sebelumnya tentang manipulasi data geospasial, kali ini kita akan membahas tentang bagaimana cara membuat dan mengedit data geospasial menggunakan library pyshp.<br>
<br>
<strong>ISI</strong><br>
<b>A.	Cara Membuat Data Geospasial</b><br>
Pembuatan data geospasial ini menggunakan libarary pyshp. Untuk membuat data geospasial diperlukan file namafile.shp beserta namafile.dbf.<br>
Adapun langkahnya adalah sebagai berikut:<br>
a.	Import shapefile<br>
b.	Instansiasi writer method<br>
    sf = shapefile.Writer(param)<br>
    Dimana param adalah pilih shapetype:<br>
    1.	shapeType = 1<br>
    2.	shapeType = 3<br>
    3.	shapeType = 5<br>
c.	Sama seperti read, kita lakukan metode dbf dan shp.<br>
<br>
<b>-	Shapefile (shp)</b><br>
Untuk menambahkan record tergantung dengan type ESRInya.<br>
1. sf.point (x,y)<br>
3. sf.line = (parts: [[x,y],[z,w],...])<br>
6. sf.poly = (parts: [[x,y],[z,w],...])<br>

<br>
<b>-	Databasefile (dbf)</b><br>
Tahapannya adalah sebagi berikut:<br>
a.	Membuat atribut dahulu kemudian menambahkan record. <br>
    Contoh:<br>
    sf.field (‘Nama Filed’,’C’,’40’)<br>
    Dimana C adalah Character, dan 40 adalah length. Dalam arti nama atribut, nama field dengan panjang 40 karakter.<br>
b.	Tambahkan record dibawah ini<br>
    sf.record(‘Bandung’)<br>
    sf.record(‘Bandung’,’Sarijadi’)<br>
c.	Setelah selesai maka simpan, dengan perintah:<br>
sf.save(‘namafile.shp’)<br>
<br><br>
<b>B.	EDITING DATA GEOSPASIAL</b><br>
Adapun dalam editing data geospasial hampir sama dengan langkah-langkah membuat data geospasial, yang membedakan adalah:<br>
<i>sf = shapefile.Writer(param)</i><br>
diganti dengan<br>
<i>sf = shapefile.Editor(param)</i><br>
dimana param adalah nama letak file.<br>
<br>
Adapun operasi dalam editing pada shp dan dbf sama saja.<br>
<p align="center">
<br>
<img src="../../img/pertemuan5_tabel.JPG" width="300" height="150">
</p><br><br>
Dan jika sudah selesai, simpan dengan perintah:<br>
Sf.save(‘namafile’)<br>
<br>
<strong>PENUTUP</strong><br>
<b>Kesimpulan</b><br>
Jadi, untuk membuat dan mengedit data geospasial langkah-langkahnya hampir sama. Yang membedakan adalah method yang digunakan. Metgod yang digunakan untuk membuat data geospasial adalah WRITE sedangankan untuk mengedit adalah EDITOR.<br>
<br>
<b>Saran</b>
Adapun sarannya yaitu untuk memahami lebih lanjut dan lebih rinci tentang cara membuat dan mengedit data geospasial, bisa kita praktekan secara langsung menggunakan bahasa pemrograman python. Hal tesebut harus dicoba guna untuk mengetes langkah-langkah di atas berhasil atau tidak.
</p>

