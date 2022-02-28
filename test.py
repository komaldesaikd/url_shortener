import unittest
from routes import db, app
import json
  
class BasicTest(unittest.TestCase):  
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")        
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'WELCOME' in response.data)

class encodeTest(unittest.TestCase):  
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/encode")        
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/encode")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/encode")
        self.assertTrue(b'Enter URL' in response.data)

    def test_index_post(self):
        tester = app.test_client(self)
        data = {'url':'https://www.google.com/search?q=wikipedia&oq=wikip&aqs=chrome.1.69i57j0i512l4j46i512j0i512l4.3607j0j15&sourceid=chrome&ie=UTF-8'}
        response = tester.post("/encode",data=data)        
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content_post(self):
        tester = app.test_client(self)
        data = {'url':'https://www.google.com/search?q=wikipedia&oq=wikip&aqs=chrome.1.69i57j0i512l4j46i512j0i512l4.3607j0j15&sourceid=chrome&ie=UTF-8'}
        response = tester.post("/encode",data=data) 
        self.assertEqual(response.content_type,"application/json")   

    def test_index_data_post(self):
        tester = app.test_client(self)
        value = 'https://www.google.com/search?q=wikipedia&oq=wikip&aqs=chrome.1.69i57j0i512l4j46i512j0i512l4.3607j0j15&sourceid=chrome&ie=UTF-81'
        data = {'url':'https://www.google.com/search?q=wikipedia&oq=wikip&aqs=chrome.1.69i57j0i512l4j46i512j0i512l4.3607j0j15&sourceid=chrome&ie=UTF-81'}
        response = tester.post("/encode",data=data)
        response_data = response.get_data(as_text=True)  
        self.assertTrue(value in response_data) 

class decodeTest(unittest.TestCase):  
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/decode")        
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/decode")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/decode")
        self.assertTrue(b'Enter URL' in response.data)

    def test_index_post(self):
        tester = app.test_client(self)
        data = {'url':'jkllll'}
        response = tester.post("/decode",data=data)       
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content_post(self):
        tester = app.test_client(self)
        data = {'url':'jkllmm'}
        response = tester.post("/decode",data=data) 
        self.assertEqual(response.content_type,"application/json")         

    def test_index_data_post(self):
        tester = app.test_client(self)
        data_para = 'https://www.wikipedia.org/'       
        data = {'url':data_para}
        response = tester.post("/encode",data=data)
        response_data = response.get_data(as_text=True) 
        response_data = json.loads(response_data)
        value = response_data[data_para]
        data = {'url':value}
        response = tester.post("/decode",data=data)
        response_data = response.get_data(as_text=True)
        self.assertTrue(value in response_data)
        response_data = json.loads(response_data)
        self.assertEqual(data_para,response_data[value])         
           
if __name__ == '__main__':
    unittest.main()
