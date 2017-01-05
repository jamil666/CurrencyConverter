from PIL import Image
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

    AZflag = "/static/images/AZ.png"
    USflag = "/static/images/US.png"
    UKflag = "/static/images/UK.png"
    RUflag = "/static/images/RU.png"
    EUROflag = "/static/images/Euro.png"

    context = {
        "USD": str(valyuta.usd),
        "EURO": str(valyuta.euro),
        "GBP": str(valyuta.gbp),
        "RUB": str(valyuta.rub),
        "date": datetime.now(),
        "Sourceform": Sourceform,
        "Destinationform": Destinationform,
        "Value": Value,
        "Flag1": AZflag,
        "Flag2": AZflag
    }


    if request.method == 'POST':

        if Sourceform.is_valid() and Destinationform.is_valid():    # POST validation check

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "USD":
                summa = float(request.POST['input_field']) / valyuta.usd    # Convert value from AZN to USD
                summa = round(summa, 4).__str__() + " " + "$"               # Show first 4 digits after comma and + $

                context["Summa"] = summa      # Added converted value to context dictionary
                context["Flag1"] = AZflag
                context["Flag2"] = USflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "USD" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.usd    # Convert value from USD to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = USflag
                context["Flag2"] = AZflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "EURO":
                summa = float(request.POST['input_field']) / valyuta.euro   # Convert value from AZN to EURO
                summa = round(summa, 4).__str__() + " " + "€"               # Show first 4 digits after comma and + €

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = AZflag
                context["Flag2"] = EUROflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "EURO" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.euro   # Convert value from EURO to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = EUROflag
                context["Flag2"] = AZflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "GBP":
                summa = float(request.POST['input_field']) / valyuta.gbp    # Convert value from AZN to GBP
                summa = round(summa, 4).__str__() + " " + "£"               # Show first 4 digits after comma and + £

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = AZflag
                context["Flag2"] = UKflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "GBP" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) / valyuta.gbp    # Convert value from GBP to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = UKflag
                context["Flag2"] = AZflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "AZN" and request.POST['destination_choice_field'] == "RUB":
                summa = float(request.POST['input_field']) / valyuta.rub    # Convert value from AZN to RUB
                summa = round(summa, 4).__str__() + " " + "RUB"               # Show first 4 digits after comma and + $

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = AZflag
                context["Flag2"] = RUflag

                return render(request, 'page.html', context)

            if request.POST['source_choice_field'] == "RUB" and request.POST['destination_choice_field'] == "AZN":
                summa = float(request.POST['input_field']) * valyuta.rub    # Convert value from RUB to AZN
                summa = round(summa, 4).__str__() + " " + "AZN"             # Show first 4 digits after comma and + AZN

                context["Summa"] = summa  # Added converted value to context dictionary
                context["Flag1"] = RUflag
                context["Flag2"] = AZflag

                return render(request, 'page.html', context)

            return render(request, 'page.html', context)

        if request.method == 'GET':
            print(request.GET['source_choice_field'])


    return render (request, 'page.html', context)