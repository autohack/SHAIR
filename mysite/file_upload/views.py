# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from file_upload.models import Document
from file_upload.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.user_name = request.session['username']
            newdoc.save()

            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('mysite.file_upload.views.list'))
            return HttpResponseRedirect('/file_upload/')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # for doc in documents1
    #     file_name = doc.docfile.name
    #     if file_name


    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form, 'username' : request.session['username']},
        context_instance=RequestContext(request)
    )
def delete(request,document_id):
    a =Document.objects.get(id=document_id)
    a.is_deleted = 1
    a.save()

    return HttpResponseRedirect('/file_upload/')
