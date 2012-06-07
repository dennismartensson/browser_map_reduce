from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

timesEach = [1] * 1000000
timsTotal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
map_jobs = [(x, timesEach) for x in timsTotal]
reduce_jobs = []
result = None

jobs_out = []

def index(request):

	if map_jobs:
		function_to_run = "map"
		job_content = map_jobs.pop()
		jobs_out.append(1)
		count = job_content[0]
	elif jobs_out and not map_jobs:
		function_to_run = "wait"
		job_content = "0"
		count = "wait"
	elif reduce_jobs and not jobs_out:
		function_to_run = "reduce"
		job_content = reduce_jobs;
		count = job_content
	else:
		return render(request, 'done.html', {"result": result})

	return render(request, 'index.html',{"function_to_run": function_to_run, "job_content":job_content, "count": count})


def reduce(request):
	reduceData = request.GET.get('count', None)

	if reduceData:
		jobs_out.pop()
		reduce_jobs.append(int(float(reduceData)))
	return redirect('index')


def finalize(request):
	finalizeData = request.GET.get('sum', None)

	if finalizeData:
		result = finalizeData
	return render(request, 'done.html', {"result": result})
