Por algum motivo, o flask não estava reconhecendo quando eu utilizava uma arquivo
cujo nome não fosse wsgi.py ou app.py, mesmo usando o FLASK_APP. 
Por isso, em caso de teste, será necessário renomear os nomes dos arquivos.

Usando o app.run() no arquivo, é possível contornar esse problema.
