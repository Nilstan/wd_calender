from datetime import date, datetime, timedelta
import numpy as np

class Calendar: 
    """The Calendar class is created to setup the wanted state
     in terms of startdate, holiday and office hours.
    """
    def __init__(self):
        self.workday_intervall = 8
        self.wd_start = timedelta(hours = 8)
        self.wd_end = timedelta(hours = 16)
        self.rec_holiday = {}
        self.holiday = []
        self.start_date = date(2022,1,1)
        self.start_time = timedelta(8,0)
        self.start = datetime(2022,1,1,8,0)

    def set_start_date(self, year: int, month: int, day: int, hour: int, min: int):
        """Method to set the start date in the calender

        Args:
            year (int): year of start date
            month (int): month of start date
            day (int): day of start date
            hour (int): hour of start time
            min (int): minute of start time
        """
        self.start_date = date(year, month, day)
        self.start_time = timedelta(hours = hour,minutes = min)
        self.start = datetime(year, month, day, hour, min)
        self.current_wd = self.start_date + self.start_time

        
    def get_start_date(self) -> datetime:
        """Get method to access the start date and time

        Returns:
            datetime: the current workday
        """
        return self.start

    def set_working_hours(self, wd_start: int, wd_end: int):
        """Method which sets the start and end time of the workday

        Args:
            wd_start (int): time that workday start
            wd_end (int): time that workday ends
        """
        self.workday_intervall = wd_end - wd_start
        self.wd_start = timedelta(hours = wd_start)
        self.wd_end = timedelta(hours = wd_end)


    def check_wd(self, date: date) -> bool:
        """Method which checks if the input date is a workday, by checking if 
        its a weekday and not a holiday.

        Args:
            date (date): date that is checked if its a workday or not

        Returns:
            Bool: flag to signal if it is a workday or not
        """
        if date in self.holiday or date.weekday() in [5, 6]:
            return False
        elif date.month in self.rec_holiday and date.day == self.rec_holiday[date.month]:
            return False
        return True 

    def set_rec_holiday(self, month: int, day: int):
        """Method defines recurring holidays, as it is recurring, it has no year

        Args:
            month (int): Month for the recurring holiday
            day (int): day for the recurring holiday
        """
        self.rec_holiday[month] = day
    
    def set_holiday(self, year: int, month: int, day: int):
        """Method that sets holidays

        Args:
            year (int): year of the holiday
            month (int): month of the holiday
            day (int): day of the holiday
        """
        self.holiday.append(date(year, month, day))
    
    def set_current_wd(self, wd: datetime):
        """Set method for the current workday

        Args:
            wd (datetime): the new date that is the new current workday
        """
        self.current_wd = wd
    
    def get_current_wd(self) -> datetime:
        """Get method to access the current workday

        Returns:
            datetime: the current workday
        """
        return self.current_wd
    


class Calculator:
    """The Calculator class find the end date using a Calender class which has start date and working hours defined and 
    the number of working days
    """
    def set_workdays(self, work_days: float):
        """Function which allows to set the number of workdays, 

        Args:
            work_days (float): The float number of workdays that is wanted to find end date from, 
            where the int refers to days and rest refers to percent of hours of a working day
        """
        self.wd = work_days

        
    def calc_date(self, cal: Calendar):
        """Method which calulates the change of date for the given workdays

        Args:
            cal (Calender): Object which handles all calender functions such as defining the holiday and workday start and end 
        """
        inc = np.sign(self.wd)
        current_date = cal.current_wd

        #Loop over self.wd number of workdays
        while int(self.wd) != 0:
            current_date += timedelta(days = float(inc))
            is_wd = cal.check_wd(current_date)
            if is_wd:
                self.wd -= inc
        cal.set_current_wd(current_date)

    def calc_time(self, cal: Calendar):
        """Method which calculates the change of time 

        Args:
            cal (Calender): Object which handles all calender functions such as defining the holiday and workday start and end 
        """
        
        work_days = self.wd
        #inc is used to check direction of calculation +/-
        inc = np.sign(work_days)
        current_date = cal.current_wd
        wd_intervall = cal.wd_end - cal.wd_start

        
        #Calculating the number of hours
        rest = (self.wd-int(self.wd)) * cal.workday_intervall

        #Check if there is any change in time wanted
        if rest == 0:
            return
        
        #Create change in time based of rest of workday
        hour = int(rest)
        min = int((rest%hour)*60)
        time_delta = timedelta(hours = hour, minutes = min)

        new_time = cal.start_time + time_delta

        #Check if start time is outside of working hours
        if cal.start_time > cal.wd_end:
            new_time = cal.wd_end + time_delta
        elif cal.start_time < cal.wd_start:
            new_time = cal.wd_start + time_delta

        #Check if time worked overlaps with new day
        if new_time > cal.wd_end:
            new_time = new_time - wd_intervall
            work_days += inc
        elif new_time < cal.wd_start:
            new_time = new_time + wd_intervall
            work_days += inc

        self.set_workdays(work_days)
        
        #Check if this new date is a workday or not and add new day
        self.calc_date(cal)

        #Add time to date    
        current_date = cal.get_current_wd() 
        current_date = datetime(current_date.year, current_date.month, current_date.day)
        current_date = current_date + new_time
        cal.set_current_wd(current_date)

    def calc_new_wd(self, cal: Calendar):
        """Method to calculate both date and time calculations for end date

        Args:
            cal (Calender): Object which handles all calender functions such as defining the holiday and workday start and end 
        """
        self.calc_date(cal)
        self.calc_time(cal)
        

############# RUN ##################
#Setup of workday calender 
work = Calendar()
work.set_start_date(2004,5,25,7,3)
work.set_holiday(2004,5,27)
work.set_rec_holiday(5,17)
work.set_working_hours(8,16)

#Calulator to generate end date with given number of workdays
calc = Calculator()
wd = -0.75
calc.set_workdays(wd)
calc.calc_new_wd(work)

#Print of the result
end_date = work.get_current_wd()
start_date = work.get_start_date()

print(f"The end date with {wd} number of workdays and a start date of {start_date} is: {end_date}")






    



