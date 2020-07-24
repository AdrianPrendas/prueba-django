from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from atm.models import Transaction


@login_required
def index(request):
    logs = Transaction.objects.all()

    context = {
        "logs": logs,
        "username": request.user.username
    }

    return render(request, "index.html", context=context)

def debit(request):

    if request.method == 'POST':
        input_data = amount = int(request.POST.get('amount'))

        singular_plural = lambda x: "billete" if x==1 else "billetes"

        result = {}

        BILS = {10000, 5000, 2000}

        for b in BILS:
            if amount / b > 0:
                result[b] = int(amount / b)
                amount -= result[b] * b
            else:
                result[b] = 0

        if amount == 0:
            string = "Su dinero es "
            for k, v in result.items():
                string += f"{v} {singular_plural(v)} de {k}, "

            Transaction.objects.create(
                user=User.objects.get(id=request.user.id),
                amount=input_data
            )

            context = {
                "detail": string[:-2],
                "input": input_data,
            }

            return render(request, "debit.html", context=context)
        else:
            err = "error este cajero solo dispensa billetes de 10, 5 y 2 mil colones"
            return render(request, "debit.html", {"err": err, "input": input_data})
