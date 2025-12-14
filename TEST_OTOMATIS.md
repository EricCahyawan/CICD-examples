# Test Workflow Otomatis Setelah Push

## ✅ **Sekarang Sudah Fixed!**

### **Trigger Configuration:**

#### **Simple CI** (sudah benar):
```yaml
on:
  push:
    branches: [ main ]     # ✅ Otomatis saat push ke main
  pull_request:
    branches: [ main ]     # ✅ Otomatis saat PR ke main
```

#### **CD Pipeline** (sudah diperbaiki):
```yaml
on:
  push:
    branches: [ main ]     # ✅ BARU: Otomatis saat push ke main
  release:
    types: [published]     # ✅ Saat create release
```

## 🚀 **Cara Test Otomatis:**

### **Test 1: Push ke Main Branch**
```bash
# Edit file apapun (misal tambah comment)
# Di src/calculator.py tambah comment:
# This is a test comment

git add .
git commit -m "Test automatic CI/CD trigger"
git push origin main
```

**Yang Akan Terjadi:**
- ✅ **Simple CI** otomatis berjalan
- ✅ **CD Pipeline** otomatis berjalan
- ✅ Lihat di Actions tab - kedua workflow running

### **Test 2: Edit Code dan Push**
```bash
# Edit src/calculator.py - tambah fungsi:
def square(self, a):
    """Menghitung kuadrat"""
    return a * a

# Edit tests/test_calculator.py - tambah test:
def test_square(self):
    """Test fungsi square"""
    self.assertEqual(self.calc.square(4), 16)

git add .
git commit -m "Add square function"
git push origin main
```

**Yang Akan Terjadi:**
- ✅ CI test fungsi baru
- ✅ CD deploy dengan fungsi baru

## 📊 **Expected Results di Actions Tab:**

Setelah push, Anda akan melihat:
```
✅ Simple CI #X        (running/completed)
✅ CD Pipeline #X      (running/completed)
```

**Keduanya berjalan untuk commit yang sama!**

## 🔍 **Troubleshooting:**

### **Jika Masih Manual:**
1. **Check branch name** - pastikan push ke `main` (bukan `master`)
2. **Check file location** - pastikan workflow files di `.github/workflows/`
3. **Check YAML syntax** - pastikan tidak ada syntax error

### **Check Branch Name:**
```bash
# Lihat current branch
git branch

# Jika di master, rename ke main:
git branch -m master main
git push -u origin main
```

## ✅ **Verification Steps:**

1. **Edit file kecil** (tambah comment)
2. **Commit dan push** ke main
3. **Buka GitHub Actions tab**
4. **Lihat 2 workflow berjalan otomatis**
5. **Success!** 🎉

## 🎯 **Key Points:**

- **CI Pipeline**: Test code quality saat push
- **CD Pipeline**: Deploy otomatis saat push
- **No Manual Trigger**: Semuanya otomatis
- **Fast Feedback**: Langsung tahu jika ada error