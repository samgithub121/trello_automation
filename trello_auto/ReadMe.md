****************** Trello Automation  ******************

This is a test automation framework developed in pytest for automating trello.This framework uses two types of config fliles,
first is the .ini file where you user can do the test case/credentials related configuration.Second is a .csv file where user can
create the data set for the cards. 

# Pre requisites
-----------------------
1. Ensure that Python 3.6.9 is installed on the Host machine.
2. Install requirements.txt file using pip3 install -r requirements.txt.
3. This test automation framework currently supports only chrome browser at this moment,enusre the cross check your chrome browser version
   and update the chromedriver.exe under trello_auto\tools.

# Executing test cases
-----------------------
In this framework there are 3 ways by which you can execute test cases.First is via UI automation through selenium,second is via over headless commandline
execution and third is via REST API.
The uiconfig.ini is the config file where the test executer has to update and run accordingly.
The section exec_mode = headless / normal determines how a TC has to execute.
At the end of the execution the results will be available in HTML format under the reports folder.

Command to run :-
         -> Navigate to trello_auto folder on command prompt.
         
UI Based automation,, under the test case(test001_create_trello_card.py) mention the name of the board you wish to create card  :-    
          pytest test_suite\ui\test001_create_trello_card.py --html=reports\results.html
          
Headless Execution : In the uiconfig.ini make exec_mode=headless and under the test case(test001_create_trello_card.py) mention the name of the board you wish to create card 
          pytest test_suite\ui\test001_create_trello_card.py --html=reports\results.html
          
REST API execution for creating board, under the test case(test002_create_trello_board.py) mention the name of the board you wish to create:-
          pytest test_suite\api\test002_create_trello_board.py --html=reports\results.html
          
REST API execution for creating card, under the test case(test001_create_trello_card.py) mention the name of the board you wish to create card :-
          pytest test_suite\api\test001_create_trello_card.py --html=reports\results.html		  


# Further Scope Of Enhancements
-------------------------------
1. Extend to support on other browse like IE,Firefox etc.
2. Parallel execution support.
3. Multiple platform execution support.
4. Sauce lab execution support.
5. Result updation to Qtest.
6. Re-try/ re-run for failed cases.
7. Screenshot capture for failed scenarios.
8. Applitools integration for any image based comparisons.
9. Integration of tools such as NightwatchJS, mochajs , supertest etc.


