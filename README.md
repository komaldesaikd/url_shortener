# url_shortener
This code has Python Backend code for URL shortener


#Steps to execute

Step 1 : Execute "routes.py" file and it will start the server  (Link : "http://127.0.0.1:5000/").

Step 2 : i-For encoding any url provide Enter original url value on get request of "http://127.0.0.1:5000/encode".

         ii-Enter submit button for post data and it will return encoded short url for respective original url in json format({original_url:short_url}). 
         
         iii-Now to fetch original web by using short url , check on get request of "http://127.0.0.1:5000/<short_url>"
         
         iv- It will redirect to original web.
         
Step 3:  i-To decode encoded short url Enter short url value on get request of "http://127.0.0.1:5000/decode".

         ii-Enter submit button for post data and it will return decoded original url for respective short url in json format({short_url:original_url}). 
         
Step 4: To test this functionality execute test.py file which has basic, encode & decode unit testcases which will provide pass results for all testcases.
        
         
         

