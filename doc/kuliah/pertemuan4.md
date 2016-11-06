<h2 align="center">RETRIEVE DATA GEOSPASIAL - Pertemuan ke-4 GIS<br></h2>
<p align="center">
<br>
<img src="../../img/pertemuan4_ilustrasi.JPG" width="400" height="200">
</p><br>
<p align="justify">
<br>
<strong>PEMBUKAAN</strong><br>
<b>Latar Belakang </b><br>
Seperti yang telah dijelaskan pada pertemuan sebelumnya bahwa untuk memanipulasi data geospasial khususnya pada data vektor dilakukan dengan cara CRUD (create, reatrieve, update, delete). Untuk lebih jelasnya tentang pembahasan Retrieve data maka pertemuan kali ini akan membahas tentang:<br>
a.	Retrieve Data Vektor<br>
b.	Operasi pengambilan data menggunakan pemrograman phyton pada library pyshp<br>
c.	Tugas praktikum membuat class geospasial editor dengan menggunakan method select where negara dengan menggunakan python.<br>
<br>
<strong>ISI</strong><br>
<b>A.	Retrieve Data Vektor</b><br>
Untuk meretrieve data atau menampilkan data geospasial (data vektor) yang berformat shape file atau .shp menggunakan library phyton yang bernama pyshp.<br>
Seperti yang kita ketahui bahwa shape file adalah standar file vektor geospasial yang dikeluarkan oleh perusahaan ESRI.<br>
Shape file memiliki 2 format.<br>
<i><b>1.	.shp</b></i><br>
Yang berisikan data geometri. Data geometri adalah data kordinat yang memiliki bangun data atau ruang.<br>
Diantaranya:<br>
a.	<i>Data point/ titik</i>. Data point memiliki nomor standar [1].<br>
b.	<i>Line/Garis/Polyline</i>. Polyline memiliki nomor standar [3]. Seperti yang digambarkan di bawah ini bahwa polyline tidak akan kembali ke titik awal seperti jalan, sungai dll.<br>
<p align="center">
<br>
<img src="../../img/pertemuan4_polyline.png" width="300" height="150">
</p><br>
 c.	<i>Polygon</i>. Memiliki nomor standar [5]. Adapun polygon akan kembali ke titik awal seperti gambar berikut. Contohnya adalah batas wilayah, negara dll.<br>
 <p align="center">
<br>
<img src="../../img/pertemuan4_polygon.png" width="300" height="150">
</p><br>
Dari ketiga hal tersebut maka ESRI menyebutkan bahwa point, polyline dan polygon disebut shape type yang memiliki nomor standar [1],[3], dan [5].<br>
<br>
<i><b>2.	.dbf</b></i><br>
Data yang berisikan tabel basis data.<br>
<br>
<br>
<b>B.	Operasi Pengambilan Data</b><br>
Operasi pengambilan data ini menggunakan library pyshp class shape file. Cara membukanya yaitu:<br>
a.	Buka cmd dan masuk ke dalam python<br>
b.	Baca shapefile<br>
<p align="center">
<img src="../../img/pertemuan4_sf.png" width="400" height="150">
</p><br>
<br> 
Kemudian, pada:<br>
<b>1.	.shp</b><br>
File shp ini berisikan bbox, parts, points dan shape type.<br>
Keterangan:<br>
•	<i>Bbox (Boarding Box)</i> merupakan batas view peta. Contohnya: koordinat a,b,c,d disebut dengan bbox. (ex in python: Nomor1.bbox)<br>
<p align="center">
<img src="../../img/pertemuan4_bali.png" width="300" height="150">
</p><br>
•	<i>Parts</i> = apakah record ini bagian record yang lainnya atau pecahan lainnya. (ex in python: Nomor1.parts)<br>
•	<i>Points</i> = yang membentuk titik-titik di peta/koordinat pembentuk peta. . (ex in python: Nomor1.points)<br>
•	<i>Shape type</i> = jenis geometri dari points. . (ex in python: Nomor1.shapeType)<br>
<br>
Adapun Operasi pada shp mengunakan method:<br>
-	Shapes()<br>
Contoh dalam menampilkan jumlah record :<br>
<p align="center">
<img src="../../img/pertemuan4_shapes.JPG" width="700" height="150">
</p><br> 
-	Shape (n), dimana n adalah nomor record.<br>
<br>
<b>2	.dbf</b><br>
Pada file dbf pengaksesannya menggunakan [ ].<br>
Adapun operasi pada dbf menggunakan method:<br>
-	records()<br>
-	record(n), dimana n merupakan nomor sequence record.<br>
<br>
<br>
<b>C.	Tugas Praktikum</b><br>
1.	buatlah class geospasial editor<br>
<p align="center">
<img src="../../img/pertemuan4_buatclass.JPG" width="400" height="250">
</p><br>
2.	Buatlah method select, where negara dengan record Indonesia<br>
<p align="center">
<br>
<img src="../../img/pertemuan4_methodselectwhere.JPG" width="600" height="200">
</p><br>

<strong>PENUTUP</strong><br>
<b>Kesimpulan</b><br>
Jadi untuk menampilkan atau meretrieve data vektor bisa menggunakna library python yang bernama pyshp. Di dalam itu bisa kita gunakan class dan method untuk mengambil data yang berformat shp.<br>

<b>Saran</b><br>
Lebih diperbanyak praktek karena berlatih secara langsung dapat memudahkan pelajar untuk memahami hal yang dipelajari dibandingkan dengan membaca materi beribu ribu halaman.<br>




