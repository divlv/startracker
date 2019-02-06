from collections import Counter
from itertools import chain
import copy
# Already reported as meetings, small tasks, company events, etc.
weekMeetingsInHours = [["12.Jan", 2], ["13.Jan", 0.5], ["14.Jan", 3], ["15.Jan", 0.5], ["16.Jan", 0.5]]
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

tasks = ["JIRA-123", "JIRA-456"]
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

