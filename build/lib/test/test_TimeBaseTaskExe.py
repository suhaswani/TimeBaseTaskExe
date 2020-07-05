from TbTe.timebasedtaskexe import TimeBaseTaskExe
from freezegun import freeze_time
import pytest

''' for timebased version'''
@freeze_time("2020-07-02 13:30:00")
def test1():
    timebase = TimeBaseTaskExe(tasktype='sms', name='Suhas',country='India', starttm='13:00:00', endtm='14:30:00')
    assert timebase.timebased() == True


@freeze_time("2020-07-02 16:30:00")
def test2():
    timebase = TimeBaseTaskExe(tasktype='email', name='Suhas',country='India', starttm='13:00:00', endtm='14:30:00')
    assert timebase.timebased() == False


@freeze_time("2020-07-02 12:30:00")
def test3():
    timebase = TimeBaseTaskExe(tasktype='call', name='Suhas',country='India', starttm='13:00:00', endtm='14:30:00')
    assert str(timebase.timebased()) == '13:00:00'


'''   For enhanced version as per Wednesday 1 july'''
@freeze_time("2020-07-01 12:00:00")
def test4():
    timebase = TimeBaseTaskExe(tasktype='email', name='Suhas',country='India', starttm='13:30:00', endtm='14:30:00')
    assert timebase.enhancedtimebased(d11='tuesday', d12='thursday') == 'thursday 13:30:00'


# as per friday 3 july
@freeze_time("2020-07-03 12:00:00")
def test5():
    timebase = TimeBaseTaskExe(tasktype='email', name='Suhas',country='India', starttm='13:30:00', endtm='14:30:00')
    assert timebase.enhancedtimebased(d11='tuesday', d12='thursday') == 'tuesday 13:30:00'


# as per Thusday 30 june
@freeze_time("2020-06-30 14:00:00")
def test6():
    timebase = TimeBaseTaskExe(tasktype='email', name='Suhas',country='India', starttm='13:30:00', endtm='14:30:00')
    assert timebase.enhancedtimebased(d11='tuesday', d12='thursday') == True

