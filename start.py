from collections import Counter
from itertools import chain
import copy
# Already reported as meetings, small tasks, company events, etc.
weekMeetingsInHours = [["1.Mar", 8], ["4.Mar", 2], ["5.Mar", 0.5], ["6.Mar", 2.5], ["7.Mar", 0.5],
["8.Mar", 1.5], ["11.Mar", 2], ["12.Mar", 3], ["13.Mar", 7], ["14.Mar", 1.5],
["15.Mar", 0.5], ["18.Mar", 2], ["19.Mar", 0.5], ["20.Mar", 0.5], ["21.Mar", 0.5],
["22.Mar", 0.5], ["25.Mar", 2], ["26.Mar", 3], ["27.Mar", 3], ["28.Mar", 0.5], ["29.Mar", 0.5]]

print ("Already reported for each day,(hours)", weekMeetingsInHours)

halfHoursForWork = []
for wf in weekMeetingsInHours:
   halfHoursForWork.append((8 - wf[1])*2)

# Logging purposes only: ######
logHours = []
for p in halfHoursForWork:
   logHours.append(str(p/2)+"h")
print ("Time slots for each day,(hours)", logHours)
###############################


halfHourParts = sum(halfHoursForWork)

print("Total time to report:", halfHourParts/2, "hours")

tasks = ["JIRA-577", "JIRA-468", "JIRA-287", "JIRA-255", "JIRA-255", "JIRA-287", "JIRA-137", "JIRA-534", "JIRA-137", "JIRA-287", "JIRA-708", "JIRA-709", "JIRA-714", "JIRA-709", "JIRA-709"]

tasksCount = tasks.__len__()

# Tasks for processing:
print ("Jiras count:", tasksCount, tasks)

# Time reporting integer parts calculation (extra piece for last task):
equalPartsCount = halfHourParts // tasksCount # int division
lastTaskExtra = 0
if (equalPartsCount * tasksCount) < halfHourParts:
   lastTaskExtra = halfHourParts - (equalPartsCount * tasksCount)

halfHoursToFill = []
i = 0;
for t in tasks:
   i = i+1
   if i==tasksCount:
       halfHoursToFill.append([t, equalPartsCount + lastTaskExtra])
   else:
       halfHoursToFill.append([t, equalPartsCount])

# Logging purposes only:
hoursToFill = copy.deepcopy(halfHoursToFill)
for p in hoursToFill:
   p[1] = str(p[1]/2)+"h"
print ("Need to report for each task, in total (hours)", hoursToFill)


halfHoursToFillQueue = []

for hhtf in halfHoursToFill:
   for i in range(1, int(hhtf[1]+1)):
       halfHoursToFillQueue.append([hhtf[0], 1])


print ("\nReporing proposal, in minutes:")

grouped = {}

while halfHoursForWork.__len__()>0:
   dayInfo = weekMeetingsInHours.pop(0)[0]

   currentTimeSlot = halfHoursForWork.pop(0)
   filledslot = []
   for i in range (1, int(currentTimeSlot+1)):
       if halfHoursToFillQueue.__len__()>0:
           filledslot.append(halfHoursToFillQueue.pop(0)[0])
   dayAndReportTime = [ [dayInfo, filledslot] ]

   for day, iss in dayAndReportTime:
       c = Counter(chain(iss))
       for k, v in c.items():
           print(day, "==>", k, str(v*30)+"m")
           if k not in grouped:
            grouped[k] = day+", "+str(v*30)+"m"
           else:
            grouped[k] = grouped[k]+" | "+day+", "+str(v*30)+"m"
#
# For easier manual reporting, let's group by JIRAs as well...            
#
print ("====================== Grouped by JIRAs ===============================")
for k, v in grouped.items():
    print(k, v)
