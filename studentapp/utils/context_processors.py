from django.contrib.gis.geoip import GeoIP


def geoip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    g = GeoIP()
    client_city = g.country_name('ip')
    return {'client_city': client_city}