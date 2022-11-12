from django.shortcuts import redirect, render
from .models import Address_Book
from .forms import Address_BookForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Address_BookListView(ListView):
    model = Address_Book
    template_name = 'myapp/index.html'   
    context_object_name = 'address_book_list'


class Address_BookDetailView(DetailView):
    model = Address_Book
    template_name = 'myapp/detail.html'
    context_object_name = 'address_book'


class Address_BookUpdateView(UpdateView):
    model = Address_Book
    template_name = 'myapp/update.html'
    context_object_name = 'address_book'
    fields=('Name','Email','DOB','Address','Pincode')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class Address_BookDeleteView(DeleteView):
    model = Address_Book
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('cbvindex')


def index(request):
    address_book_list = Address_Book.objects.all()
    if request.method=='POST':
        Name=request.POST.get('Name','')
        Email=request.POST.get('Email','')
        DOB = request.POST.get('DOB','')
        Address = request.POST.get('Address','')
        Pincode = request.POST.get('Pincode','')

        address_book = Address_Book(Name=Name, Email=Email, DOB=DOB, Address=Address, Pincode=Pincode)
        address_book.save()
        return redirect('/')
    

    return render(request, 'myapp/index.html',{'task_list':address_book_list })

def delete(request,address_bookid):
    address_book = Address_Book.objects.get(id=address_bookid)

    if request.method=="POST":
        address_book.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html', {'task':task})

def update(request,address_bookid):
    address_book = Address_Book.objects.get(id=address_bookid)
    form = Address_BookForm(request.POST or None, instance=address_book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'address_book':address_book})
