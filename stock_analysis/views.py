from django.shortcuts import render



def stocks(request):

    return render(request, "stock_analysis/stocks.html")