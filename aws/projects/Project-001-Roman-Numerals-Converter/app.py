from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i)
        decimal_num %= i 
    return num_to_roman

# Ister ustekini kullan ister bunu
#def convert_to_roman(num):
#    roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
#    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#    romanvalue = ''
#    for i,d in enumerate(number):
#        while (num >= d): 
#            num -= d
#            romanvalue += roman[i]
#    return romanvalue

@app.route('/', methods=['POST','GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']     # degerler dictionary olarak geliyor dedi o yuzden key i aliyoz [] ile
        if not alpha.isdecimal():
            return render_template('index.html', not_valid=True,developer_name='Pablo')
        number=int(alpha)
        if not 0<number<4000:
            return render_template('index.html', not_valid=True,developer_name='Pablo')
        return render_template('result.html', developer_name='Pablo', number_decimal=number,number_roman=convert(number))
            



    else:
        return render_template('index.html',not_valid = False, develeoper_name='Pablo') 








if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=80)