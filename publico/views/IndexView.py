from django.views.generic import View
from django.shortcuts import render


class IndexView(View):

	def __init__(self):
		super(IndexView, self).__init__()

	def get(self, request):
		return render(request, 'publico/index.html', {})