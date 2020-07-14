from django.contrib.auth.decorators import login_required

from papermerge.search.backends import get_search_backend
from papermerge.core.models import Page, Folder, BaseTreeNode
from django.shortcuts import render


@login_required
def browse(request):
    return render(
        request,
        "admin/index.html"
    )


@login_required
def search(request):
    search_term = request.GET.get('q')
    backend = get_search_backend()

    results_folders = backend.search(search_term, Folder)

    results_docs = backend.search(search_term, Page)

    qs_docs = BaseTreeNode.objects.filter(
        id__in=[
            p.document.basetreenode_ptr_id for p in results_docs
        ]
    )

    return render(
        request,
        "admin/search.html",
        {
            'results_docs': qs_docs.all(),
            'results_folders': qs_docs.all()
        }
    )
