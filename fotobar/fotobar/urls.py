from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
 from django.contrib import admin
 admin.autodiscover()

#urlpatterns = patterns('',
#    (r'^login/$', 'bar app.views.login_user'),
#)

def index(request):
	template = loader.get_template('bar app/auth.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))