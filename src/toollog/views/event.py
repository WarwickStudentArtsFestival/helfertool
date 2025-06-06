from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.http import urlencode
from django.views.decorators.cache import never_cache

from helfertool.utils import nopermission
from registration.models import Event
from registration.permissions import has_access, ACCESS_EVENT_VIEW_AUDITLOGS

from ..models import LogEntry
from ..forms import EventAuditLogFilter


@login_required
@never_cache
def event_audit_log(request, event_url_name):
    event = get_object_or_404(Event, url_name=event_url_name)

    # check permission
    if not has_access(request.user, event, ACCESS_EVENT_VIEW_AUDITLOGS):
        return nopermission(request)

    # get logs for this event
    if settings.DATABASE_LOGGING:
        enabled = True
        all_logs = LogEntry.objects.filter(event=event)

        # form for filter
        form = EventAuditLogFilter(request.GET or None, event=event)
        if form.is_valid():
            # apply filters
            if form.instance.user:
                all_logs = all_logs.filter(user=form.instance.user)
            if form.instance.helper:
                all_logs = all_logs.filter(helper=form.instance.helper)
            if form.instance.message:
                all_logs = all_logs.filter(message__icontains=form.instance.message)

        # paginate
        paginator = Paginator(all_logs, 50)
        page = request.GET.get("page")
        log = paginator.get_page(page)
        paginator_search_string = "?" + urlencode(
            {
                "user": form.instance.user.pk if form.instance.user else "",
                "helper": form.instance.helper.pk if form.instance.helper else "",
                "message": form.instance.message,
            }
        )
    else:
        enabled = False
        log = None
        form = None
        paginator_search_string = ""

    # render page
    context = {
        "event": event,
        "enabled": enabled,
        "form": form,
        "log": log,
        "paginator_search_string": paginator_search_string,
    }
    return render(request, "toollog/event_audit_log.html", context)
