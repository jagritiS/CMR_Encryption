from urllib import response

from flask import Flask, render_template, request

from ceasar import Ceasar
from mono import Mono
from railfence import Railfence

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      plaintext = request.form['PlainText']
      #from ceasar
      encrypted_text = Ceasar.encrypt(plaintext)
      decrypted_text = Ceasar.decrypt(encrypted_text)
      #from railfence
      r_encr =Railfence.encryptRailFence(plaintext)
      r_decr = Railfence.decryptRailFence(r_encr)
      #monoalphabetic
      m_encr =Mono.encrypt(plaintext)
      m_decr = Mono.decrypt(m_encr)
      data = [plaintext,encrypted_text, decrypted_text,r_encr,r_decr,m_encr,m_decr]
      print(plaintext)
      print(encrypted_text)
      print(decrypted_text)
      return render_template("result.html",data = data)

if __name__ == '__main__':
   app.run(debug = True)
if __name__ == '__main__':
    app.run()
