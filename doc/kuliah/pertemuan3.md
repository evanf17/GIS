<h2 align="center">MANIPULASI DATA GEOSPASIAL - Pertemuan ke-3 GIS<br></h2>
<p align="center">
<br>
<img src="../../img/pertemuan3.jpg" width="400" height="200">
</p><br>
<p align="justify"> 
<strong>PEMBUKAAN</strong><br>
<b>Latar Belakang </b><br>
Pada pertemuan ke-3 Sistem Informasi Geografis ini, saya akan membahas tentang bagaimana memanipulasi data geospasial seperti hal nya pada framework lain pada data vektor yang berformat shp. Untuk memanipulasi data geospasial yaitu dengan CRUD. Mari kita uraikan bagaimana caranya memanipulasi data khususnya bagian retrieve, file yang dibutuhkannya, aplikasi yang dipakai serta tutorial penggunaan library py shp.<br>
<br>
<strong>ISI</strong><br>
Cara memanipulasi data geospasial dapat dilakukan dengan CRUD. Apa itu CRUD? CRUD berasal dari singkatan dari Create Retrieve Update Delete , yang sering digunakan pada software atau aplikasi pengolahan data yang kebanyakan menggunakan fungsi CRUD didalamnya termasuk dalam pengelolaan data geospasial . CRUD ini digunakan untuk menambahkan data, menghapus data, serta mengubah data dan menampilkan data.<br>

Dikhususkan pada penjelasan <b>Retrieve</b>. Retrieve adalah bagaian dari manipulasi data yang digunakan untuk melihat isi data pada geospasial berupa data vektor yaitu yang berbentuk shape file yang diluncurkan oleh ESRI dengan extensil .shp.<br>

File yang dibutuhkan untuk melakukan manipulasi data yaitu:<br>
1. shp -> berupa koordinat/titik.<br>
2. dbf -> berupa tabel/database.<br>
3. shx -> berisi index data<br>

Dari ketiga file tersebut, ketiganya dapat dibuka menggunakan aplikasi:<br>
<b>a. QGIS</b> <br>
&nsbp;&nsbp;&nsbp;QGIS adalah aplikasi untuk mempelajari sistem informasi geografis (include data geospasial). Cara menggunakannnya yaitu:<br>
- buka aplikasi QGIS<br>
- klik kanan view data (buka filenya kemudian drag & drop). Pertama masukan dulu file .shp nya kemudian disusul dengan file .dbf yang terdapat pada natural earth.<br>
<b>b. Library py shp</b><br>
&nsbp;&nsbp;&nsbp;Library py shp merupakan library dari bahasa pemrograman python. Caranya yaitu:<br>
- install python. Dalam python terdapat dua bentuk. yaitu console (dipakai untuk debug/trial/coba-coba) dan script(di dalam satu file terdapat script python)<br>
- install pip<br>
- install py shp<br>
- mulai pengkodean<br>
Untuk pengguna linux, untuk melakukan library shp tidak usah menginstall yang di atas, tetapi untuk pengguna windows disarankan untuk menginstall jika ingin memakai libarary py shp.<br>

Berikut adalah contoh pengkodean atau script untuk menghitung jumlah record pada sebuah file yang berformat shp:<br>
- masuk ke lokasi python terlebih dahulu<br>
- ketikan python<br>
- ketikan import shape file<br>
- ketikan a=shapefile.Reader ('shp/bts_negara.shp')<br>
- ketikan b=a.shapes()<br>
- ketikan print len (b)<br>
<br>
Untuk lebih jelasnya bisa kunjungi tutorialnya pada akun youtube saya https://youtu.be/WKeO5SJmgR8<br>

<br>
<strong>PENUTUP</strong><br>
<strong>Kesimpulan</strong><br>
Jadi untuk memanipulasi data dengan cara CRUD (create, retrieve, update, delete). Untuk melihat isi data (retrieve) bisa menggunakan aplikasi QGIS atau library py shp yang menggunakan bahasa python. <br>
<br>
<strong>Saran</strong><br>
Tutorial di atas perlu dicoba atau dipraktekan guna untuk mempelajari lebih lanjut tentang memanipulasi data geospasial.<br>
<br>
Sekian terimakasih.<br>
<br>

Referensi: http://jagocoding.com/tutorial/684
</p>



