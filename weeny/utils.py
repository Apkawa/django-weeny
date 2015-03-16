# -*- coding: utf-8 -*-

from .models import WeenySite, WeenyURL


def generate_url(
        url=None,
        obj=None,
        site_id=None,
        weeny_url_kw=None
):
    assert any([url, obj]) or not all([url, obj]), u"only url or obj"
    if site_id:
        w_site = WeenySite.objects.get(id=site_id)
    else:
        w_site = WeenySite.objects.filter()[0]

    weeny_url_kw = weeny_url_kw or {}
    if obj:
        weeny_url_kw['content_object'] = obj
    w_url = WeenyURL(weeny_site=w_site, raw_url=url, **weeny_url_kw)
    w_url.save()

    return w_url.get_absolute_url()
