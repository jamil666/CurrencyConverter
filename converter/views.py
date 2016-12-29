from django.shortcuts import render
from.aplication import valyuta
from datetime import datetime
from .models import Currency
from .forms import ChoiceSource, ChoiceDestination, Input

def page(request):

    # Add current course from parsed site to database

    db_tables = Currency(USD=valyuta.usd,
                         EURO=valyuta.euro,
                         GBP=valyuta.gbp,
                         RUB=valyuta.rub,
                         Date=datetime.now())
    db_tables.save()    # Save values to database

    Sourceform = ChoiceSource(request.POST)             # Source choosing form
    Destinationform = ChoiceDestination(request.POST)   # Destination choosing form
    Value = Input(request.POST)                         # Value input form

################################### Calculator ##########################################

    context = {
        "USD": str(valyuta.usd),
        "EURO": str(valyuta.euro),
        "GBP": str(valyuta.gbp),
        "RUB": str(valyuta.rub),
        "date": datetime.now(),
        "Sourceform": Sourceform,
        "Destinationform": Destinationform,
        "Value": Value,
    }

    if request.method == 'POST':

        if Sourceform.is_valid() and Destinationform.is_valid():    # POST validation check

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "USD":
                summa = float(request.POST['input_field']) / valyuta.usd    # Convert value from AZN to USD
                summa = round(summa, 4).__str__() + " " + "$"               # Show first 4 digits after comma and + $

                context["Summa"] = summa      # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "USD" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.usd    # Convert value from USD to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "EURO":
                summa = float(request.POST['input_field']) / valyuta.euro   # Convert value from AZN to EURO
                summa = round(summa, 4).__str__() + " " + "€"               # Show first 4 digits after comma and + €

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "EURO" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.euro   # Convert value from EURO to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "GBP":
                summa = float(request.POST['input_field']) / valyuta.gbp    # Convert value from AZN to GBP
                summa = round(summa, 4).__str__() + " " + "£"               # Show first 4 digits after comma and + £

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "GBP" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) / valyuta.gbp    # Convert value from GBP to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "RUB":
                summa = float(request.POST['input_field']) / valyuta.rub    # Convert value from AZN to RUB
                summa = round(summa, 4).__str__() + " " + "RUB"               # Show first 4 digits after comma and + $

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "RUB" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.rub    # Convert value from RUB to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary

                return render(request, 'page.html', context)

            return render(request, 'page.html', context)

    return render (request, 'page.html', context)
