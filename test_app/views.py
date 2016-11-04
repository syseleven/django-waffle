from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from waffle import flag_is_active
from waffle.decorators import waffle_flag, waffle_switch


def flag_in_view(request):
    if flag_is_active(request, 'myflag'):
        return HttpResponse('on')
    return HttpResponse('off')


def flag_in_jinja(request):
    return render(request, 'jinja/jinja.html')


def flag_in_django(request):
    c = RequestContext(request, {
        'flag_var': 'flag_var',
        'switch_var': 'switch_var',
        'sample_var': 'sample_var',
    })
    return render_to_response('django/django.html', context=c)


def no_request_context(request):
    c = Context({})
    return render_to_string('django/django_email.html', context=c)


@waffle_switch('foo')
def switched_view(request):
    return HttpResponse('foo')


@waffle_switch('!foo')
def switched_off_view(request):
    return HttpResponse('foo')


@waffle_flag('foo')
def flagged_view(request):
    return HttpResponse('foo')


@waffle_flag('!foo')
def flagged_off_view(request):
    return HttpResponse('foo')


def foo_view(request):
    return HttpResponse('redirected')


@waffle_switch('foo', redirect_to=foo_view)
def switched_view_with_valid_redirect(request):
    return HttpResponse('foo')


@waffle_switch('foo', redirect_to='foo_view')
def switched_view_with_valid_url_name(request):
    return HttpResponse('foo')


@waffle_switch('foo', redirect_to='invalid_view')
def switched_view_with_invalid_redirect(request):
    return HttpResponse('foo')


@waffle_flag('foo', redirect_to=foo_view)
def flagged_view_with_valid_redirect(request):
    return HttpResponse('foo')


@waffle_flag('foo', redirect_to='foo_view')
def flagged_view_with_valid_url_name(request):
    return HttpResponse('foo')


@waffle_flag('foo', redirect_to='invalid_view')
def flagged_view_with_invalid_redirect(request):
    return HttpResponse('foo')
