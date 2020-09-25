import pdb

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.user import User
import repositories.user_repository as user_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
user_repository.delete_all()

user_1 = User('Mary Berry')
user_repository.save(user_1)

user_2 = User('Paul Hollywood')
user_repository.save(user_2)

merchant_1 = Merchant('Tesco')
merchant_repository.save(merchant_1)

merchant_2 = Merchant('ASDA')
merchant_repository.save(merchant_2)

transaction_1 = Transaction(15, user_1, merchant_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(10, user_2, merchant_2)
transaction_repository.save(transaction_2)

pdb.set_trace()