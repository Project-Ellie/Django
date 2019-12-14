from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home_page_view(request):
    logger.info("Receiving request from user %s" % request.user)
    return HttpResponse("Hello Wolfie")
