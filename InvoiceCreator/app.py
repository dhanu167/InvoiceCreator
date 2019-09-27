from flask import Flask,request,render_template, flash, redirect, url_for, session
from wtforms import Form, StringField, TextAreaField, validators, widgets, IntegerField, SelectField
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

class StateList:
    with open('list_of_state.csv','r') as state:
        read = csv.reader(state)
        state_pair = map(tuple,read)

class InvoiceForm(Form):
    state_list = [StateList]
    InvoiceNumber = IntegerField('Invoice Number', [validators.length(min=1,max=5)])
    InvoiceDate = StringField('Invoice Date',widget = widgets.Input(input_type="date"))
    State = SelectField('State',choices=state_list )
    TransportMode = SelectField('Transport Mode', choices=[('Road','Road'),('Air','Air')])
    VehicleNumber = StringField('Vehicle Number')

@app.route('/Form',methods = ['GET','POST'])
def InvoiceDetails():
    InvoiceDetailsForm  = InvoiceForm(request.form)
    if request.method == 'POST' and InvoiceDetailsForm.validate():
        InvoiceNumber = InvoiceDetailsForm.InvoiceNumber.data
        InvoiceDate = InvoiceDetailsForm.InvoiceDate.data
        State = InvoiceDetailsForm.State.data
        TransportMode = InvoiceDetailsForm.TransportMode.data
        VehicleNumber = InvoiceDetailsForm.VehicleNumber.data
    return render_template('InvoiceForm.html', form = InvoiceDetailsForm)


if __name__ =='__main__':
    app.run(debug=True)
