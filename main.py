from os import abort

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
bookDB = [
    {
        'id': '101',
        'name': 'Harry Potter',
        'author': 'JK Rowling',
        'price': 100
    },
    {'id': '201',
     'name': 'The Davinci Code',
     'author': 'Dan Brown',
     'price': 600
     },
    {
        'id': '102',
        'name': 'Assim Falou Zaratustra',
        'author': 'Friedrich Nietzsche',
        'price': 540
    },
    {
        'id': '103',
        'name': 'Ansiedade',
        'author': 'Augusto Cury',
        'price': 230
    },
    {
        'id': '109',
        'name': 'No Seu Olhar',
        'author': 'Friedrich Nietzsche',
        'price': 600
    },
    {
        'id': '104',
        'name': 'A Hora da Estrela',
        'author': 'Augusto Cury',
        'price': 800
    },
    {
        'id': '105',
        'name': 'Fogo & Sangue',
        'author': 'George R. R. Martin',
        'price': 200
    }
]

cd_dvd = [
    {
        'title': 'Alone',
        'artist': 'Harry Potter',
        'genre': 'JK Rowling',
        'year': 2001,
        'number': 10456,
        'duration': '45 min',
        'price': 600
    },

    {'title': 'Away',
     'artist': 'Augusto Cury',
     'genre': 'JK Rowling',
     'year': 2001,
     'number': 10456,
     'duration': '45 min',
     'price': 100
     }
]

Book_Cds = bookDB + cd_dvd


# get all books and cds given artist
@app.route('/cd_dvd/cds/<artist>', methods=['GET'])
def getAll(artist):
    for bk in bookDB:
        for cds in cd_dvd:
             if (cds['artist']== artist):
                   if(bk['author']== artist):
                    return jsonify({'all':bk},{'al':cds})


# get all albums
@app.route('/cd_dvd/cd', methods=['GET'])
def getAllCds():
    return jsonify({'cds': cd_dvd})


# get cds by author
@app.route('/cd_dvd/cd/<artist>', methods=['GET'])
def getCd(artist):
    usr = [cd for cd in cd_dvd if (cd['artist'] == artist)]
    return jsonify({'cd': usr})


# DELETE a Cd given its artist
@app.route('/cd_dvd/cd/<artist>', methods=['DELETE'])
def deleteCd(artist):
    em = [cd for cd in cd_dvd if (cd['artist'] == artist)]
    if len(em) == 0:
        abort(404)

    cd_dvd.remove(em[0])
    return jsonify({'response': 'Success'})


# get cd by highest price
@app.route('/cd_dvd/cd/H', methods=['GET'])
def getCd1():
    usr1 = [cd for cd in cd_dvd if (cd['price'] > 500)]
    return jsonify({'cd': usr1})


# get cd by lowest price
@app.route('/cd_dvd/cd/L', methods=['GET'])
def getCd2():
    usr2 = [cd for cd in cd_dvd if (cd['price'] <= 500)]
    return jsonify({'cd': usr2})


# how many Cds are there
@app.route('/cd_dvd/cd/count', methods=['GET'])
def getCd3():
    count = 0
    for cd in cd_dvd:
        count = count + 1
    return jsonify({'Number of CDs avalible': count})


# -------------------BOOKS------------------------------------------------
# get all books
@app.route('/bookdb/book', methods=['GET'])
def getAllBooks():
    return jsonify({'bks': bookDB})


# get book by author
@app.route('/bookdb/book/<author>', methods=['GET'])
def getBook(author):
    usr = [bk for bk in bookDB if (bk['author'] == author)]
    return jsonify({'bk': usr})


# get book by highest price
@app.route('/bookdb/book/H', methods=['GET'])
def getBook1():
    usr1 = [bk for bk in bookDB if (bk['price'] > 500)]
    return jsonify({'bk': usr1})


# get book by lowest price
@app.route('/bookdb/book/L', methods=['GET'])
def getBook2():
    usr2 = [bk for bk in bookDB if (bk['price'] < 500)]
    return jsonify({'bk': usr2})


# how many books are there
@app.route('/bookdb/book/all', methods=['GET'])
def getBook3():
    cont = 0
    for bk in bookDB:
        cont = cont + 1
    return jsonify({'Number of books avalible': cont})


# update a book given its ID
@app.route('/bookdb/book/<bookId>', methods=['POST'])
def updateBook(bookId):
    em = [bk for bk in bookDB if (bk['id'] == bookId)]
    if 'name' in request.json:
        em[0]['name'] = request.json['name']
    if 'author' in request.json:
        em[0]['author'] = request.json['author']
    return jsonify({'bk': em[0]})


# create a new book object
@app.route('/bookdb/book', methods=['PUT'])
def createBook():
    dat = {
        'id': request.json['id'],
        'name': request.json['name'],
        'author': request.json['author'],
        'price': request.json['price']
    }
    bookDB.append(dat)
    return jsonify(dat)


# DELETE a book given its author
@app.route('/bookdb/book/<author>', methods=['DELETE'])
def deleteBook(author):
    em = [bk for bk in bookDB if (bk['author'] == author)]
    if len(em) == 0:
        abort(404)

    bookDB.remove(em[0])
    return jsonify({'response': 'Success'})


# run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
