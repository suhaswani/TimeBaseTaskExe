from datetime import datetime


class TimeBaseTaskExe:
    def __init__(self, tasktype, name,country, starttm, endtm):
        self.tasktype = tasktype
        self.name = name
        self.country = country
        if type(starttm) != datetime.time:
            self.starttm = (datetime.strptime(starttm, '%H:%M:%S').time())
        if type(endtm) != datetime.time:
            self.endtm = (datetime.strptime(endtm, '%H:%M:%S').time())

    def timebased(self):
        print('Your Entered Input: ')
        print(self.tasktype, self.name, self.starttm, self.endtm)
        print('Output:')
        current_time = datetime.now().time()
        if self.starttm < current_time < self.endtm:
            return True
        elif self.starttm < self.endtm < current_time:
            return False
        elif current_time < self.starttm < self.endtm:
            return self.starttm

    def enhancedtimebased(self,d11,d12):
        day_name = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        current_time = datetime.now().time()
        current_day = datetime.now().weekday()
        current_day_name = datetime.today().strftime("%A").lower()

        print('Your Entered Input: ')
        print(self.tasktype, self.name, self.starttm, self.endtm, d11, d12)
        print('Output:')
        if current_day_name == d11 or current_day_name == d12:
            if self.starttm < current_time < self.endtm:
                return True
            elif self.starttm < self.endtm < current_time:
                if current_day_name == d11:
                    return '{} {}'.format(d12, self.starttm)
                if current_day_name == d12:
                    return '{} {}'.format(d11, self.starttm)
            elif current_time < self.starttm < self.endtm:
                if current_day_name == d11:
                    return '{} {}'.format(d11, self.starttm)
                if current_day_name == d12:
                    return '{} {}'.format(d12, self.starttm)
        else:
            d1 = day_name.index(d11)
            d2 = day_name.index(d12)
            l1 = [d1, d2]
            l1.sort()
            if l1[-1] < current_day:
                return '{} {}'.format(day_name[l1[0]], self.starttm)
            else:
                for i in l1:
                    if i > current_day:
                        return '{} {}'.format(day_name[i], self.starttm)

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)

if __name__ == "__main__":

    while True:
        task = ['email', 'call', 'sms']
        TaskType = input('Enter your Task Type(Email,Call,SMS):', )
        if TaskType.lower() not in task:
            print('Please Choose your Proper Task Type')
            continue
        elif TaskType.lower() in task:
            User = input('UserName:', )
            Country = input('Country:',)
            while True:
                while True:
                    try:
                        StartTime = (datetime.strptime(input('Enter a Start time in 24Hours format as HH:MM:SS :', ), '%H:%M:%S').time())
                    except (ValueError, NameError) as msg:
                        print('Please Enter StartTime As INSTRUCTED',msg)
                        continue
                    else:
                        while True:
                            try:
                                EndTime = (datetime.strptime(input('Enter a End time in 24Hours format as HH:MM:SS : '), '%H:%M:%S').time())
                            except (ValueError, NameError) as msg:
                                print('Please Enter EndTime As INSTRUCTED',msg)
                                continue
                            else:
                                if StartTime >= EndTime:
                                    print('EndTime Should Be Greater Than StartTime')
                                    continue
                                timebase = TimeBaseTaskExe(TaskType, User,Country,StartTime.strftime("%H:%M:%S"),EndTime.strftime("%H:%M:%S"))
                                print('SELECT OPTION:\nT/t-TimeBased\nE/e-EnhancedTimeBased')
                                option = input("Please Choose Your Option As T/t OR E/e:")
                                if option == 'T' or option == 't':
                                    print(timebase.timebased())
                                    break
                                elif option == 'E' or option == 'e':
                                    while True:
                                        day_name = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
                                        print('MONDAY', 'TUESDAT', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')
                                        d11 = input('Enter 1st day for Session As Above:', ).lower()
                                        d12 = input('Enter 2nd day for Session As Above:', ).lower()
                                        if (d11 not in day_name) or (d12 not in day_name):
                                            print('Please ReEnter Days Name As Instructed ')
                                            continue
                                        elif (d11 in day_name) or (d12 in day_name):
                                            print(timebase.enhancedtimebased(d11,d12))
                                        break
                                break
                        break
                break
        break




