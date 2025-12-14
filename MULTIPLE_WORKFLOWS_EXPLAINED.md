# Multiple Workflows di GitHub Actions

## 🔄 Bagaimana Multiple Workflows Bekerja

### Jika Ada 3 Workflow Files:
```
.github/workflows/
├── ci.yml           # Workflow 1
├── advanced-ci.yml  # Workflow 2
└── simple-ci.yml    # Workflow 3
```

### Yang Terjadi Saat Push:
```
Push ke main branch
    ↓
GitHub Actions mendeteksi 3 workflows
    ↓
Menjalankan SEMUA 3 workflows secara PARALLEL
    ↓
├── CI Pipeline (dari ci.yml) - BERJALAN
├── Advanced CI Pipeline (dari advanced-ci.yml) - BERJALAN  
└── Simple CI (dari simple-ci.yml) - BERJALAN
```

## 📋 Contoh di Actions Tab:

Anda akan melihat:
```
✅ Simple CI #123
❌ CI Pipeline #123  
✅ Advanced CI Pipeline #123
✅ CD Pipeline #123
```

**Semua berjalan untuk commit yang sama!**

## ⚠️ **Masalah dengan Multiple CI Workflows:**

### 1. **Resource Waste**
- 3x lebih banyak compute time
- 3x lebih banyak GitHub Actions minutes
- Redundant testing

### 2. **Confusion**
- Mana yang harus diperhatikan?
- Jika 1 gagal, 2 berhasil → bingung
- PR checks jadi banyak

### 3. **Slower Feedback**
- Harus tunggu semua selesai
- Lebih lama untuk merge PR

## ✅ **Best Practice: Pilih Satu Saja**

### Untuk Learning/Demo:
**Gunakan `simple-ci.yml` saja**
- Lebih reliable
- Cepat
- Easy to debug

### Untuk Production:
**Gunakan `ci.yml` (basic)**
- Comprehensive testing
- Security scanning
- Multi-Python versions

### Untuk Advanced Learning:
**Gunakan `advanced-ci.yml`**
- Multi-OS testing
- Performance testing
- Documentation checks

## 🛠️ **Cara Mengelola Multiple Workflows:**

### Option 1: Hapus yang Tidak Perlu
```bash
# Keep only simple-ci.yml
rm .github/workflows/ci.yml
rm .github/workflows/advanced-ci.yml

git add .
git commit -m "Keep only simple CI"
git push origin main
```

### Option 2: Rename untuk Disable
```bash
# Rename to .yml.disabled
mv .github/workflows/ci.yml .github/workflows/ci.yml.disabled
mv .github/workflows/advanced-ci.yml .github/workflows/advanced-ci.yml.disabled
```

### Option 3: Different Triggers
Edit each workflow dengan trigger berbeda:

**simple-ci.yml** - untuk development:
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

**ci.yml** - untuk release:
```yaml
on:
  push:
    tags: [ 'v*' ]
  release:
    types: [published]
```

**advanced-ci.yml** - manual only:
```yaml
on:
  workflow_dispatch:  # Manual trigger only
  schedule:
    - cron: '0 2 * * *'  # Nightly build
```

## 🎯 **Rekomendasi untuk Anda:**

### Saat Ini (Learning):
1. **Hapus `ci.yml` dan `advanced-ci.yml`**
2. **Keep only `simple-ci.yml`**
3. **Pastikan simple-ci.yml berjalan ✅**
4. **Setelah paham, bisa coba yang lain**

### Commands:
```bash
cd "CICD examples"

# Remove complex workflows
rm .github/workflows/ci.yml
rm .github/workflows/advanced-ci.yml

# Keep only simple-ci.yml
git add .
git commit -m "Simplify to one CI workflow"
git push origin main
```

## 📊 **Hasil Setelah Simplify:**

Actions tab akan show:
```
✅ Simple CI #124
✅ CD Pipeline #124
```

**Lebih clean, lebih mudah dipahami!**

## 🔍 **Kapan Gunakan Multiple Workflows:**

### Use Cases yang Valid:
1. **Different Purposes**:
   - `ci.yml` - Testing
   - `cd.yml` - Deployment
   - `security.yml` - Security scan

2. **Different Triggers**:
   - `pr-ci.yml` - Untuk PR only
   - `main-ci.yml` - Untuk main branch only
   - `nightly.yml` - Scheduled runs

3. **Different Environments**:
   - `dev-ci.yml` - Development testing
   - `prod-ci.yml` - Production validation

### Avoid Multiple Similar Workflows:
- ❌ `ci.yml`, `simple-ci.yml`, `advanced-ci.yml` untuk same purpose
- ✅ Pick one yang sesuai needs Anda

## 💡 **Pro Tips:**

1. **Start Simple**: Gunakan simple-ci.yml dulu
2. **One Purpose per Workflow**: Jangan duplicate functionality  
3. **Clear Naming**: Nama workflow harus jelas purposenya
4. **Monitor Usage**: Check GitHub Actions usage di Settings
5. **Optimize Triggers**: Jangan trigger semua workflow untuk every push