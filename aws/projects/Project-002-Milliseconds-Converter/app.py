from flask import Flask, render_template, request

app = Flask(__name__)

# write a function that converts the given milliseconds into hours, minutes, and seconds
def convert(milliseconds):
    # one hour in milliseconds
    hour_in_milliseconds = 60*60*1000
    # calculate the hours within given milliseconds
    hours = milliseconds // hour_in_milliseconds
    # calculate milliseconds left over when hours subtracted
    milliseconds_left = milliseconds % hour_in_milliseconds
    # one minute in milliseconds
    minutes_in_milliseconds = 60*1000
    # calculate the minutes within remainder milliseconds
    minutes = milliseconds_left // minutes_in_milliseconds
    # calculate milliseconds left over when minutes subtracted
    milliseconds_left %= minutes_in_milliseconds
    # calculate the seconds within remainder milliseconds
    seconds = milliseconds_left // 1000
    # format the output string
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)
    

@app.route('/', methods=['POST','GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']     # degerler dictionary olarak geliyor dedi o yuzden key i aliyoz [number] ile
        if not alpha.isdecimal():
            return render_template('index.html', not_valid=True,developer_name='Abdullah')
        number=int(alpha)
        if number < 1:
            return render_template('index.html', not_valid=True,developer_name='Abdullah')
        return render_template('result.html', developer_name='Abdullah', milliseconds=number, result=convert(number))
    else:
        return render_template('index.html',not_valid = False, develeoper_name='Abdullah') 



if __name__=='__main__':
    app.run(debug=True)                         #This for if we run it on web localhost
    #app.run(host='0.0.0.0',port=80)            #This is for if we run on AWS