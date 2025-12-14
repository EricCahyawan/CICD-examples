# Tutorial Lengkap CI/CD dengan GitHub Actions

## 🎯 Tujuan Tutorial
Tutorial ini akan memandu Anda step-by-step untuk memahami dan mengimplementasikan CI/CD menggunakan GitHub Actions.

## 📚 Prerequisite
- Git dan GitHub account
- Python 3.8+ terinstall
- Text editor (VS Code recommended)
- Basic understanding of Python dan Git

## 🚀 Step-by-Step Implementation

### Step 1: Setup Repository

1. **Buat Repository Baru di GitHub**
   ```
   Repository name: calculator-cicd-demo
   Description: CI/CD Demo untuk STQA
   Public/Private: Public
   Initialize with README: ✅
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/username/calculator-cicd-demo.git
   cd calculator-cicd-demo
   ```

3. **Copy Files dari Tutorial Ini**
   - Copy semua files dari folder "CICD examples" ke repository Anda

### Step 2: Understand the Code Structure

#### Calculator Application (`src/calculator.py`)
```python
# Aplikasi sederhana dengan 5 fungsi matematika:
- add(a, b)      # Penjumlahan
- subtract(a, b) # Pengurangan  
- multiply(a, b) # Perkalian
- divide(a, b)   # Pembagian (dengan error handling)
- power(a, b)    # Pangkat
```

#### Unit Tests (`tests/test_calculator.py`)
```python
# Test cases untuk setiap fungsi:
- test_add()      # Test penjumlahan
- test_subtract() # Test pengurangan
- test_multiply() # Test perkalian
- test_divide()   # Test pembagian + exception handling
- test_power()    # Test pangkat
```

### Step 3: Local Testing

1. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Tests Locally**
   ```bash
   # Basic test run
   pytest tests/
   
   # Verbose output
   pytest tests/ -v
   
   # With coverage
   pytest tests/ --cov=src --cov-report=html
   ```

4. **Check Code Quality**
   ```bash
   # Linting
   flake8 .
   
   # Formatting check
   black --check .
   
   # Security scan
   bandit -r src/
   ```

### Step 4: Understanding CI Workflow

#### File: `.github/workflows/ci.yml`

**Trigger Events:**
```yaml
on:
  push:
    branches: [ main, develop ]  # Auto-run saat push
  pull_request:
    branches: [ main ]           # Auto-run saat PR
  workflow_dispatch:             # Manual trigger
```

**Jobs Breakdown:**

1. **Test Job** - Multi-Python Testing
   ```yaml
   strategy:
     matrix:
       python-version: [3.8, 3.9, '3.10', '3.11']
   ```
   - Tests di 4 versi Python berbeda
   - Memastikan compatibility

2. **Steps dalam Test Job:**
   - ✅ Checkout code
   - ✅ Setup Python environment
   - ✅ Cache dependencies (speed optimization)
   - ✅ Install dependencies
   - ✅ Lint dengan flake8
   - ✅ Format check dengan black
   - ✅ Run tests dengan coverage
   - ✅ Upload coverage reports

3. **Security Job** - Vulnerability Scanning
   - Bandit: Static security analysis
   - Safety: Known vulnerability check

4. **Build Job** - Package Creation
   - Build Python package
   - Upload artifacts

### Step 5: Understanding CD Workflow

#### File: `.github/workflows/cd.yml`

**Trigger Events:**
```yaml
on:
  release:
    types: [published]    # Saat create release
  push:
    tags: ['v*']         # Saat push tag version
  workflow_dispatch:     # Manual dengan environment choice
```

**Deployment Flow:**
1. **Staging Deployment** (otomatis)
2. **Production Deployment** (dengan approval)

### Step 6: Commit dan Push

1. **Add Files**
   ```bash
   git add .
   git commit -m "Add CI/CD implementation with GitHub Actions"
   git push origin main
   ```

2. **Lihat Actions Running**
   - Buka GitHub repository
   - Klik tab "Actions"
   - Lihat CI Pipeline berjalan

### Step 7: Testing CI Pipeline

#### Test 1: Normal Push
1. Edit file `src/calculator.py` (tambah comment)
2. Commit dan push
3. Lihat CI pipeline berjalan otomatis

#### Test 2: Failing Test
1. Edit `tests/test_calculator.py`:
   ```python
   def test_add(self):
       self.assertEqual(self.calc.add(2, 3), 6)  # Wrong expected result
   ```
