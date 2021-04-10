****************** Trello Automation  *********************

# Pre requisites
-----------------------
1. Ensure that Python 3.6.9 is installed on the Host machine.
2. Install requirements.txt file using pip3 install -r requirements.txt.
3. This test automation framework currently supports only chrome browser at this moment,enusre the cross check your chrom browser version
   and update the chromedriver.exe under trello_auto\tools.

# Executing test cases
-----------------------

Command to run :-
         1. Navigate to london_ticket_auto folder on command prompt.
         
         2. Run - pytest test_suite\test_book_london_ticket.py --html=reports\results.html

# Further Scope Of Enhancements
-------------------------------
1. Extend to support on other browse like IE,Firefox etc.
2. Parallel execution support.
3. Multiple platform execution support.
4. Sauce lab execution support.
5. Result updation to Qtest.
6. Re-try/ re-run for failed cases.
7. Screenshot capture for failed scenarios.


