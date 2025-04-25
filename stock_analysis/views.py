from django.shortcuts import render
from dal import autocomplete

from .models import Stock
from .forms import StockForm
from .utils import scrape_stock_data


def stocks(request):
    
    if request.method == "POST":
        
        form = StockForm(request.POST)
        if form.is_valid(): 
            stock_id = request.POST.get("stock")
            stock = Stock.objects.get(pk=stock_id)
            symbol = stock.symbol
            exchange = stock.exchange

            stock_response = scrape_stock_data(symbol, exchange)

            print("*" * 40)
            print(stock_response)
        else:
            print("The form is not valid.")
    else:
        form = StockForm()

        context = {
            "form": form
        }

        return render(request, "stock_analysis/stocks.html", context)



class StockAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):

        qs = Stock.objects.all()

        if self.q:

            qs = qs.filter(name__istartswith=self.q)

        return qs
    
    def get_result_label(self, result):
        return result.name