from django.shortcuts import render
from api.models import Temperature, Humidity, Pressure
from django.db.models import Max, Min, F
from datetime import datetime, timedelta

from chartjs.views.lines import BaseLineChartView

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class LineChartView(BaseLineChartView):
    labels = []
    max_list = []
    min_list = []
    
    
    def set_minmax(self, index, item):
        
        if item > self.max_list[index]:
            self.max_list[index] = item

        if item < self.min_list[index]:
            self.min_list[index] = item
        
    def last_seven_days(self):
        now = datetime.now()
        seven_days_ago = now - timedelta(days=7)
        
        datas = Temperature.objects.order_by('-recorded_time').filter(recorded_time__range=(seven_days_ago,now)).annotate(value=F('celsius'))
        
        for data in datas:
            weekday = datetime.weekday(data.recorded_time)
            print(str(data.recorded_time) +' = '+ str(weekday) +' '+ days[weekday])
            if days[weekday] not in self.labels:
                self.labels.append(days[weekday])
        
        self.max_list = [-100 for i in range(len(self.labels))]
        self.min_list = [9999 for i in range(len(self.labels))]

        for data in datas:
            weekday = datetime.weekday(data.recorded_time)
            idx = self.labels.index(days[weekday])
            self.set_minmax(idx, data.value)

    def get_providers(self):
        """ Return the names for the datasets. """
        return ['Max','Min']
        
    def get_labels(self):
        """ Return labels for our days. """
        return self.labels
        
    def get_data(self):
        """ Return min/max datasets to draw. """
        
        self.last_seven_days()
        
        return [self.max_list, self.min_list]

def c2f(celsius):
    return ((celsius * 9/5) +32)


def home(request):
    now = datetime.now()
    day_ago = now - timedelta(days=1)

    temp =   Temperature.objects.order_by('-recorded_time').first()
    tcount = Temperature.objects.count()
    tfirst = Temperature.objects.order_by('recorded_time').first()
    tmax = c2f(Temperature.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Max('celsius'))['celsius__max'])
    # tmax = Temperature.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Max('celsius'))
    tmin = c2f(Temperature.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Min('celsius'))['celsius__min'])

    hum  =   Humidity.objects.order_by('-recorded_time').first()
    hcount = Humidity.objects.count()
    hfirst = Humidity.objects.order_by('recorded_time').first()
    hmax = Humidity.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Max('humidity'))['humidity__max']
    hmin = Humidity.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Min('humidity'))['humidity__min']

    press =  Pressure.objects.order_by('-recorded_time').first()
    pcount = Pressure.objects.count()
    pfirst = Pressure.objects.order_by('recorded_time').first()
    pmax = Pressure.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Max('pressure'))['pressure__max']
    pmin = Pressure.objects.filter(recorded_time__range=(day_ago,now)).aggregate(Min('pressure'))['pressure__min']

    return render(request, 'home.html', {'temp': temp,
                  'hum': hum, 'press': press,
                  'temp_max': tmax, 'temp_min': tmin,
                  'hum_max': hmax, 'hum_min': hmin,
                  'press_max': pmax, 'press_min': pmin,
                  'tcount': tcount, 'tfirst': tfirst.recorded_time,
                  'hcount': hcount, 'hfirst': hfirst.recorded_time,
                  'pcount': pcount, 'pfirst': pfirst.recorded_time})
