# Environment to Deploy - Penjelasan

## 🎯 Apa itu "Environment to Deploy"?

**Environment to Deploy** adalah pilihan target environment (lingkungan) tempat aplikasi akan di-deploy saat menjalankan CD Pipeline secara manual.

## 🏗️ **Jenis Environment dalam CD Pipeline:**

### **1. Staging Environment**
- **Tujuan**: Testing environment sebelum production
- **Karakteristik**: 
  - Mirip dengan production tapi tidak live untuk users
  - Untuk testing final sebelum release
  - Safe untuk eksperimen
- **URL Example**: `https://staging.calculator-app.com`

### **2. Production Environment**  
- **Tujuan**: Live environment untuk end users
- **Karakteristik**:
  - Real application yang digunakan users
  - Requires extra security dan approval
  - Critical untuk business
- **URL Example**: `https://calculator-app.com`

## 🔄 **Kapan Muncul Pilihan Environment?**

### **Saat Manual Trigger:**
1. **GitHub → Actions → CD Pipeline**
2. **Klik "Run workflow"**
3. **Muncul dropdown "Environment to deploy":**
   ```
   Environment to deploy: [Dropdown]
   ├── staging     ← Default
   └── production  ← Requires approval
   ```

### **Saat Otomatis (Push):**
- **Tidak ada pilihan** - otomatis deploy ke staging dulu
- **Production** hanya jika ada release

## 📋 **Workflow Logic di CD Pipeline:**

### **Jika Pilih "staging":**
```yaml
Jobs yang berjalan:
✅ deploy-staging     # Deploy ke staging
❌ deploy-production  # SKIP - tidak berjalan
```

### **Jika Pilih "production":**
```yaml
Jobs yang berjalan:
✅ deploy-staging     # Deploy ke staging dulu
✅ deploy-production  # Lanjut ke production
```

## 🛠️ **Konfigurasi di cd.yml:**

### **Input Definition:**
```yaml
workflow_dispatch:
  inputs:
    environment:
      description: 'Environment to deploy'
      required: true
      default: 'staging'        # Default pilihan
      type: choice
      options:
      - staging                 # Pilihan 1
      - production             # Pilihan 2
```

### **Job Conditions:**
```yaml
# Job 1: Selalu berjalan
deploy-staging:
  name: Deploy to Staging
  runs-on: ubuntu-latest

# Job 2: Conditional - hanya jika pilih production
deploy-production:
  name: Deploy to Production
  needs: deploy-staging
  if: github.event.inputs.environment == 'production'
```

## 🎯 **Praktik dalam Real World:**

### **Development Flow:**
```
Developer Code → CI Testing → Staging Deploy → Production Deploy
                    ↓              ↓              ↓
                 Unit Tests    Integration    Live Users
                              Testing
```

### **Environment Promotion:**
```
Local → Staging → Production
  ↓       ↓         ↓
 Dev    Testing   Live App
```

## 🚀 **Cara Menggunakan:**

### **Untuk Testing (Pilih Staging):**
1. **Actions → CD Pipeline → Run workflow**
2. **Environment: staging**
3. **Run workflow**
4. **Hasil**: Deploy ke staging environment saja

### **Untuk Release (Pilih Production):**
1. **Actions → CD Pipeline → Run workflow**  
2. **Environment: production**
3. **Run workflow**
4. **Hasil**: Deploy ke staging → lanjut production

## 🔒 **Security & Approval:**

### **Staging Environment:**
- **No approval needed** - otomatis deploy
- **Safe untuk testing**

### **Production Environment:**
- **Manual approval required** (bisa diset di GitHub)
- **Extra security checks**
- **Deployment notifications**

## 💡 **Dalam Proyek Calculator Demo:**

### **Staging Deployment:**
```bash
echo "🚀 Deploying to staging environment..."
echo "📍 Staging URL: https://staging.calculator-app.com"
```

### **Production Deployment:**
```bash
echo "🚀 Deploying to production environment..."  
echo "📍 Production URL: https://calculator-app.com"
```

**Note**: Ini adalah simulasi - dalam real project akan ada actual deployment commands.

## 🎓 **Key Takeaways:**

1. **Environment** = Target tempat deploy aplikasi
2. **Staging** = Testing environment (safe)
3. **Production** = Live environment (critical)
4. **Manual Choice** = Flexibility untuk pilih target
5. **Automated Flow** = Staging → Production progression

## 📊 **Summary:**

| Environment | Purpose | Risk Level | Approval | Users |
|-------------|---------|------------|----------|-------|
| Staging | Testing | Low | No | Developers |
| Production | Live App | High | Yes | End Users |

**Environment to Deploy** memberikan control untuk memilih apakah ingin deploy ke testing environment (staging) atau live environment (production) saat menjalankan CD pipeline secara manual.