2. Commit dan push
3. Lihat CI pipeline gagal
4. Fix test dan push lagi

#### Test 3: Code Quality Issue
1. Edit `src/calculator.py` dengan formatting buruk:
   ```python
   def add(self,a,b):return a+b  # Bad formatting
   ```
2. Commit dan push
3. Lihat linting error di CI
4. Fix dengan `black .` dan push

#### Test 4: Pull Request
1. Buat branch baru:
   ```bash
   git checkout -b feature/new-function
   ```
2. Tambah fungsi baru di calculator
3. Tambah test untuk fungsi baru
4. Push branch dan buat PR
5. Lihat CI checks di PR

### Step 8: Testing CD Pipeline

#### Test 1: Manual Deployment
1. Di GitHub, buka Actions tab
2. Pilih "CD Pipeline"
3. Klik "Run workflow"
4. Pilih environment "staging"
5. Lihat deployment process

#### Test 2: Release Deployment
1. Buat release di GitHub:
   - Tag: v1.0.0
   - Title: "First Release"
   - Description: "Initial calculator release"
2. Publish release
3. Lihat CD pipeline berjalan otomatis

### Step 9: Monitoring dan Debugging

#### Melihat Logs
1. **Workflow Overview**:
   - Actions tab → Pilih workflow run
   - Lihat status semua jobs

2. **Job Details**:
   - Klik job name untuk detail
   - Expand steps untuk lihat logs

3. **Error Debugging**:
   - Red X = error, klik untuk detail
   - Lihat error message di logs
   - Check file paths dan syntax

#### Common Issues dan Solutions

1. **Import Error**:
   ```
   Error: ModuleNotFoundError: No module named 'src'
   ```
   **Solution**: Check `sys.path` di test files

2. **Linting Error**:
   ```
   Error: E302 expected 2 blank lines, found 1
   ```
   **Solution**: Run `black .` untuk auto-format

3. **Test Failure**:
   ```
   AssertionError: 5 != 6
   ```
   **Solution**: Check test logic dan expected values

### Step 10: Advanced Features

#### Branch Protection Rules
1. Settings → Branches
2. Add rule untuk main branch:
   - Require status checks
   - Require PR reviews
   - Dismiss stale reviews

#### Environment Protection
1. Settings → Environments
2. Buat "production" environment
3. Add protection rules:
   - Required reviewers
   - Wait timer
   - Deployment branches

#### Secrets Management
1. Settings → Secrets and variables → Actions
2. Add secrets untuk deployment:
   - `DEPLOY_TOKEN`
   - `DATABASE_URL`
   - `API_KEY`

## 🎯 Learning Checkpoints

Setelah menyelesaikan tutorial ini, Anda harus bisa:

### CI (Continuous Integration)
- ✅ Memahami trigger events (push, PR, manual)
- ✅ Setup multi-environment testing
- ✅ Implement automated testing
- ✅ Add code quality checks
- ✅ Setup security scanning
- ✅ Handle build artifacts

### CD (Continuous Deployment)
- ✅ Setup staging deployment
- ✅ Implement production deployment dengan approval
- ✅ Add smoke testing
- ✅ Handle deployment notifications
- ✅ Understand environment management

### DevOps Best Practices
- ✅ Short-lived branches
- ✅ Frequent integration
- ✅ Automated testing
- ✅ Code quality gates
- ✅ Security scanning
- ✅ Deployment automation

## 🔍 Verification Checklist

Pastikan semua ini berfungsi:

### CI Pipeline
- [ ] Tests berjalan di multiple Python versions
- [ ] Code coverage > 80%
- [ ] Linting passes (flake8)
- [ ] Formatting correct (black)
- [ ] Security scan clean (bandit)
- [ ] Build artifacts created

### CD Pipeline
- [ ] Staging deployment berhasil
- [ ] Smoke tests pass
- [ ] Production deployment dengan approval
- [ ] Deployment notifications working

### Repository Setup
- [ ] Branch protection rules active
- [ ] PR checks required
- [ ] Environment protection configured
- [ ] Secrets properly managed

## 🎉 Congratulations!

Anda telah berhasil mengimplementasikan CI/CD pipeline lengkap dengan GitHub Actions! 

Pipeline ini mengikuti best practices DevOps dan siap untuk production use.

---

**Next Steps:**
- Explore advanced GitHub Actions features
- Add more sophisticated testing (integration, e2e)
- Implement monitoring dan alerting
- Learn about infrastructure as code (IaC)