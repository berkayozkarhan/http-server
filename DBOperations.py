import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="DboShop"
)
cursor = db.cursor()

responseMsg = {
                'sign-up-success':'Registration is successful. You are redirected to the homepage.',
                'sign-up-failed':'Registration failed. Your e-mail address is already registered in the system.',
                'login-success':'Login success.',
                'login-failed':'Login failed.'
              }


def registerControl(fields):
    #field dictionary yapısında geliyor.value değerleri de 1 elemanlı listeler içeriyor.
    firstName = fields.get('firstName')[0]
    lastName = fields.get('lastName')[0]
    eMail = fields.get('eMail')[0]
    password = fields.get('password')[0]
    birthDay = fields.get('days')[0]
    birthMonth = fields.get('months')[0]
    birthYear = fields.get('years')[0]
    address1 = fields.get('adress1')[0]
    address2 = fields.get('address2')[0]
    city = fields.get('city')[0]
    stateID = fields.get('state')[0]
    postcode = fields.get('postcode')[0]
    country = fields.get('country')[0]
    additionalInfo = fields.get('aditionalInfo')[0]
    homePhone = fields.get('phone-home')[0]
    mobilePhone = fields.get('mobile-phone')[0]
    cursor = db.cursor()
    sqlUserControl = 'SELECT * FROM USERS WHERE EMAIL=\'{}\''.format(eMail)
    cursor.execute(sqlUserControl)
    result = cursor.fetchall()
    if result:
        return (False,responseMsg['sign-up-failed']) #Giriş başarısız.
    else:
        return (True,responseMsg['sign-up-success']) #Giriş başarılı.





