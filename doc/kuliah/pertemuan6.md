<h2 align="center">INSTALASI MAP PROXY DAN MAP SERVER PADA UBUNTU<br></h2>
<p align="center">
<br>
<img src="../../img/pertemuan6.JPG" width="300" height="400">
</p><br>
<p align="justify">
<br><br>
<strong>PEMBUKAAN</strong><br>
<b>Latar Belakang Masalah</b><br>
Pada zaman sekarang yang semakin canggil ini berbagai macam cara bisa dilakukan dalam pemanfaatan geografis pada sistem digital seperti menyediakan map atau peta yang dibuat secara sistem sesuai dengan keinginan si pembuat peta. Salah satunya yaitu google maps. Adapun pada pembahasan kali ini akan menjelaskan bagaimna cara membuat maps secara custom.<br>
<br>
<strong>ISI</strong><br>
<b>1. Pengertian Map Server</b><br>
Secara singkat map server adalah penyedia layanan (web service peta). Dalam arti Map Server adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG). MapServer dikembangkan oleh University of Minnesota - jadi, sering dan lebih khusus disebut sebagai "UMN MapServer", untuk membedakannya dari komersial "peta server". MapServer awalnya dikembangkan dengan dukungan dari NASA, yang membutuhkan cara untuk membuat citra satelit yang tersedia untuk umum.<br>

<br><br>
<b>2. Pengertian Map Proxy</b><br>
Map proxy adalah aplikasi penampung data sementara dari penyedia layanan web (web service) peta, agar pengambilan data yang berulang-ulang lebih cepat (tanpa meminta kembali ke map server).<br>
<br>
<b>3. Web Service Peta</b><br>
Web service peta terdiri dari 2 bagian, yaitu:<br>
a. <i>Lossly</i> (ada data yang dibuang). Seperti WMS (Web Map Service) dan WMTS (Web Map Tile Service)<br>
b. <i>Lossless</i> seperti WFS (web Feature Service) dan WCS (Web Corrage Service)<br>
Keseluruhan format ini distandarkan oleh organisasi OGC.<br>
<br>
<b>4. Cara Instalasi Map Server dan Map Proxy</b><br>
Untuk menginstalasi map server direkomendasikan menggunakan linux atau virtualbox.<br>
LAngkahnya: <br>
a. Buka terminal (ubuntu)<br>
b. Ketikan perintah sudo apt-get install cgi-mapserver<br>
c. Untuk mengetahui struktur direktori Map Server, gunakan perintah : dpkg -L cgi-mapserver<br>
d. Karena saya mengeksekusinya menggunakan python, install python juga dengan perintah : sudo apt-get install python-pip python-dev<br>
e. Kemudian install uwsgi, dengan perintah : sudo pip install uwsgi<br>
f. Kemudian install Map Proxy, dengan perintah : sudo pip install MapProxy <br>
g. Setelah diinstall maka unduh peta Indonesia dan konfigurasi map proxy serta map file dari map server di halaman download.<br>
<br>
<strong>PENUTUP</strong><br>
<b>Kesimpulan</b><br>
Jadi, untuk membuat map secara custom, kita harus terlebih dahulu menginstall map server dan map proxy pada ubuntu (disarankan).<br>
<br>
<b>Saran</b>
Praktikum tentang hal ini harus bisa lebih dipahami dimengerti, tidak hanya dibuat saja, tetapi harus tahu fungsi dari setiap perintah yang dieksekusi.
</p>

