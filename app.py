from flask import Flask,render_template,request
app = Flask(__name__)

#from subprocess import call
import savedb
import json

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/insertdata", methods = ['POST'])
def insertdata():
   formdata = request.form.to_dict()
   User_name = formdata['User']
   Date = formdata['Date']
   Counter = formdata['counter']
   counter_int = int(Counter)
   Create_row = {} 
   Task_dict ={}
   for i in range(counter_int):
      Task_dict['Task_'+str(i)] = [
                              formdata['text_'+str(i)+'_P'],
                              formdata['text_'+str(i)+'_T'],
                              formdata['text_'+str(i)+'_H']
                              ]
   Create_row = {
                "User":User_name,
                "Date":Date,
                "Task_dts":Task_dict
                } 
     
    #print("The timesheet has been updated for the date " + Date +" by "+User_name+".")
   #print(" The 2nd project, hours and task: "+Project_1+", "+Hours_1+" ,"+Task_1)
   print("The counter value is "+Counter)
   #print(" the value of P,T,H are "+Project+","+Task+","+Hours)
   print("The task dict is: ")
   for i in range(counter_int):
    print(Task_dict['Task_'+str(i)])
   print("The create row is ")
   print(Create_row)
   print("The specified values :")
   print(Create_row['Task_dts']['Task_0'])
   
   savedb.insert_row(Create_row)

   return render_template('submit.html')

@app.route("/find", methods = ['GET'])
def find():
    User_name = request.args.get('User')
    Date = request.args.get('Date')
    print("The username and date from find is "+str(User_name)+" and "+str(Date))
    response = savedb.find_data(User_name,Date)
    Task_dts_list = []
    for key,value in response['document']['Task_dts'].items():
        Task_dts_list += value 
    print("The response is ")
    print(response)
    return render_template('find.html',data=response)

@app.route("/delete", methods = ['POST'])
def delete():
    formdata = request.form.to_dict()
    User_name = formdata['User']
    Date = formdata['Date']
    print("The username and date from delete is "+str(User_name)+" and "+str(Date))
    response = savedb.delete_data(User_name,Date)
    print("The response is ")
    print(response)
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug= True,port=5001)