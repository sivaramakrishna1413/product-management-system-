from django.shortcuts import render
from product.models import products
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
# Create your views here.


def Show_products(request):
    products_list = products.objects.all()
    context={
        'productsList':products_list,
    }
    return render (request,'pdfconvert/showinfo.html',context)



def pdf_report_create(request):
    pdf=products.objects.all()
    
    template_path = 'pdfconvert/user_printer.html'
    context = {'pdf': pdf}
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] =  'filename="ProductReport.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    