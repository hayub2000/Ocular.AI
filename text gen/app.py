from flask import Flask, request
from flask_cors import CORS

from gpt_neo import Ocular_Method

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/getstory', methods=['POST'])
def get_story():
    input_string = request.json['input_string']
    print(input_string)
    response = Ocular_Method(input_string) 
    
    # ("ادرینالائن سے میری جیکٹ سے پسینہ نکلنے لگا، حتیٰ کہ منجمد ٹھنڈے میں بھی۔ کرولا میں چڑھنے سے پہلے، میں نے پیچھے کی جانب دیکھا تو ہمارے پیچھے والی شیطانی گاڑی کی جانب جھکیں۔ میں صرف دو افراد کو گاڑی کے سامنے کی سیٹوں میں بیٹھا دیکھ سکا۔ میں کوئی خصوصی نشانیاں نہیں دیکھ سکا تھا، مگر میں ان کے نظروں میں محسوس کر سکتا تھا کہ وہ مجھ پر تیز نگاہ ڈال رہے ہیں، جیسے کھانے کے لئے بے چین شیر ہیں۔")

    # Perform your calculation on the input string
    # output_string = input_string.upper()  # Example calculation: convert to uppercase
    print('return from model'+response)
    return {'output_string': response}

if __name__ == "__main__":
    app.run(debug=True)
















# from flask import Flask
# from gpt_neo import Ocular_Module
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     # response = Ocular_Method("ادرینالائن سے میری جیکٹ سے پسینہ نکلنے لگا، حتیٰ کہ منجمد ٹھنڈے میں بھی۔ کرولا میں چڑھنے سے پہلے، میں نے پیچھے کی جانب دیکھا تو ہمارے پیچھے والی شیطانی گاڑی کی جانب جھکیں۔ میں صرف دو افراد کو گاڑی کے سامنے کی سیٹوں میں بیٹھا دیکھ سکا۔ میں کوئی خصوصی نشانیاں نہیں دیکھ سکا تھا، مگر میں ان کے نظروں میں محسوس کر سکتا تھا کہ وہ مجھ پر تیز نگاہ ڈال رہے ہیں، جیسے کھانے کے لئے بے چین شیر ہیں۔")
#     # print(response);
#     return 'Hello World';


# if __name__ == "__main__":
#     app.run(debug=True)
