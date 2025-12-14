# Calculator CI/CD Demo

Proyek ini adalah demonstrasi implementasi **Continuous Integration (CI)** dan **Continuous Deployment (CD)** menggunakan **GitHub Actions** untuk mata kuliah STQA Bab 12-13.

## 📋 Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Struktur Proyek](#struktur-proyek)
- [Fitur CI/CD](#fitur-cicd)
- [Cara Menjalankan](#cara-menjalankan)
- [Cara Menguji](#cara-menguji)
- [GitHub Actions Workflows](#github-actions-workflows)
- [Cara Melihat Keberhasilan](#cara-melihat-keberhasilan)

## 🎯 Tentang Proyek

Proyek ini berisi:
- **Aplikasi Calculator sederhana** (Python) dengan operasi matematika dasar
- **Unit Tests** lengkap dengan coverage reporting
- **CI Pipeline** otomatis dengan GitHub Actions
- **CD Pipeline** untuk deployment ke staging dan production
- **Code Quality Tools** (linting, formatting, security scanning)

## 📁 Struktur Proyek

```
CICD examples/
├── .github/
│   └── workflows/
│       ├── ci.yml          # Continuous Integration workflow
│       └── cd.yml          # Continuous Deployment workflow
├── src/
│   ├── __init__.py
│   └── calculator.py       # Aplikasi utama
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Unit tests
├── .flake8                 # Konfigurasi linting
├── .gitignore             # Git ignore rules
├── pyproject.toml         # Konfigurasi modern Python
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
└── README.md             # Dokumentasi ini
```

## 🔄 Fitur CI/CD

### Continuous Integration (CI)
- **Automated Testing**: Unit tests dengan pytest
- **Code Coverage**: Laporan coverage dengan pytest-cov
- **Code Quality**: Linting dengan flake8
- **Code Formatting**: Format checking dengan black
- **Security Scanning**: Vulnerability scanning dengan bandit dan safety
- **Multi-Python Support**: Testing di Python 3.8, 3.9, 3.10, 3.11
- **Dependency Caching**: Mempercepat build dengan cache

### Continuous Deployment (CD)
- **Staging Deployment**: Otomatis deploy ke staging
- **Production Deployment**: Deploy ke production dengan approval
- **Smoke Testing**: Testing dasar setelah deployment
- **Deployment Notifications**: Notifikasi status deployment

## 🚀 Cara Menjalankan

### 1. Setup Environment
```bash
# Clone atau download proyek ini
cd "CICD examples"

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi
```bash
python src/calculator.py
```

## 🧪 Cara Menguji

### 1. Unit Tests
```bash
# Jalankan semua tests
pytest tests/

# Jalankan tests dengan verbose output
pytest tests/ -v

# Jalankan tests dengan coverage
pytest tests/ --cov=src --cov-report=html
```

### 2. Code Quality Checks
```bash
# Linting dengan flake8
flake8 .

# Format checking dengan black
black --check .

# Format code dengan black
black .

# Security scan dengan bandit
bandit -r src/
```

### 3. Manual Testing
```bash
# Test calculator functions
python -c "
from src.calculator import Calculator
calc = Calculator()
print('Testing Calculator:')
print(f'5 + 3 = {calc.add(5, 3)}')
print(f'10 - 4 = {calc.subtract(10, 4)}')
print(f'6 * 7 = {calc.multiply(6, 7)}')
print(f'15 / 3 = {calc.divide(15, 3)}')
"
```

## ⚙️ GitHub Actions Workflows

### CI Workflow (`.github/workflows/ci.yml`)

**Trigger Events:**
- Push ke branch `main` atau `develop`
- Pull request ke branch `main`
- Manual trigger dari GitHub UI

**Jobs:**
1. **Test Job**: 
   - Multi-Python version testing (3.8, 3.9, 3.10, 3.11)
   - Unit tests dengan coverage
   - Code linting dan formatting check
   - Upload coverage reports

2. **Security Job**:
   - Security vulnerability scanning
   - Dependency security check

3. **Build Job**:
   - Package building
   - Artifact upload

### CD Workflow (`.github/workflows/cd.yml`)

**Trigger Events:**
- Release publication
- Push tag yang dimulai dengan 'v'
- Manual trigger dengan environment selection

**Jobs:**
1. **Staging Deployment**:
   - Deploy ke staging environment
   - Smoke testing
   - Deployment notification

2. **Production Deployment**:
   - Deploy ke production (dengan approval)
   - Final security check
   - Production smoke testing
   - Deployment record creation

## 📊 Cara Melihat Keberhasilan

### 1. Di GitHub Repository

#### Actions Tab
1. Buka repository di GitHub
2. Klik tab **"Actions"**
3. Lihat daftar workflow runs:
   - ✅ **Green checkmark**: Workflow berhasil
   - ❌ **Red X**: Workflow gagal
   - 🟡 **Yellow circle**: Workflow sedang berjalan

#### Workflow Details
1. Klik pada workflow run untuk melihat detail
2. Lihat status setiap job:
   - **Test and Code Quality**
   - **Security Scan** 
   - **Build Package**
3. Klik job untuk melihat log detail setiap step

#### Pull Request Checks
- Saat membuat PR, lihat **"Checks"** tab
- Semua checks harus ✅ sebelum merge
- Review coverage report dan test results

### 2. Badges di README
Tambahkan badges untuk monitoring status:

```markdown
![CI](https://github.com/username/repo/workflows/CI%20Pipeline/badge.svg)
![CD](https://github.com/username/repo/workflows/CD%20Pipeline/badge.svg)
```

### 3. Coverage Reports
- **Codecov**: Lihat coverage percentage dan trends
- **HTML Report**: Buka `htmlcov/index.html` setelah run local tests

### 4. Deployment Status
- **Staging**: Check deployment logs di Actions
- **Production**: Verify manual approval dan deployment success

### 5. Monitoring Metrics

#### Success Indicators:
- ✅ All tests passing
- ✅ Coverage > 80%
- ✅ No linting errors
- ✅ No security vulnerabilities
- ✅ Successful deployments
- ✅ Smoke tests passing

#### Failure Indicators:
- ❌ Test failures
- ❌ Coverage below threshold
- ❌ Linting/formatting errors
- ❌ Security vulnerabilities found
- ❌ Deployment failures

## 🔧 Troubleshooting

### Common Issues:

1. **Tests Failing**:
   ```bash
   # Run tests locally first
   pytest tests/ -v
   ```

2. **Linting Errors**:
   ```bash
   # Fix formatting
   black .
   # Check remaining issues
   flake8 .
   ```

3. **Import Errors**:
   - Pastikan `__init__.py` ada di setiap package
   - Check Python path di test files

4. **Workflow Failures**:
   - Check logs di GitHub Actions
   - Verify file paths dan permissions
   - Check syntax di YAML files

## 📚 Konsep CI/CD yang Didemonstrasikan

### Continuous Integration (CI):
- ✅ **Short-lived branches**: Feature branches yang cepat di-merge
- ✅ **Frequent pull requests**: PR dengan automated checks
- ✅ **Automated CI tools**: GitHub Actions workflows
- ✅ **Automated testing**: Unit tests otomatis
- ✅ **Code quality**: Linting dan formatting checks
- ✅ **Security scanning**: Vulnerability detection

### Continuous Delivery (CD):
- ✅ **Automated deployment**: Deploy otomatis ke staging
- ✅ **Production readiness**: Main branch selalu deployable
- ✅ **Environment promotion**: Staging → Production flow
- ✅ **Smoke testing**: Post-deployment verification
- ✅ **Rollback capability**: Kemampuan rollback jika gagal

## 🎓 Learning Outcomes

Setelah menggunakan proyek ini, Anda akan memahami:
1. Cara setup GitHub Actions workflows
2. Implementasi automated testing dalam CI
3. Code quality dan security scanning
4. Deployment automation dengan CD
5. Monitoring dan troubleshooting CI/CD pipelines
6. Best practices untuk DevOps workflows

---

**Dibuat untuk**: STQA Bab 12-13 DevOps CI/CD  
**Tools**: GitHub Actions, Python, pytest, flake8, black, bandit