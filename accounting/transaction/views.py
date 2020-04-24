from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core import serializers
from transaction.models import *
from .forms import TransactionAdd
from django.db.models.query import QuerySet
import datetime
from django.db.models import Sum


class TransactionView(TemplateView):
    template_name = "transaction.html"

    def get(self, request, *args, **kwargs):
        context = super(TransactionView, self).get_context_data(**kwargs)
        transactions = Transaction.objects.all()
        context['transactions'] = transactions
        context['sum_kari'] = Transaction.objects.values('subject_kari').annotate(total_amount=Sum('amount'))
        context['sum_kasi'] = Transaction.objects.values('subject_kasi').annotate(total_amount=Sum('amount'))
        context['form'] = TransactionAdd()
        # Transaction.objects.all().delete()
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        obj = Transaction()
        obj.update_timestamp = datetime.datetime.now()
        if request.POST['transaction_category'] == 'buy':
            obj.subject_kari = '商品'
            obj.subject_kasi = '買掛金'
        elif request.POST['transaction_category'] == 'borrow':
            obj.subject_kari = '普通預金'
            obj.subject_kasi = '借入金'
        info = TransactionAdd(request.POST, instance=obj)
        info.save()


        return redirect(to='/index')
