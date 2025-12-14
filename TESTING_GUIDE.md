# Panduan Testing CI/CD - Sesuai Materi Bab 12-13

## 🎯 Apa yang Diuji dalam CI/CD

### **CI (Continuous Integration) Testing:**
1. **Unit Tests** - Test semua fungsi calculator
2. **Integration Tests** - Test import dan module compatibility  
3. **Build Tests** - Test aplikasi bisa dijalankan

### **CD (Continuous Deployment) Testing:**
1. **Deployment Process** - Simulasi deployment ke staging/production
2. **Smoke Tests** - Test dasar setelah deployment
3. **Environment Validation** - Test aplikasi di environment target

## 🚀 Cara Menjalankan Testing

### **1. Automatic Testing (Recommended)**

#### **A. Push ke Main Branch**
```bash
# Dari folder CICD examples
git add .
git commit -m "Test CI/CD pipeline"
git push origin main
```
**Yang Terjadi:**
- ✅ Simple CI berjalan otomatis
- ✅ CD Pipeline berjalan otomatis
- ✅ Lihat hasil di Actions tab

#### **B. Pull Request Testing**
```bash
# Buat branch untuk testing
git checkout -b test-feature

# Edit src/calculator.py - tambah fungsi:
# def square(self, a):
#     return a * a

# Edit tests/test_calculator.py - tambah test:
# def test_square(self):
#     self.assertEqual(self.calc.square(4), 16)

# Commit dan push
git add .
git commit -m "Add square function"
git push origin test-feature

# Buat PR di GitHub
```
**Yang Terjadi:**
- ✅ Simple CI berjalan untuk PR
- ✅ Test new feature sebelum merge
- ✅ Code review process

### **2. Manual Testing**

#### **Manual Trigger di GitHub:**
1. **GitHub repository → Actions tab**
2. **Pilih "Simple CI" atau "CD Pipeline"**
3. **Klik "Run workflow"**
4. **Select branch: main**
5. **Klik "Run workflow"**

#### **Release Testing:**
1. **GitHub → Releases → "Create a new release"**
2. **Tag: v1.0.0**
3. **Title: "Test Release"**
4. **Publish release**
5. **CD Pipeline otomatis berjalan**

## 📊 Apa yang Ditest di Setiap Workflow

### **Simple CI Workflow (`simple-ci.yml`):**

#### **Test Steps:**
1. **Setup Environment**
   ```yaml
   - Set up Python 3.10
   - Install dependencies (pytest)
   ```

2. **Import Testing**
   ```yaml
   - Test import: from src.calculator import Calculator
   - Test basic functionality: calc.add(2,3)
   ```

3. **Unit Testing**
   ```yaml
   - Run: python -m pytest tests/ -v
   - Test semua fungsi calculator
   ```

4. **Application Testing**
   ```yaml
   - Run: python src/calculator.py
   - Test aplikasi bisa dijalankan
   ```

### **CD Pipeline Workflow (`cd.yml`):**

#### **Deployment Steps:**
1. **Staging Deployment**
   ```yaml
   - Deploy to staging environment
   - Run smoke tests
   - Validate deployment
   ```

2. **Production Deployment**
   ```yaml
   - Deploy to production (manual approval)
   - Final security check
   - Production smoke tests
   ```

## ✅ Cara Melihat Hasil Testing

### **Di GitHub Actions:**
1. **Actions Tab** → Lihat workflow runs
2. **Klik workflow run** → Lihat job details
3. **Klik job** → Lihat step-by-step logs
4. **Green ✅** = Success, **Red ❌** = Failed

### **Success Indicators:**
```
✅ Simple CI
  ✅ Set up Python
  ✅ Install dependencies
  ✅ Test import
  ✅ Run tests
  ✅ Test calculator functions

✅ CD Pipeline  
  ✅ Deploy to staging
  ✅ Run smoke tests
  ✅ Deploy to production
```

### **Failure Indicators:**
```
❌ Simple CI
  ✅ Set up Python
  ✅ Install dependencies
  ❌ Run tests
    FAILED tests/test_calculator.py::test_add
```

## 🔧 Troubleshooting

### **Jika CI Gagal:**
1. **Klik job yang gagal**
2. **Lihat error message**
3. **Fix di local:**
   ```bash
   python -m pytest tests/ -v
   python src/calculator.py
   ```
4. **Push fix:**
   ```bash
   git add .
   git commit -m "Fix CI issues"
   git push origin main
   ```

### **Common Issues:**
- **Import Error**: Check file structure
- **Test Failure**: Check test logic
- **Syntax Error**: Check Python syntax

## 🎓 Learning Objectives

### **CI Concepts Tested:**
- ✅ **Automated Testing**: Tests run otomatis
- ✅ **Fast Feedback**: Quick notification jika ada error
- ✅ **Integration**: Code dari berbagai developer terintegrasi
- ✅ **Quality Gates**: Code harus pass tests sebelum merge

### **CD Concepts Tested:**
- ✅ **Automated Deployment**: Deploy otomatis ke staging
- ✅ **Environment Promotion**: Staging → Production
- ✅ **Smoke Testing**: Basic validation setelah deploy
- ✅ **Rollback Capability**: Bisa rollback jika gagal

## 📝 Testing Checklist

### **Before Push:**
- [ ] Test local: `python -m pytest tests/`
- [ ] Run app: `python src/calculator.py`
- [ ] Check imports: `python -c "from src.calculator import Calculator"`

### **After Push:**
- [ ] Check Actions tab
- [ ] Verify all jobs ✅
- [ ] Review logs jika ada ❌
- [ ] Fix issues dan push ulang

### **For PR:**
- [ ] Create feature branch
- [ ] Add tests untuk new features
- [ ] Verify CI passes
- [ ] Merge setelah review

## 🎯 Key Takeaways

1. **CI/CD Testing** memastikan code quality dan deployment reliability
2. **Automated Testing** memberikan fast feedback untuk developers
3. **Multiple Trigger Methods** memberikan flexibility dalam testing
4. **Proper Monitoring** membantu identify dan fix issues quickly
5. **Integration dengan Git Workflow** mendukung collaborative development