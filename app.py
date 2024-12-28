# Import library yang diperlukan dari Flask
from flask import Flask, redirect, url_for, request, render_template
# Membuat instance/objek Flask
app = Flask(__name__)

# Route untuk homepage (127.0.0.1:5000/)
@app.route('/')  
def home():
    # Ketika user mengakses homepage, tampilkan halaman login.html
    return render_template('login.html')

# Route untuk halaman success dengan parameter dinamis 'name'
@app.route('/success/<name>')
def success(name):
    # Menampilkan pesan selamat datang dengan nama yang diinput
    # Parameter name akan diambil dari URL (contoh: /success/John)
    return f'<h1>Selamat Datang {name}</h1>'

# Route untuk halaman login dengan method POST dan GET
@app.route('/login', methods=['POST', 'GET'])
def login():
    # Cek method request yang diterima
    if request.method == 'POST':
        # Jika POST (form disubmit):
        # Ambil nilai dari input field dengan name='nm'
        user = request.form['nm']
        # Redirect ke halaman success dengan parameter name=user
        return redirect(url_for('success', name=user))
    else:
        # Jika GET (akses halaman pertama kali):
        # Tampilkan halaman login.html
        return render_template('login.html')

# Cek apakah file ini dijalankan langsung (bukan di-import)
if __name__ == '__main__':
    # Jalankan aplikasi Flask dengan mode debug
    app.run(debug=True)