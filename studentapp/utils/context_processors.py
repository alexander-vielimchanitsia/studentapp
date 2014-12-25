from django.contrib.gis.geoip import GeoIP


# def get_client_ip(ip):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def geoip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    g = GeoIP()
    client_ip = ip
    client_city = g.city(ip)
    return {'client_ip': client_ip}