# Troubleshooting GitHub Actions

## 🔍 Langkah Debugging

### 1. Pastikan Struktur Folder Benar
Struktur yang HARUS ada di repository GitHub:
```
repository-root/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── src/
├── tests/
└── requirements.txt
```

### 2. Check File Workflow Ada
Buka repository di GitHub → klik folder `.github` → `workflows` → pastikan file `ci.yml` ada

### 3. Jika Folder .github Tidak Ada:

**Cara 1: Upload Manual di GitHub**
1. Di repository GitHub, klik "Add file" → "Create new file"
2. Ketik nama file: `.github/workflows/ci.yml`
3. Copy paste isi dari file ci.yml
4. Commit file

**Cara 2: Push Ulang dari Local**
```bash
# Pastikan di folder CICD examples
cd "d:\kampus\STQA\materi\txt\CICD examples"

# Check apakah folder .github ada
dir .github

# Jika tidak ada, buat ulang
mkdir .github
mkdir .github\workflows

# Copy file workflow (sudah ada di folder ini)
# Lalu push ulang
git add .
git commit -m "Add GitHub Actions workflows"
git push origin main
```

### 4. Trigger Workflow Manual
Setelah file workflow ada:
1. GitHub repository → Actions tab
2. Pilih workflow "CI Pipeline"
3. Klik "Run workflow" → "Run workflow"

## ✅ Cara Memastikan Berhasil
- Actions tab menampilkan workflow
- Ada tombol "Run workflow"
- Workflow berjalan saat push ke main branch