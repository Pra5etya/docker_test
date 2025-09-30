# Kapan Menggunakan Docker

1. Kamu bisa bikin container berisi environment yang konsisten serta menghindari package error
    * misal: Flask versi tertentu + database.

2. Ingin custom OSI atau port sendiri
    * misal: menggunakan docker-compose

3. Cocok untuk team development, CI/CD, atau aplikasi yang butuh banyak service sekaligus
    * misal: web + database + redis + message broker.

4. Lebih rapi: nggak "mengotori" OS yang digunakan

# Cara Penerapan Docker

1. Buat aplikasi sederhana terlebih dahulu lalu buat Dockerfile (bisa dilihat di note atau contoh Dockerfile)

2. Aplikasi yang membutuhkan service (packages terpisah dari library environment) maka diperlukan docker-compose.yaml, adanya docker-compose.yaml bisa custom Port (OSI) atau I/O nya

3. File atau direktori yang tidak di masukan ke docker bisa diterapkan ke .dockerignore

4. Selain itu ekstensi service yang ada di library juga harus di setting agar bisa di jalankan pada program