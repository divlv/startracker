# StarTracker

Python script for time reporting.

* Adjust source data for already reported hours for meetings, company events, some short tasks, etc.
* Then add tasks list, you need to report "smoothly".
* Run script
* Profit!

Sample output:
```
Already reported for each day,(hours) [['12.Jan', 2], ['13.Jan', 0.5], ['14.Jan', 3], ['15.Jan', 0.5], ['16.Jan', 0.5]]
Time slots for each day,(hours) ['6.0h', '7.5h', '5.0h', '7.5h', '7.5h']
Total time to report: 33.5 hours
Jiras count: 2 ['JIRA-123', 'JIRA-456']
Need to report for each task, in total (hours) [['JIRA-123', '16.5h'], ['JIRA-456', '17.0h']]

Reporing proposal, in minutes:
12.Jan ==> JIRA-123 360m
13.Jan ==> JIRA-123 450m
14.Jan ==> JIRA-123 180m
14.Jan ==> JIRA-456 120m
15.Jan ==> JIRA-456 450m
16.Jan ==> JIRA-456 450m
```
