from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/', methods=[ 'GET' ])
@app.route('/<int:start>/<int:limit>', methods=[ 'GET' ])
@app.route('/<string:condition>', methods=[ 'GET' ])
@app.route('/<int:start>/<int:limit>/<string:condition>', methods=[ 'GET' ])
def UrlParam(start=0, limit=0, condition=None):
    obj = {} 
    try:
        results= [{'userId': 1, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 2, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 3, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 4, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 5, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 6, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 7, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 8, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 9, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 10, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 11, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 12, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 13, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 14, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 15, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 16, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 17, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 18, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 19, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 20, 'dryCoughCondition': 'Low', 'condition': 'moderate'}]    

        if(start != 0 and limit != 0):
            count = len(results)     
            if count < start or limit < 0:         
                abort(404)     
         
            obj['start'] = start    
            obj['limit'] = limit     
            obj['count'] = count

            # make URLs
            # make previous url
            if start == 1:
                obj['previous'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1
                url = request.host_url

                if (condition == None):
                    obj['previous'] = url + '%d/%d' % (start_copy, limit_copy)
                else:
                    obj['previous'] = url + '%d/%d/' % (start_copy, limit_copy) + condition
                
            # make next url
            if start + limit > count:
                obj['next'] = ''
            else:
                start_copy = start + limit
                url = request.host_url

                if (condition == None):
                    obj['next'] = url + '%d/%d' % (start_copy, limit)
                else:
                    obj['next'] = url + '%d/%d/' % (start_copy, limit) + condition

            # finally extract result according to bounds
            temp_results = results[(start - 1):(start - 1 + limit)]
        else:
            temp_results = results
        newList = []
        if (temp_results != None and condition != None ):
            for item in temp_results:
                if(item['condition'].lower() == str(condition).lower()):
                    newList.append(item)
            obj['result'] = newList
        else:
            obj['result'] = temp_results
    except Exception as e:
        return(str(e))
    return obj

@app.route('/urlarg', methods=[ 'GET' ])
def UrlArg():
    obj = {} 
    try:
        start = int(request.args.get('start', 0))
        limit = int(request.args.get('limit', 0))
        condition = str(request.args.get('condition', ''))

        results= [{'userId': 1, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 2, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 3, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 4, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 5, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 6, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 7, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 8, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 9, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 10, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 11, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 12, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 13, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 14, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 15, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 16, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 17, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 18, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 19, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 20, 'dryCoughCondition': 'Low', 'condition': 'moderate'}]    

        if(start != 0 and limit != 0):
            count = len(results)     
            if count < start or limit < 0:         
                abort(404)     
         
            obj['start'] = start    
            obj['limit'] = limit     
            obj['count'] = count

            # make URLs
            # make previous url
            if start == 1:
                obj['previous'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1

                #url = url_root         
                url = request.host_url
                if (condition == ''):
                    obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
                else:
                    obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy) + '&condition=' + condition
                
            # make next url
            if start + limit > count:
                obj['next'] = ''
            else:
                start_copy = start + limit
                url = request.host_url         
                #url = ''
                if (condition == ''):
                    obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
                else:
                    obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit) + '&condition=' + condition

            # finally extract result according to bounds
            temp_results = results[(start - 1):(start - 1 + limit)]
        else:
            temp_results = results
        
        newList = []
        if (temp_results != None and condition != '' ):
            for item in temp_results:
                if(item['condition'].lower() == condition.lower()):
                    newList.append(item)
            obj['result'] = newList
        else:
            obj['result'] = temp_results
        
    except Exception as e:
	    return(str(e))
    
    return obj

@app.route('/reqbody', methods=[ 'POST' ])
def ReqBody():
    obj = {} 
    try:
        body = request.get_json(force=True)
        start = int(body.get('start', 0))
        limit = int(body.get('limit', 0))
        condition = str(body.get('condition', ''))
        drycoughcondition = str(body.get('drycoughcondition', ''))

        results= [{'userId': 1, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 2, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 3, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 4, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 5, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 6, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 7, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 8, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 9, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 10, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 11, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 12, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 13, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 14, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 15, 'dryCoughCondition': 'Moderate', 'condition': 'critical'},
               {'userId': 16, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 17, 'dryCoughCondition': 'Low', 'condition': 'high'},
               {'userId': 18, 'dryCoughCondition': 'Low', 'condition': 'critical'},
               {'userId': 19, 'dryCoughCondition': 'Low', 'condition': 'low'},
               {'userId': 20, 'dryCoughCondition': 'Low', 'condition': 'moderate'}]    

        if(start != 0 and limit != 0):
            count = len(results)     
            if count < start or limit < 0:         
                abort(404)     
         
            obj['start'] = start    
            obj['limit'] = limit     
            obj['count'] = count

            # make URLs
            # make previous url
            if start == 1:
                obj['previous'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1

            # finally extract result according to bounds
            temp_results = results[(start - 1):(start - 1 + limit)]
        else:
            temp_results = results
        
        newList = []
        if (temp_results != None):
            for item in temp_results:
                if (condition != '' and drycoughcondition != ''):
                    if(item['condition'].lower() == condition.lower() and item['dryCoughCondition'].lower() == drycoughcondition.lower()):
                        newList.append(item)
                else:
                    if(item['condition'].lower() == condition.lower() or item['dryCoughCondition'].lower() == drycoughcondition.lower()):
                        newList.append(item)
                    elif(condition == '' and drycoughcondition == ''):
                        newList.append(item)
                
            obj['result'] = newList
        else:
            obj['result'] = temp_results
        
    except Exception as e:
        return(str(e))
    return obj


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

