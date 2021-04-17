import mysql.connector

class Bank_system:
    #Check if user exists
    def check_user(self, username, password):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT EXISTS(SELECT username FROM bank_accounts.accounts WHERE username = '{}' AND password='{}')" .format(username, password)
        mycursor.execute(query)
        query_result = str(mycursor.fetchall())

        mycursor.close()
        mydb.close()
        
        if(query_result[2] == '1'):
            return True
        else:
            return False
    
    def check_target_user(self, username):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT EXISTS(SELECT username FROM bank_accounts.accounts WHERE username = '{}')".format(username)
        mycursor.execute(query)
        query_result = str(mycursor.fetchall())

        mycursor.close()
        mydb.close()
        
        if(query_result[2] == '1'):
            return True
        else:
            return False

    
    def update_asset(self, id_accounts, withdraw):
        update_value = input('How much?')
        if(" " in update_value):
            print('Spaces are not allowed')
            self.update_asset(id_accounts, withdraw)

        operator = '+'
        if(withdraw):
            operator = '-'

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "UPDATE bank_accounts.accounts SET assets = assets {} {} WHERE id_accounts = {}" .format(operator, update_value, id_accounts)
        mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()

    
    def get_account_id(self, username, password):
        print('In get account id, username and password: {}, {}'.format(username, password))
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT id_accounts FROM bank_accounts.accounts WHERE username='{}' AND password='{}';" .format(username, password)
        print('query: ', query)
        mycursor.execute(query)
        query_result_int = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        account_id = str(query_result_int[0]).replace('(','').replace(')','').replace(',','')
     
        return account_id

    def get_target_account_id(self, username):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT id_accounts FROM bank_accounts.accounts WHERE username='{}';" .format(username)
        mycursor.execute(query)
        query_result_int = mycursor.fetchall()
        account_id = str(query_result_int[0]).replace('(','').replace(')','').replace(',','')
        mycursor.close()
        mydb.close()

        return account_id
    
    def deposit(self, account_id, amount):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "UPDATE bank_accounts.accounts SET assets = assets + {} WHERE id_accounts = {}".format(amount, account_id)
        mycursor.execute(query)
        mydb.commit()

        mycursor.close()
        mydb.close()
    
    def withdraw(self, account_id, amount):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "UPDATE bank_accounts.accounts SET assets = assets - {} WHERE id_accounts = {}".format(amount, account_id)
        mycursor.execute(query)
        mydb.commit()

        mycursor.close()
        mydb.close()
    
    def transfer_assets(self, id_account_user, id_account_target, amount):                
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "UPDATE bank_accounts.accounts SET assets = assets + {} WHERE id_accounts = {}".format(amount, id_account_target)
        mycursor.execute(query)
        mydb.commit()
        query = "UPDATE bank_accounts.accounts SET assets = assets - {} WHERE id_accounts = {}".format(amount, id_account_user)
        mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        
    def check_username(self, username):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT EXISTS(SELECT username FROM bank_accounts.accounts WHERE username = '{}')" .format(username)
        mycursor.execute(query)
        query_result = str(mycursor.fetchall())

        mycursor.close()
        mydb.close()
            
        if(query_result[2] == '1'):
            return True
        else:
            return False
    
    def add_user_to_db(self, username, password):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "INSERT INTO bank_accounts.accounts(username, password) VALUES('{}', '{}');" .format(username, password)
        mycursor.execute(query)
        mydb.commit()

        mycursor.close()
        mydb.close()
    
    def delete_account(self, account_id):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "DELETE FROM bank_accounts.accounts WHERE id_accounts = {};".format(account_id)
        mycursor.execute(query)
        mydb.commit()

        mycursor.close()
        mydb.close()

    
    def get_assets(self, account_id):
        #account_id = self.get_target_account_id(username)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
        mycursor = mydb.cursor()
        query = "SELECT assets FROM bank_accounts.accounts WHERE id_accounts = '{}'" .format(account_id)
        mycursor.execute(query)
        query_result = str(mycursor.fetchall())

        mycursor.close()
        mydb.close()

        users_assets = query_result.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(',', '')

        return users_assets
        


            
#def unit_test():
#    print(Bank_system().get_assets('user1'))

#unit_test()