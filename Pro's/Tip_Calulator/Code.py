'''
Tip calculator algo:
1. input bill price(cost) and number of person's
2. default indian tip percentage 10%
3. convert tip percentage tp fractional
4. multiply fractional value to bill
5. add tip to actual bill price
'''

from flask import render_template, Flask, request
from sympy import content
app=Flask(__name__)

@app.route("/",methods=['POST'])
def main_page():
    return "content.html"

if "__main__" == __name__:
    app.run()
tipPercetage=10
cost=2600

# To find tipPercentage fractional value
tip_frac=tipPercetage/100

# multiply bill cost by fractional value
tip=cost*tip_frac

# add tip to actual bill
total_bill=cost+tip

# print(round(total_bill))