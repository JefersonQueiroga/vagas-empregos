from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Funcao, Empresa, Vaga
from .forms import VagaFiltroForm, FuncaoForm, EmpresaForm, VagaForm


@login_required
def index(request):
    return render(request, 'vagas/index.html')


# CRUD Função
@login_required
def funcao_list(request):
    funcoes = Funcao.objects.all()
    paginator = Paginator(funcoes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vagas/funcao/funcao_list.html', {'page_obj': page_obj})


@login_required
def funcao_create(request):
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Função cadastrada com sucesso!')
            return redirect('funcao_list')
    else:
        form = FuncaoForm()
    return render(request, 'vagas/funcao/funcao_form.html', {'form': form})


@login_required
def funcao_update(request, pk):
    funcao = get_object_or_404(Funcao, pk=pk)
    if request.method == 'POST':
        form = FuncaoForm(request.POST, instance=funcao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Função atualizada com sucesso!')
            return redirect('funcao_list')
    else:
        form = FuncaoForm(instance=funcao)
    return render(request, 'vagas/funcao/funcao_form.html', {'form': form, 'funcao': funcao})


@login_required
def funcao_delete(request, pk):
    funcao = get_object_or_404(Funcao, pk=pk)
    if request.method == 'POST':
        funcao.delete()
        messages.success(request, 'Função excluída com sucesso!')
        return redirect('funcao_list')
    return render(request, 'vagas/funcao/funcao_confirm_delete.html', {'funcao': funcao})


# CRUD Empresa
@login_required
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'vagas/empresa/empresa_list.html', {'empresas': empresas})


@login_required
def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'vagas/empresa/empresa_form.html', {'form': form})


@login_required
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('empresa_list')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'vagas/empresa/empresa_form.html', {'form': form, 'empresa': empresa})


@login_required
def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('empresa_list')
    return render(request, 'vagas/empresa/empresa_confirm_delete.html', {'empresa': empresa})


# CRUD Vaga
@login_required
def vaga_list(request):
    vagas = Vaga.objects.all()

    # Inicializar formulário com dados GET
    form = VagaFiltroForm(request.GET or None)

    # Aplicar filtros se o formulário for válido
    if form.is_valid():
        descricao = form.cleaned_data.get('descricao')
        funcao = form.cleaned_data.get('funcao')
        empresa = form.cleaned_data.get('empresa')

        if descricao:
            vagas = vagas.filter(descricao_vaga__icontains=descricao)

        if funcao:
            vagas = vagas.filter(funcao=funcao)

        if empresa:
            vagas = vagas.filter(empresa=empresa)

    context = {
        'vagas': vagas,
        'form': form,
    }

    return render(request, 'vagas/vaga/vaga_list.html', context)


@login_required
def vaga_create(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga cadastrada com sucesso!')
            return redirect('vaga_list')
    else:
        form = VagaForm()
    return render(request, 'vagas/vaga/vaga_form.html', {'form': form})


@login_required
def vaga_update(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga atualizada com sucesso!')
            return redirect('vaga_list')
    else:
        form = VagaForm(instance=vaga)
    return render(request, 'vagas/vaga/vaga_form.html', {'form': form, 'vaga': vaga})


@login_required
def vaga_delete(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga excluída com sucesso!')
        return redirect('vaga_list')
    return render(request, 'vagas/vaga/vaga_confirm_delete.html', {'vaga': vaga})
