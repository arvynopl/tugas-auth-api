# Implementasi Sistem Autentikasi API Menggunakan FastAPI

## Informasi Pengembang

Dikembangkan oleh: Arvyno Pranata Limahardja
- NIM: 18222007
- Mata Kuliah: II3160 Teknologi Sistem Terintegrasi

## Deskripsi Singkat

Proyek ini merupakan implementasi sistem autentikasi API dengan menggunakan framework FastAPI. Sistem ini menyediakan mekanisme autentikasi berbasis username/password dan otorisasi menggunakan API key.

## Fitur Sistem

- Autentikasi pengguna menggunakan username dan password
- Otorisasi akses API menggunakan API key
- Implementasi rute publik dan terproteksi
- Penyimpanan password menggunakan hashing bcrypt
- Validasi data menggunakan Pydantic models
- Penanganan kesalahan komprehensif
- Dokumentasi API otomatis

## Struktur Proyek

```plaintext
fastapi_auth_project/
├── app/
│   ├── __init__.py
│   ├── main.py                     # Aplikasi utama FastAPI
│   ├── config.py                   # Konfigurasi sistem
│   ├── security/                   # Modul keamanan
│   │   ├── __init__.py
│   │   ├── auth.py                # Logika autentikasi
│   │   └── models.py              # Model data
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           └── routes.py          # Endpoint API
├── requirements.txt               # Dependensi proyek
└── README.md                     # Dokumentasi proyek
```

## Langkah-langkah Instalasi

1. Mengunduh repositori:
```bash
git clone https://github.com/username/fastapi-auth-project.git
cd fastapi-auth-project
```

2. Membuat dan mengaktifkan virtual environment:
```bash
# Untuk sistem Windows
python -m venv venv
venv\Scripts\activate

# Untuk sistem Unix/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Mengunduh dependensi:
```bash
pip install -r requirements.txt
```

## Konfigurasi Sistem

Membuat file `.env` pada direktori utama dengan isi sebagai berikut:
```env
SECRET_KEY=kunci-rahasia-anda
JWT_SECRET_KEY=kunci-jwt-anda
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Menjalankan Aplikasi

Menjalankan server menggunakan perintah:
```bash
uvicorn app.main:app --reload
```

Aplikasi dapat diakses melalui: `http://127.0.0.1:8000`

## Dokumentasi API

### 1. Endpoint Publik
- `GET /api/v1/public`
  - Deskripsi: Endpoint yang dapat diakses tanpa autentikasi
  - Response:
    ```json
    {
        "message": "This is a public endpoint"
    }
    ```

### 2. Endpoint Login
- `POST /api/v1/login`
  - Deskripsi: Autentikasi pengguna
  - Request Body:
    ```json
    {
        "username": "johndoe",
        "password": "secret123"
    }
    ```
  - Respons: Token akses dan API key

### 3. Endpoint Terproteksi
- `GET /api/v1/secure`
  - Deskripsi: Endpoint yang memerlukan autentikasi
  - Header yang diperlukan: `X-API-Key: [api-key]`
  - Response: Data terproteksi

## Pengujian API

Pengujian dilakukan menggunakan Thunder Client dengan pembuktian berupa screenshot pada dokumen laporan. 

Di bawah ini juga disediakan cara lain pengujian API dengan menggunakan command curl:

### 1. Pengujian Endpoint Publik
```bash
curl http://127.0.0.1:8000/api/v1/public
```

### 2. Pengujian Login
```bash
curl -X POST http://127.0.0.1:8000/api/v1/login \
  -H "Content-Type: application/json" \
  -d '{"username":"johndoe","password":"secret123"}'
```

### 3. Pengujian Endpoint Terproteksi
```bash
curl http://127.0.0.1:8000/api/v1/secure \
  -H "X-API-Key: [api-key-hasil-login]"
```

## Aspek Keamanan

- Implementasi password hashing menggunakan bcrypt
- Proteksi endpoint menggunakan API key
- Sistem token JWT dengan masa berlaku
- Validasi input menggunakan Pydantic
- Implementasi CORS untuk keamanan lintas domain

## Penanganan Error

Sistem mengembalikan kode status HTTP yang sesuai:
- 401: Unauthorized - Kredensial tidak valid
- 403: Forbidden - Tidak memiliki izin akses
- 422: Unprocessable Entity - Format data tidak valid

## Teknologi yang Digunakan

- FastAPI (Framework utama)
- Uvicorn (Server ASGI)
- Python-Jose[cryptography] (Implementasi JWT)
- Passlib[bcrypt] (Password hashing)
- Python-multipart (Parsing form data)
- Python-dotenv (Manajemen variabel lingkungan)

## Referensi

1. FastAPI Documentation. https://fastapi.tiangolo.com/
2. FastAPI Security. https://fastapi.tiangolo.com/tutorial/security/
3. Python Documentation. https://docs.python.org/3/