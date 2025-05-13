# Twitter Giveaway Bot

Bot ini memungkinkan kamu untuk **mengirim tweet otomatis**, **like**, dan **retweet** di Twitter secara otomatis. Bot ini berguna untuk mengikuti giveaway, promosi, atau kegiatan serupa yang melibatkan interaksi otomatis di Twitter.

## Fitur

- **Mengirim tweet otomatis**: Bot akan memposting tweet dengan konten yang acak setiap hari.
- **Like dan Retweet otomatis**: Setelah tweet diposting, bot akan otomatis melakukan like dan retweet.
- **Interaksi dengan akun tertentu**: Bot akan menyebut akun tertentu di setiap tweet secara acak, seperti @GiveRep, @teman1, dan @teman2.
- **Otentikasi menggunakan OAuth 1.0a**: Bot menggunakan OAuth 1.0a untuk autentikasi dengan API Twitter.

## Persyaratan

1. **Python 3.x**: Pastikan kamu sudah menginstall Python versi terbaru.
2. **Library yang dibutuhkan**:
    - `requests`
    - `requests-oauthlib`
    - `python-dotenv`
    
   Install semua dependensi ini dengan menjalankan:

   ```bash
   pip install requests requests-oauthlib python-dotenv
   
## Twitter Developer Account:

Kamu harus memiliki akun Twitter Developer untuk mendapatkan API keys.

Buat aplikasi baru di Twitter Developer Portal dan pastikan permission untuk "Read and Write" diaktifkan.

Generate API keys dan Access Tokens yang dibutuhkan untuk autentikasi.

Setup
1. Mengatur Twitter Developer Credentials
Setelah kamu membuat aplikasi di Twitter Developer Portal, kamu perlu mengisi file .env dengan kredensial yang didapatkan dari portal tersebut.

Buat file .env di root folder proyek dan isi dengan informasi berikut:

      API_KEY=YourAPIKey
      API_SECRET_KEY=YourAPISecretKey
      ACCESS_TOKEN=YourAccessToken
      ACCESS_TOKEN_SECRET=YourAccessTokenSecret
API Key: Dapatkan dari Keys and Tokens di Twitter Developer Portal.

API Secret Key: Dapatkan dari Keys and Tokens.

Access Token: Dapatkan dari Keys and Tokens setelah memberikan izin aplikasi.

Access Token Secret: Dapatkan dari Keys and Tokens.

2. Menjalankan Bot
Setelah semua kredensial terpasang di .env, kamu bisa menjalankan script utama dengan perintah:
    
       python3 main.py
   
