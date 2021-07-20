import streamlit as st
app=st.selectbox("Please select the APP:",("Calculator","BMI Calculator","Currency Converter"))
if app == "Calculator":

    '''
    calculator to calculate numeric operations and expression
    Add(+)
    Difference(-)
divide(/)
multiply(*).
Author:Shaik Peeramohidin
GitHub:https://github.com/sk-pm
'''
#importing  streamlit
#title to app
    st.title("Calculator")
#taking inputs
    var1 = st.number_input("Enter first value:")
    operation = st.radio("Please select one of the following operations:",("+","-","/","*"))
    var2 = st.number_input("Enter second value:")
    def ADD(a,b):
        return a+b
    def SUB(a,b):
        return a-b
    def DIV(a,b):
        return a/b
    def MUL(a,b):
        return a*b
    try:
        if( st.button("Result")):
            if operation == "+":
                result = ADD(var1,var2)
                st.success("Result of {} + {} = {} ".format(var1,var2,result))
            elif operation == "-":
                result = SUB(var1,var2)
                st.success("Result of {} - {} = {} ".format(var1,var2,result))
            elif operation == "/":
                try:
                    result = DIV(var1,var2)
                    st.success("Result of {} / {} = {} ".format(var1,var2,result))
                except:
                    st.error("Can't Divde by Zero")
            elif operation == "*":
                result = MUL(var1,var2)
                st.success("Result of {} * {} = {} ".format(var1,var2,result))

    except:
        st.text("Above fields can not be blank")
elif app=="BMI Calculator":
    '''
    Program to calculate BMI
    BMI=Weight in KG/ square of height in meters.
    1Pound(Lb)=0.453592 Kilograms(Kgs)
    Author:Shaik Peeramohidin
    GitHub:https://github.com/sk-pm
    '''
 

    # title to app
    st.title("Welcome - BMI Calculator")
    # take weight units
    weight_units = st.radio('Please Select Weight In Units:', ('Kilograms(Kgs)', 'Pounds(lbs)'))
    # weight
    try:
        weight = st.number_input("Please Enter Your Weight :")
        # convert weight pounds to Kgs
        if weight_units == 'Pounds(lbs)':
            weight = weight * 0.453592
        else:
            weight = weight * 1
    except:
        st.text("Above field can not be blank")
    # take height units
    height_units = st.radio('Please Select Your Height Format: ', ('Centimeters', 'Meters', 'Feets', 'Inchs'))
    height = st.number_input("Please Enter Your Height :")
    # convert to meters
    # bmi fomula weight/(hight)^2
    try:
        if (height_units == 'Centimeters'):
            height = height / 100  # centimeters to meters
        elif (height_units == 'Feets'):
            height = height / 3.28  # feets to meters
        elif (height_units == 'Inchs'):
            height = height * 0.0254
        else:
            height = height * 1
    except:
        st.text("Above field can not be blank")


    def calculate_bmi(h, w):
        return w / h * h


    try:
        if (st.button('Calculate BMI')):

            bmi = calculate_bmi(height, weight)
            st.text(("You BMI is {}".format(bmi)))
            if (bmi < 16):
                st.error("You are Extremely Underweight")
            elif (bmi >= 16 and bmi < 18.5):
                st.warning("You are Underweight")
            elif (bmi >= 18.5 and bmi < 25):
                st.success("You are Heatlhy(Normal)")
            elif (bmi >= 25 and bmi < 30):
                st.success("You are Overweight")
            elif (bmi >= 30):
                st.error("You are Extremly Overweight")
    except:
        st.text("Please make sure all fields are filled")
elif app=="Currency Converter":
    '''
    APP: Curency convertor
    we are using API to get data of currency rates.
    using fixer API
    Author:Shaik Peeramohidin
    '''

    import streamlit as st
    import requests as rq

    st.title("Currency Converter:")
    a = st.selectbox(
        "Convert From Country:",
        ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF',
         'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP',
         'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD',
         'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR',
         'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
         'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK',
         'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR',
         'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG',
         'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
         'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD',
         'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL')
    )

    b = st.selectbox(
        "Convert To Country:",
        ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF',
         'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP',
         'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD',
         'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR',
         'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
         'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK',
         'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR',
         'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG',
         'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
         'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD',
         'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL')
    )

    url = "http://api.currencylayer.com/live?access_key=7b90e2401553ed07fad9b3e08d2cae6f&currencies=" + a + "," + b + "&format=1"
    data = rq.get(url).json()
    print(data)
    from_Country = data['quotes']['USD' + a]
    to_Country = data['quotes']['USD' + b]
    one_from_country_value = to_Country / from_Country
    c = st.number_input("Enter The Amount You Need To Convert From " + a + " to" + b + " :")
    res = round(c * one_from_country_value, 4)
    if (st.button("Convert")):
        st.success("{} ".format(res) + b)

