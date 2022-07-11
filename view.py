from .models import Cryptocoin
import csv

def ExportCoincsv(request):
	scrapped_coins = Cryptocoin.objects.all()
	response = HttpResponse('text/csv')
	response['Content-Disposition'] = 'attachment; filename=scrappedcoins.csv'
	writer = csv.writer(response)
	writer.writerow(['date_time', 'bitcoin_value', 'etherem_value', 'tether_value', 'binance_value'])
	coins = scrapped_coins.values_list('date_time', 'bitcoin_value', 'etherem_value', 'tether_value', 'binance_value')
	for coin in coins:
		writer.writerow(coin)
	return response
