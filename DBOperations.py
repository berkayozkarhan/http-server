import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="DboShop"
)
cursor = db.cursor()

responseMsg = {
                'sign-up-success':'Registration is successful.<a href="bootstrap-shop/index.html">Homepage</a>',
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
    passwordHash = 'hash değeriyle veritabanına kaydedilecek.'
    birthDay = fields.get('days')[0]
    birthMonth = fields.get('months')[0]
    birthYear = fields.get('years')[0]
    fullBirthday = birthDay + '.' + birthMonth + '.' + birthYear
    gender = 'TEST'
    address1 = fields.get('adress1')[0]
    address2 = fields.get('address2')[0]
    city = fields.get('city')[0]
    stateID = fields.get('state')[0]
    zipcode = fields.get('postcode')[0]
    country = fields.get('country')[0]
    additionalInfo = fields.get('aditionalInfo')[0]
    homePhone = fields.get('phone-home')[0]
    mobilePhone = fields.get('mobile-phone')[0]
    cursor = db.cursor()
    sqlRegistryControl = 'SELECT * FROM USERS WHERE EMAIL=\'{}\''.format(eMail)
    cursor.execute(sqlRegistryControl)
    result = cursor.fetchall()
    if result: #veritabanında aynı e posta mevcutsa:
        return (False,responseMsg['sign-up-failed']) #Kayıt başarısız.
    else: #veritabanında aynı e posta mevcut değilse:
        sqlRegistry = 'INSERT INTO USERS (FIRSTNAME,LASTNAME,EMAIL,PASSWORD,BIRTHDAY,GENDER,ADDRESS,ADDRESS2,' \
                      'CITY,STATE,ZIPCODE,COUNTRY,ADDITIONAL,HOMEPHONE,MOBILEPHONE)' \
                      'VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',' \
                      '\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(firstName,
                                                                                 lastName,
                                                                                 eMail,
                                                                                 password,
                                                                                 fullBirthday,
                                                                                 gender,
                                                                                 address1,
                                                                                 address2,
                                                                                 city,
                                                                                 stateID,
                                                                                 zipcode,
                                                                                 country,
                                                                                 additionalInfo,
                                                                                 homePhone,mobilePhone)
        try:
            cursor.execute(sqlRegistry)
            db.commit()
        except:
            print('ERROR:While adding new user to database.')
            return
        return (True,responseMsg['sign-up-success']) #Kayıt başarılı. Kaydetme işlemleri


def loginControl(fields): #fields --Z dictionary
    eMail = fields.get('inputEmail')[0]
    password = fields.get('inputPassword')[0]
    cursor = db.cursor()
    sqlLoginControl = 'SELECT * FROM USERS WHERE EMAIL=\'{}\' and PASSWORD=\'{}\''.format(eMail,password)
    cursor.execute()




