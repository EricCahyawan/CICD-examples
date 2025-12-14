"""
Calculator module untuk demonstrasi CI/CD
Aplikasi sederhana dengan fungsi matematika dasar
"""

class Calculator:
    """Kelas Calculator dengan operasi matematika dasar"""
    
    def add(self, a, b):
        """Menambahkan dua angka"""
        return a + b
    
    def subtract(self, a, b):
        """Mengurangi dua angka"""
        return a - b
    
    def multiply(self, a, b):
        """Mengalikan dua angka"""
        return a * b
    
    def divide(self, a, b):
        """Membagi dua angka"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Menghitung pangkat"""
        return base ** exponent

def main():
    """Fungsi utama untuk menjalankan calculator"""
    calc = Calculator()
    
    print("=== Simple Calculator ===")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")

if __name__ == "__main__":
    main()