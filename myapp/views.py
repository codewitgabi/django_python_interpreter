from django.shortcuts import render
import sys


def index(request):
	if request.method == "POST":
		code_snippet = request.POST.get("snippet")
		
		try:
			default_stdout = sys.stdout
			sys.stdout = open("output.txt", "w")
			exec(code_snippet)
			sys.stdout.close()
			sys.stdout = default_stdout
			
			# Get code output data
			with open("output.txt", "r") as f:
				code_result = f.read()
			
		except Exception as e:
			sys.stdout = default_stdout
			code_result = e
			
		context = {
			"code_result": code_result,
			"code_snippet": code_snippet
		}
		
		return render(request, "index.html", context)
		
	context = {
			"code_result": "",
			"code_snippet": ""
		}
		
	return render(request, "index.html", context)