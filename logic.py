import re
from database import data


def get_skill(uskill, eskill):
	s = 0
	for us in uskill.split(','):
		for es in eskill.split(','):
			if re.fullmatch(fr'{us.lower()}', es.lower()) is not None:
				s += 1
	if s >= len(uskill.split(',')):
		return True
	else:
		return False


def get_quali(uquali, equali):
	for uq in uquali.split(','):
		for eq in equali.split(','):
			if eq.lower().find(uq.lower()) != -1:
				return True
	return False


def get_loc(uloc, eloc):
	for ul in uloc.split(','):
		for el in eloc.split(','):
			if el.lower().find(ul.lower()) != -1:
				return True
	return False


def find_avg(temp):
	sum = 0
	for i in temp:
		sum += i
	return round(sum/len(temp), 4)


def average_salary(uskill, uquali, uloc, uminexp, umaxexp):
	avg = []
	for d in data:
		if get_skill(uskill, d['skill']):
			if get_quali(uquali, d['Education']):
				if get_loc(uloc, d['Current Location']):
					if  float(uminexp) <= float(d['ExpValue']) <= float(umaxexp):
						avg.append(d['SalValue'])
	if len(avg) != 0:
		print(avg)
		return f'Average Salary of {len(avg)} employees is {find_avg(avg)}'
	else:
		return 'No such employee found in the record.'
