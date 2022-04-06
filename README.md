# **Pendeteksi Link / URL Phishing (Phishing Detection)**

---

Final Capstone SIB x Dicoding Indonesia.
Team ID : CSD-178
Membangun sistem machine learning untuk mendeteksi link/url phishing menggunakan beberapa algoritma.

Langkah-langkah untuk menjalankan aplikasi

1. Install environment dibawah ini :

```sh
pip install uvicorn
pip install fastapi
pip install joblib
```

2. jalankan aplikasi melalui command prompt

```sh
python -m uvicorn url_phishing_detection:app
```

3. buka link di browser

Interactive API docs

```sh
https://127.0.0.1:8000/docs
```

Selesai, kalian tinggal masukkan link yang akan dilakukan pengecekan, tekan tombol ```execute```, kemudian hasil prediksinya akan muncul.