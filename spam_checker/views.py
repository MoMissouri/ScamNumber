from django.shortcuts import render
from django.http import HttpResponse
from .scripts.functions import categorize_words, pre_process, predict


def home(request):
    input_text = request.POST.get("input_text", None)
    context = {}
    print('spam_checker', input_text)
    if input_text:
        # Text processed using script
        input_text_processed = pre_process(input_text)
        pred_text, text_colour = predict(input_text_processed)

        # Returning results
        context["result"] = pred_text
        context["color"]=text_colour
        context["input_text"]=input_text
        print('context', context )
    return render(request, "spam_checker/home.html", context=context)

