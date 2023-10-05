from django.http import JsonResponse

def FaltaAgua(request):
    if request.method == 'GET':
        faltadeagua = {'id':1, 'resposta':'Sim'}
        return JsonResponse(faltadeagua)

