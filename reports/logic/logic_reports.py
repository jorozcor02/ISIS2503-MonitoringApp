from ..models import Reports 

def get_reports():
    queryset = Reports.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_report(form):
    report = form.save()
    report.save()
    return () 