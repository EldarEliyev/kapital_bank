from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from .models import KapitalBank
from .serializer import KapitalBankSerializer
from .forms import KapitalBankForm  # Form varsa əlavə elə

# --- Template Views ---

def kapital_list(request):
    kapitals = KapitalBank.objects.all()
    return render(request, 'kapital_bank/kapital_list.html', {'kapitals': kapitals})

def kapital_detail(request, pk):
    kapital = get_object_or_404(KapitalBank, pk=pk)
    return render(request, 'kapital_bank/kapital_detail.html', {'kapital': kapital})

def kapital_create(request):
    if request.method == 'POST':
        form = KapitalBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kapital_bank:kapital_list')
    else:
        form = KapitalBankForm()
    return render(request, 'kapital_bank/kapital_form.html', {'form': form})

def kapital_update(request, pk):
    kapital = get_object_or_404(KapitalBank, pk=pk)
    if request.method == 'POST':
        form = KapitalBankForm(request.POST, instance=kapital)
        if form.is_valid():
            form.save()
            return redirect('kapital_bank:kapital_detail', pk=pk)
    else:
        form = KapitalBankForm(instance=kapital)
    return render(request, 'kapital_bank/kapital_form.html', {'form': form})

def kapital_delete(request, pk):
    kapital = get_object_or_404(KapitalBank, pk=pk)
    if request.method == 'POST':
        kapital.delete()
        return redirect('kapital_bank:kapital_list')
    return render(request, 'kapital_bank/kapital_confirm_delete.html', {'kapital': kapital})

# --- API Views ---

class KapitalBankListCreateAPIView(APIView):
    def get(self, request):
        kapitals = KapitalBank.objects.all()
        serializer = KapitalBankSerializer(kapitals, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = KapitalBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class KapitalBankDetailAPIView(APIView):
    def get(self, request, pk):
        kapital = get_object_or_404(KapitalBank, pk=pk)
        serializer = KapitalBankSerializer(kapital)
        return Response(serializer.data)
    
    def put(self, request, pk):
        kapital = get_object_or_404(KapitalBank, pk=pk)
        serializer = KapitalBankSerializer(kapital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        kapital = get_object_or_404(KapitalBank, pk=pk)
        kapital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
