from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .models import Gasto

def inicio(request):
    # Pega o último cartão usado salvo na memória ou deixa 'adriana' como padrão
    ultimo_cartao = request.session.get('ultimo_cartao', 'adriana')

    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        cartao = request.POST.get('cartao')

        if descricao and valor and cartao:
            Gasto.objects.create(
                descricao=descricao,
                valor=valor,
                cartao=cartao,
                data=timezone.now().date()
            )
            # Guarda na sessão o cartão que ela acabou de usar
            request.session['ultimo_cartao'] = cartao
            return redirect('inicio')

    gastos = Gasto.objects.all().order_by('-data', '-id')

    # Totais calculados
    total_adriana = Gasto.objects.filter(cartao='adriana').aggregate(Sum('valor'))['valor__sum'] or 0
    total_cassio = Gasto.objects.filter(cartao='cassio').aggregate(Sum('valor'))['valor__sum'] or 0

    context = {
        'gastos': gastos,
        'total_adriana': total_adriana,
        'total_cassio': total_cassio,
        'ultimo_cartao': ultimo_cartao,
    }
    return render(request, 'inicio.html', context)


def excluir_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id=gasto_id)
    gasto.delete()
    return redirect('inicio')