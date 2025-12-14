# Cara Membuat Pull Request untuk Testing CI/CD

## 🎯 Tujuan
Membuat Pull Request untuk menguji CI pipeline yang berjalan otomatis saat PR dibuat.

## 📋 Step-by-Step

### Step 1: Buat Branch Baru
```bash
# Pastikan di folder project
cd "d:\kampus\STQA\materi\txt\CICD examples"

# Buat dan pindah ke branch baru
git checkout -b feature/test-ci

# Atau jika git checkout tidak work:
git branch feature/test-ci
git switch feature/test-ci
```

### Step 2: Buat Perubahan Kecil
Edit file `src/calculator.py` - tambah fungsi baru:

```python
def square(self, a):
    """Menghitung kuadrat dari angka"""
    return a * a
```

### Step 3: Buat Test untuk Fungsi Baru
Edit file `tests/test_calculator.py` - tambah test:

```python
def test_square(self):
    """Test fungsi kuadrat"""
    self.assertEqual(self.calc.square(4), 16)
    self.assertEqual(self.calc.square(0), 0)
    self.assertEqual(self.calc.square(-3), 9)
```

### Step 4: Commit dan Push Branch
```bash
# Add changes
git add .

# Commit dengan message yang jelas
git commit -m "Add square function and tests"

# Push branch baru ke GitHub
git push origin feature/test-ci
```

### Step 5: Buat Pull Request di GitHub
1. **Buka repository di GitHub**
2. **Akan muncul banner**: "feature/test-ci had recent pushes" → klik **"Compare & pull request"**
3. **Atau manual**: klik "Pull requests" → "New pull request"
4. **Set branches**:
   - Base: `main`
   - Compare: `feature/test-ci`
5. **Isi PR details**:
   - Title: "Add square function for CI testing"
   - Description: "Testing CI pipeline with new feature"
6. **Klik "Create pull request"**

### Step 6: Lihat CI Berjalan
Setelah PR dibuat:
1. **Scroll ke bawah di PR page**
2. **Lihat section "Checks"** - akan muncul:
   - ⏳ CI Pipeline / Test and Code Quality (in progress)
   - ⏳ CI Pipeline / Security Scan (pending)
   - ⏳ CI Pipeline / Build Package (pending)
3. **Klik "Details"** untuk lihat logs
4. **Tunggu sampai semua ✅ atau ❌**

## 🧪 Alternative: Testing Tanpa PR

### Cara 1: Push ke Main Branch
```bash
# Langsung edit di main branch
git checkout main

# Edit file (tambah comment atau fungsi kecil)
# Commit dan push
git add .
git commit -m "Test CI pipeline"
git push origin main

# CI akan berjalan otomatis
```

### Cara 2: Manual Trigger
1. **GitHub repository → Actions tab**
2. **Pilih "CI Pipeline"**
3. **Klik "Run workflow"**
4. **Pilih branch "main"**
5. **Klik "Run workflow"**

## 📊 Cara Melihat Hasil CI

### Di Actions Tab:
1. **GitHub repository → Actions**
2. **Klik workflow run** (yang sedang berjalan atau selesai)
3. **Lihat jobs**:
   - Test and Code Quality
   - Security Scan  
   - Build Package
4. **Klik job untuk lihat detail logs**

### Di Pull Request:
1. **Buka PR yang dibuat**
2. **Scroll ke "Checks" section**
3. **Lihat status setiap check**
4. **Klik "Details" untuk logs**

## ✅ Success Indicators

### CI Pipeline Berhasil:
- ✅ All checks passed
- ✅ Tests: X passed, 0 failed
- ✅ Coverage: >80%
- ✅ Linting: No errors
- ✅ Security: No vulnerabilities

### CI Pipeline Gagal:
- ❌ Some checks failed
- ❌ Test failures
- ❌ Linting errors
- ❌ Security issues

## 🔧 Jika CI Gagal

### Common Fixes:
```bash
# Fix linting errors
black .
flake8 .

# Run tests locally first
pytest tests/ -v

# Fix dan push ulang
git add .
git commit -m "Fix CI issues"
git push origin feature/test-ci
```

## 🎯 Learning Points

1. **Branch Strategy**: Feature branch → PR → Main
2. **Automated Testing**: CI runs on every PR
3. **Code Quality Gates**: Must pass before merge
4. **Feedback Loop**: Quick feedback on code changes
5. **Collaboration**: PR review process