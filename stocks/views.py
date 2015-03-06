from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from stocks.models import Stocks, DefinitionTerms
from NewStock_API import Get_Quote, Get_percent_change,Get_52_week_low, Get_52_week_high, Get_Days_high, Get_Days_low, Get_52_week_high_low, Get_days_high_low, Get_previous_close, Get_volume
from InvestopediaTermsAPI import Definition
from django.views import generic


def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = Stocks.objects.filter(symbol=query)
    else:
        # If no query was entered, simply return all objects.
        results = ""
    all_stocks = Stocks.objects.all()
    context = {'results': results, 'all_stocks': all_stocks}
    return render(request, 'stocks/search.html', context)


# def choice(request, stocks_id):
#     total_choice = DataChoice.objects.all()
#     stocks = Stocks.objects.get(id=stocks_id)
#     context = {'total_choice': total_choice, 'stocks': stocks}
#     return render(request, 'stocks/choice.html', context)


def data(request, stocks_id):
    selected_stock = Stocks.objects.get(id=stocks_id)
    # conversion from id to stock name i.e symbol
    selected_symbol = selected_stock.symbol
    # symbol's conversion to string
    strng = ""
    symbol = selected_symbol + strng
    selected_name = selected_stock.full_name
    # Getting current price definition and data
    current_price_term = DefinitionTerms.objects.get(terms='currentprice')
    current_price_in_terms = current_price_term.terms
    current_price_definition = Definition(current_price_in_terms)
    quote = Get_Quote(symbol)
    # Getting today's high definition and data
    todays_high_term = DefinitionTerms.objects.get(terms='todayshigh')
    todays_high_in_terms = todays_high_term.terms
    todays_high_definition = Definition(todays_high_in_terms)
    todays_high = Get_Days_high(symbol)
    # Getting today's low definition and data
    todays_low_term = DefinitionTerms.objects.get(terms='todayslow')
    todays_low_in_terms = todays_low_term.terms
    todays_low_definition = Definition(todays_low_in_terms)
    todays_low = Get_Days_low(symbol)
    # Getting 52 week low/high definition and data
    fifty_two_week_high_low_term = DefinitionTerms.objects.get(terms='52weekhighlow')
    fifty_two_week_high_low_in_terms = fifty_two_week_high_low_term.terms
    fifty_two_week_high_low_definition = Definition(fifty_two_week_high_low_in_terms)
    fifty_two_week_high_low = Get_52_week_high_low(symbol)
    # Getting percentage change definition and data
    percent_change_term = DefinitionTerms.objects.get(terms='price-change')
    percent_change_term_in_terms = percent_change_term.terms
    percent_change_definition = Definition(percent_change_term_in_terms)
    percent_change = Get_percent_change(symbol)
    # Getting volume definition and data
    volume_term = DefinitionTerms.objects.get(terms='volume')
    volume_term_in_terms = volume_term.terms
    volume_definition = Definition(volume_term_in_terms)
    volume = Get_volume(symbol)
    # Putting all under one dict which will be returned.
    context = {'current_price_definition': current_price_definition,
               'todays_high_definition': todays_high_definition,
               'fifty_two_week_high_low_definition': fifty_two_week_high_low_definition,
               'percent_change_definition': percent_change_definition,
               'todays_low_definition': todays_low_definition,
               'volume_definition': volume_definition,
               'todays_high': todays_high,
               'todays_low': todays_low,
               'selected_name': selected_name,
               "selected_symbol": selected_symbol,
               "quote": quote,
               "percent_change": percent_change,
               "fifty_two_week_high_low": fifty_two_week_high_low,
               "volume": volume}
    return render(request, 'stocks/data.html', context)



