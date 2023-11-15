from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv


from django.template.loader import get_template
from xhtml2pdf import pisa




def base(request):
    return render(request, "base.html")


def calculate_price(cpu, ram, ssd, ssd2, usuarios, backups, windows, red, dedicada, admin):
    total_price = 0

    # Define the CSV file path
    csv_file = "theme/static/csv/prices.csv"

    if csv_file:
        # Initialize RAM, CPU, and SSD prices
        ram_price = None
        cpu_price = None
        ssd_price = None
        ssd2_price = None
        usuarios_price = None
        backups_price = None
        windows_price = 0
        red_price = None
        dedicada_price = None
        admin_price = None

        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                try:
                    row_cpu = int(row[0])
                    row_ram = int(row[2])
                    row_ssd = int(row[4])
                    row_ssd2 = int(row[13])


                    if row_ram == ram:
                        ram_price = row[3]

                    if row_cpu == cpu:
                        cpu_price = row[1]
                        windows_price = row_cpu * 5.5

                    if row_ssd == ssd:
                        ssd_price = row[5]

                    if row_ssd2 == ssd2:
                        ssd2_price = row[14]
                    
                    usuarios_price = usuarios * 4.75
                    backups_price = backups * 80
                    red_price = 25
                    dedicada_price = 18
                    

                    # If we found prices for all components, break the loop
                    if ram_price is not None and cpu_price is not None and ssd_price is not None and usuarios_price is not None and ssd2_price is not None and backups_price is not None and windows_price is not None and admin_price is not None:
                        break
                except (ValueError, IndexError):
                    # Handle invalid data in the CSV (non-numeric values or missing columns)
                    pass

        if ram_price is not None:
            total_price += float(ram_price.replace('€', '').replace(',', '.').replace(' ', '').replace('â‚¬', ''))
        if cpu_price is not None:
            total_price += float(cpu_price.replace('€', '').replace(',', '.').replace(' ', '').replace('â‚¬', ''))
        if ssd_price is not None:
            total_price += float(ssd_price.replace('€', '').replace(',', '.').replace(' ', '').replace('â‚¬', ''))
        if usuarios_price is not None:
            total_price += usuarios_price
        if ssd2_price is not None:
            total_price += float(ssd2_price.replace('€', '').replace(',', '.').replace(' ', '').replace('â‚¬', ''))
        if backups_price is not None:
            total_price += backups_price
        if windows:
            total_price += windows_price
            if admin:
                admin_price = usuarios * 50
                total_price += admin_price
        if not windows:
            if admin:
                admin_price = 200
                total_price += admin_price
        if red:
            total_price += red_price
        if dedicada:
            total_price += dedicada_price




    return total_price


@csrf_exempt
def calculate_price_view(request):
    if request.method == "POST":
        cpu = int(request.POST.get("cpu", 0))
        ram = int(request.POST.get("ram", 0))
        ssd = int(request.POST.get("ssd", 0))
        ssd2 = int(request.POST.get("ssd2", 0))
        usuarios = int(request.POST.get("usuarios", 0))
        backups = float(request.POST.get("backups", 0.0))
        windows = request.POST.get("windows") == "true"
        red = request.POST.get("red") == "true"
        dedicada = request.POST.get("dedicada") == "true"
        admin = request.POST.get("admin") == "true"



        request.session['windows'] = windows
        request.session['red'] = red
        request.session['dedicada'] = dedicada
        request.session['admin'] = admin



        total_price = calculate_price(cpu, ram, ssd, ssd2, usuarios, backups, windows, red, dedicada, admin)
        


        return HttpResponse(str(total_price))  # Convert to a string and return as plain text
    else:
        return HttpResponse('Invalid request method')


def generate_pdf(request):
    if request.method == 'POST':
        cpu = int(request.POST.get("cpu", 0))
        ram = int(request.POST.get("ram", 0))
        ssd = int(request.POST.get("ssd", 0))
        ssd2 = int(request.POST.get("ssd2", 0))
        usuarios = int(request.POST.get("usuarios", 0))
        backups = float(request.POST.get("backups", 0.0))
        

        windows = request.session.get('windows', False)
        red = request.session.get('red', False)
        dedicada = request.session.get('dedicada', False)
        admin = request.session.get('admin', False)


        
        total_price_response = calculate_price_view(request)
        total_price_content = total_price_response.content.decode('utf-8')
        total_price = float(total_price_content)

        cpu_price = calculate_price(cpu, 0, 0, 0, 0, 0, 0, 0, 0,0)
        ram_price = calculate_price(0, ram, 0, 0 ,0 ,0, 0, 0 ,0,0)
        ssd_price = calculate_price(0, 0, ssd,0 ,0 ,0, 0, 0, 0,0)
        ssd2_price = calculate_price(0, 0, 0, ssd2, 0, 0, 0, 0, 0,0)
        usuarios_price = calculate_price(0, 0, 0, 0, usuarios, 0, 0, 0, 0,0)
        backups_price = calculate_price(0, 0, 0, 0, 0 ,backups, 0, 0, 0 ,0)


        if windows:
            windows_price = cpu * 5.5
            total_price += windows_price
            if admin:
                admin_price = usuarios * 50
                total_price += admin_price
        if not windows:
            if admin:
                admin_price = 200
                total_price += admin_price

        if red:
             total_price += 25

        if dedicada:
             total_price += 18


        total_price = '{:.2f}'.format(total_price)
        
        context = {
            'cpu': cpu,
            'ram': ram,
            'ssd': ssd,
            'ssd2' : ssd2,
            'usuarios' : usuarios,
            'backups' : backups,
            'windows' : windows,
            'red' : red,
            'dedicada' : dedicada,
            'admin': admin,

            'cpu_price': cpu_price,
            'ram_price': ram_price,
            'ssd_price': ssd_price,
            'ssd2_price' : ssd2_price,
            'usuarios_price' : usuarios_price,
            'backups_price' : backups_price,
            'red_price' : 25,
            'dedicada_price' : 18,

            'total_price': total_price,
        }

        if windows:
            context['windows_price'] = windows_price
        
        if admin:
            context['admin_price'] = admin_price


        template = get_template('pdf_template.html')
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="factura.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response