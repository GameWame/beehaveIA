from flask import Blueprint, request

gia= Blueprint('gia', __name__)

@gia.route('/inserisci_ape', methods=['GET', 'POST'])
def inserimento_prodotto():
    if request.method == 'POST':
        #do the magic



