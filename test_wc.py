from workday_calender import Calendar, Calculator
from datetime import datetime, date

def test_prep():
    """Function which creates the test objects for all tests 

    Returns:
        Preset of test object
    """
    test_calender = Calendar()
    test_calc = Calculator()
    test_calender.set_working_hours(8,16)
    test_calender.set_holiday(2004,5,27)
    test_calender.set_rec_holiday(5,17)
    return test_calender, test_calc


def test_1():
    """Test case 1 

    Values:
        Startdate: 24.05.2004 18:05
        Workdays: -5.5
        Expected result: 14.05.2004 12:00
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,18,5)
    calc.set_workdays(-5.5)
    calc.calc_new_wd(cal)   
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 14, 12, 0)

def test_2():
    """Test case 2 

    Values:
        Startdate: 24.05.2004 19:03
        Workdays: 44.723656
        Expected result: 27.07.2004 13:47
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,19,3)
    calc.set_workdays(44.723656)
    calc.calc_new_wd(cal) 
    result = cal.get_current_wd()
    assert result == datetime(2004, 7, 27, 13, 47)

def test_3():
    """Test case 3 

    Values:
        Startdate: 24.05.2004 18:03
        Workdays: -6.7470217
        Expected result: 13.05.2004 10:02
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,18,3)
    calc.set_workdays(-6.7470217)
    calc.calc_new_wd(cal) 
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 13, 10, 2)

def test_4():
    """Test case 4 

    Values:
        Startdate: 24.05.2004 08:03
        Workdays: 12.782709
        Expected result: 10.06.2004 14:18
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,8,3)
    calc.set_workdays(12.782709)
    calc.calc_new_wd(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 6, 10, 14, 18)

def test_5():
    """Test case 5 

    Values:
        Startdate: 24.05.2004 07:03
        Workdays: 8.276628
        Expected result: 04.06.2004 10:12
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(8.276628)
    calc.calc_new_wd(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 6, 4, 10, 12)

def test_calc_date_1():
    """Individual test for calc_date,

    Values:
        Startdate: 24.05.2004 07:03
        Workdays: 2.81
        Expected result: 26.05.2004
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(2.81)
    calc.calc_date(cal)
    result = cal.get_current_wd()
    assert result == date(2004, 5, 26)

def test_calc_date_2():
    """Individual test for calc_date

    Values:
        Startdate: 24.05.2004 07:03
        Workdays: -2.81
        Expected result: 20.05.2004
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(-2.81)
    calc.calc_date(cal)
    result = cal.get_current_wd()
    assert result == date(2004, 5, 20)

def test_calc_time_1():
    """Individual test for calc_time

    Values:
        Startdate: 24.05.2004 07:03
        Workdays: 0.75
        Expected result: 24.05.2004 14:00
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(0.75)
    calc.calc_time(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 24, 14, 0)

def test_calc_time_2():
    """Individual test for calc_time

    Values:
        Startdate: 24.05.2004 7:03
        Workdays: -0.75
        Expected result: 21.05.2004 10:00
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(-0.75)
    calc.calc_time(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 21, 10, 0)

def test_calc_time_3():
    """Individual test for calc_time

    Values:
        Startdate: 24.05.2004 16:03
        Workdays: -0.75
        Expected result: 24.05.2004 10:00
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,16,3)
    calc.set_workdays(-0.75)
    calc.calc_time(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 24, 10, 0)

def test_calc_time_4():
    """Individual test for calc_time

    Values:
        Startdate: 24.05.2004 7:03
        Workdays: 0.75
        Expected result: 24.05.2004 14:00
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,7,3)
    calc.set_workdays(0.75)
    calc.calc_time(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 24, 14, 0)

def test_calc_time_5():
    """Individual test for calc_time

    Values:
        Startdate: 24.05.2004 10:03
        Workdays: 0.5
        Expected result: 25.05.2004 14:03
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,10,3)
    calc.set_workdays(0.5)
    calc.calc_time(cal)
    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 24, 14, 3)

def test_calc_seq_1():
    """Test sequence independence of calc_date and calc_time

    Values:
        Startdate: 24.05.2004 10:03
        Workdays: 2.5
        Expected result: 26.05.2004 14:03
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,10,3)
    calc.set_workdays(2.5)
    calc.calc_time(cal)
    calc.calc_date(cal)

    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 26, 14, 3)

def test_calc_seq_2():
    """Test sequence independence of calc_date and calc_time

    Values:
        Startdate: 24.05.2004 10:03
        Workdays: -2.5
        Expected result: 19.05.2004 14:03
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,10,3)
    calc.set_workdays(-2.5)
    calc.calc_time(cal)
    calc.calc_date(cal)

    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 19, 14, 3)


def test_calc_seq_3():
    """Test sequence independence of calc_date and calc_time
    switched calc_time and calc_date

    Values:
        Startdate: 24.05.2004 10:03
        Workdays: -2.5
        Expected result: 19.05.2004 14:03
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,10,3)
    calc.set_workdays(-2.5)
    calc.calc_date(cal)
    calc.calc_time(cal)

    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 19, 14, 3)

def test_calc_seq_4():
    """Test sequence independence of calc_date and calc_time
    switched calc_time and calc_date

    Values:
        Startdate: 24.05.2004 10:03
        Workdays: 2.5
        Expected result: 26.05.2004 14:03
    """
    cal, calc = test_prep()
    cal.set_start_date(2004,5,24,10,3)
    calc.set_workdays(2.5)
    calc.calc_date(cal)
    calc.calc_time(cal)

    result = cal.get_current_wd()
    assert result == datetime(2004, 5, 26, 14, 3)





