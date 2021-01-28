from flask import Flask, jsonify,request
from datetime import date,datetime

app = Flask(__name__)

@app.route('/', methods=['POST']) 
def ProcessPayment():
    format_str1 = '%Y-%m-%d'
    today = str(date.today())
    todate = datetime.strptime(today, format_str1)
    
    data=request.get_json()
    cc=data['CreditCardNumber']
    ch=data['CardHolder']
    ex=data['ExpirationDate']
    cvv = data['SecurityCode']
    format_str = '%d/%m/%Y'
    datetime_obj = datetime.strptime(ex, format_str)
    difference = datetime_obj - todate
    difference = difference.days
    
    amount=data['Amount']
    if cc==0:
        return "Amount  cannot be null"

    if len(cc)!=16:
        return("Invalid Card Number ")

    if len(ch) == 0:
        return "Name cannot be Empty"

    if difference <= 0:
        return "Invalid Expiration Date"
    if cvv==True:
        if len(cvv) != 3 :
                return "Invalid SecurityCode"
    premiumPaymentGateway = 1
    count = 0
    try:
        if int(amount)<500:

            try:

                ExpensivePaymentGateway=1
                
                if ExpensivePaymentGateway != 0:

                	return(jsonify({
                    "result" : "Redirecting to ExpensivePaymentGateway ",
                    "status" : "200 OK ",
                    }))
                else:
                    response = jsonify({
                    "result" : "Redirecting to cheapPaymentGateway ",
                    "status" : "200 OK ",
                    })
                    return(response)

               
            except:
                pass

                
    except Exception as e:
        return("500 internal server error ")
    else:
        if int(amount)>500 and premiumPaymentGateway:
            

            response = jsonify({
            "result" : "Redirecting to premiumPaymentGateway  ",
            "status" : "200 OK ",
            })
            return(response)

        if int(amount)>500 and premiumPaymentGateway==False:
            while(count<3):
                response = jsonify({
                "result" : "Redirecting to premiumPaymentGateway  ",
                "status" : "200 OK ",
                })
                print("Retrying...")
                count = count + 1

            return "Failed!! NO premiumPaymentGateway Available "
    finally:
        if int(amount)<20:
            return(jsonify({
                "result" : "Redirecting to cheapPaymentGateway ",
                "status" : "200 OK ",
                }))
if __name__ == '__main__':
   app.run(debug=True)
                   
                   
    
