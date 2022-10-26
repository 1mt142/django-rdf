from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateContactSerializer



class CreatePDFReportView(APIView):
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        d=datetime.today().strftime('%Y-%m-%d')
        response['Content-Disposition']=f'inline;filename="{d}.pdf"'

        buffer=BytesIO()
        p = canvas.Canvas(buffer,pagesize=A4)

        #Data to print
        data={
          "Posts":[{"title":"Python","views":500},{"title":"JavaScript","views":500}],
          "Videos":[{"title":"Python Programming","likes":500}],
          "Blogs":[{"name":"Report Lab","likes":500,"claps":600}]
        }

        # Start writing pdf
        p.setFont("Helvetica",15,leading=None)
        p.setFillColorRGB(0.29296875,0.453135,0.609375)
        p.drawString(260,800,"My Website")
        p.line(0,788,1000,780)
        p.line(0,778,1000,778)
        x1 = 20
        y1 = 750

        for k,v in data.items():
            p.setFont("Helvetica",15,leading=None)
            p.drawString(x1,y1-12,f"{k}")
            for value in v:
               for key,val in value.items():
                  p.setFont("Helvetica",10,leading=None)
                  p.drawString(x1,y1-20,f"{key}-{val}")
                  y1=y1-60
                  
        p.setTitle(f"Report on {d}")
        p.showPage()
        p.save()

        pdf= buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

class CreateMethodTestView(APIView):
  def post(self,request):
      res=request.data
      print(request.data)
      serializer = (data=request.data)
      serializer.is_valid(raise_exception=True)
       

     



      return Response({"response":res})

