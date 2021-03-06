from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from django.shortcuts import get_object_or_404, render

from api.views import *

import json
import logging


class HelixBoxView(views.APIView):
    """
    Get SVG source code for a protein's helix box plot
    \n/plot/helixbox/{entry_name}/
    \n{entry_name} is a protein identifier from Uniprot, e.g. adrb2_human
    """
    renderer_classes = (StaticHTMLRenderer,)
    def get(self, request, entry_name=None):
	    if entry_name is not None:
		    p = Protein.objects.get(entry_name=entry_name)
#		    resp =  Response(str(p.get_helical_box()).replace('\n',''))
		    context = {'p':p}
		    resp = render(request,'protein/protein_helixbox.html',context)
		    resp['X-Frame-Options'] = "ALLOWALL"
		    return resp
	# return Response(str(p.get_helical_box()).split('\n'))


class SnakePlotView(views.APIView):
    """
    Get SVG source code for a protein's snake plot
    \n/plot/snake/{entry_name}/
    \n{entry_name} is a protein identifier from Uniprot, e.g. adrb2_human
    """
    renderer_classes = (StaticHTMLRenderer,)
    def get(self, request, entry_name=None):
	    if entry_name is not None:
		    p = Protein.objects.get(entry_name=entry_name)
#		    resp =  Response(str(p.get_snake_plot()).replace('\n',''))
		    context = {'p':p}
		    resp = render(request,'protein/protein_snake_plot.html',context)
		    resp['X-Frame-Options'] = "ALLOWALL"
		    return resp
#            return Response(str(p.get_snake_plot()).split('\n'))
#            return Response(str(p.get_snake_plot()).replace('\n','').replace('\"','\''))
		
#            return Response(str(p.get_snake_plot()).replace('\n',''))
