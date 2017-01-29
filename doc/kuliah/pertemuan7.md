<h2 align="center">INSTALASI MAP PROXY DAN MAP SERVER PADA UBUNTU<br></h2>
<p align="center">
<br>
<img src="../../img/pertemuan6.JPG" width="300" height="400">
</p><br>
<p align="justify">
<br><br>
<strong>PEMBUKAAN</strong><br>
<b>Latar Belakang Masalah</b><br>
Pada zaman sekarang yang semakin canggil ini berbagai macam cara bisa dilakukan dalam pemanfaatan geografis pada sistem digital seperti menyediakan map atau peta yang dibuat secara sistem sesuai dengan keinginan si pembuat peta. Salah satunya yaitu google maps. Adapun pada pembahasan kali ini akan menjelaskan bagaimna cara menjalankan map proxy dan map server yang telah diinstal sebelumnya di materi sebelumnya (pertemuan ke-6)<br>
<br>
<strong>ISI</strong><br>
Adapun cara menjalankannya yaitu sebagai berikut:<br>
a. Untuk meload data geospasial, kita perlu menyiapkannya dulu agar akan ditampilkan nantinya di Map Proxy. Kalian bisa mendownload data geospasial di situs ini, http://www.halaman.download/ kemudian pilih "Producer" dan klik "Indonesia Mapproxy".<br>
b. Jika sudah download ekstrak file tersebut (Penting!! Ketahui dimana anda mengekstrak file tersebut, karena path-nya akan digunakan untuk mengedit file yang ada di direktori yang telah di ekstrak tersebut.<br>
Disini saya simpan di direktori Downloads (Huruf kecil dan besar di perhatikan.)<br>
c. Pada file indomap -> mapproxy, akan terdapat 3 file. Buka file agm.yaml<br>
d. Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktori tempat anda menyimpan file tersebut :<br>
- pada baris<br>
binary: /usr/libexec/mapserver<br>
ubah menjadi<br>
binary: /usr/lib/cgi-bin/mapserv<br>
- pada baris<br>
map: var/mapdata/mapfile/indo.map<br>
ubah menjadi<br>
map: /home/eva/Downloads/indomap/mapfile/indo.map<br>
- Kemudian direktori baru dengan nama tmp pada direktori indomap<br>
ubah baris<br>
working_dir: /var/mapdata/tmp<br>
menjadi<br>
/home/eva/Downloads/indomap/tmp<br>
Kemudian Save <br>
e. Kemudian pada direktori mapproxy(di terminal/cmd), gunakan perintah :<br>
vi mapproxy.ini<br>
edit baris<br>
chdir = /var/mymapproxy/<br>
menjadi<br>
chdir = /home/ali/Downloads/indomap/mapproxy<br>
Kemudian Save<br>
f. edit file config.py pada direktori mapproxy<br>
ubah<br>
application = make_wsgi_app(r'/var/mymapproxy/agm.yaml')<br>
menjadi<br>
application = make_wsgi_app(r'/home/ali/Downloads/indomap/mapproxy/agm.yaml') <br>
g. Untuk menjalankan programnya gunakan perintah<br>
uwsgi mapproxy.ini<br>
h. Untuk mengecek apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080<br>
i.  Klik demo atau ketik localhost:8080/demo<br>
j. Pada bagian WMTS klik di bawah Image Format yaitu png<br>
k. Tunggu beberapa saat karna datanya sedang di load.<br>
l. Map Peta akan muncul<br>
<br>
<strong>PENUTUP</strong><br>
<b>Kesimpulan</b><br>
JSetelah dipraktekannya tutorial di atas, maka kita dapat mengetahui bagaimana cara menjalankan map server dan map proxy di dalam sistem operasi ubuntu.<br>
<br>
<b>Saran</b>
Praktikum tentang hal ini harus bisa lebih dipahami dimengerti, tidak hanya dibuat saja, tetapi harus tahu fungsi dari setiap perintah yang dieksekusi.
</p>

