import random
from datetime import timedelta
import datetime


class Generator(object):
    def __init__(self):
        super(Generator, self).__init__()
        print "teste"

    def IntField(self, min = 0, max = 100):
        return random.randint(min,max)

    def DateField(self,start, end):
        start = datetime.datetime.strptime(start,'%d/%m/%Y').date()
        end = datetime.datetime.strptime(end,'%d/%m/%Y').date()
        return start + timedelta(
            seconds= random.randint(0, int((end - start).total_seconds())))


if __name__ == '__main__':
    gen = Generator()
    print gen.IntField(min=400,max = 9000)
    datain = datetime.datetime(2013,12,12)
    # datetime.datetime(1990,12,12),datetime.datetime(2013,12,30)
    print gen.DateField('01/01/2000','30/12/2013')