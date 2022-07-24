import math
from django.conf import settings
from django.core.paginator import InvalidPage
from rest_framework import pagination
from rest_framework.response import Response
from utils.error import PageNotFound


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = settings.DEFAULT_PAGINATION_PAGE_SIZE
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        per_page = self.page.paginator.per_page
        count = self.page.paginator.count
        total_page = math.ceil(count / per_page)
        return Response({
            'page_info': {
                'current_page': self.page.number,
                'prev_page': self.get_previous_link(),
                'next_page': self.get_next_link(),
                'per_page': self.page.paginator.per_page,
                'total_page': total_page,
                'total': self.page.paginator.count,
            },
            'payload': data,
            "error": None,
            "success": True,
        })

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise PageNotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)
