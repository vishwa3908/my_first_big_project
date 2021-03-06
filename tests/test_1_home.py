import pytest
from Config.connection import connect_mysql
from  app import myapp


class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()


    #------testing home page--------------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_1_home(self):
        response = self.tester.get("/")
        response_data = response.json
        assert response_data=="WELCOME TO SHOPPING BUDDY"
        assert response.content_type =="application/json"
        assert response.status_code==200
    