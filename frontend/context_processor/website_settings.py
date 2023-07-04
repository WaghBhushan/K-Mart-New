from cms.models import WebsiteSetting

def website_settings(request):
    website_settings = WebsiteSetting.objects.all().last()
    return{ 'website_settings' : website_settings}



