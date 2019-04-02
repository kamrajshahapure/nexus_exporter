import json
import time
import json

import requests, base64
from requests.auth import HTTPBasicAuth
from http.client import HTTPSConnection
import urllib.request as urllib2
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from urllib.parse import urlparse




class NexusCollector(object):
	def collect(self):
		metric = GaugeMetricFamily('Number_of_repositories','Number_of_repositories2',labels=["Number of repositories"])
		response=requests.get('http://localhost:8081/service/rest/v1/repositories', auth=HTTPBasicAuth('admin', 'admin123'))
		json_data = json.loads(response.text)
		print (len(json_data))
		metric.add_metric("", len(json_data))
		yield metric
		
		metric = GaugeMetricFamily('Number_of_logical_processors','Number_of_logical_processors',labels=["Number_of_logical_processors"])
		response=requests.get('http://localhost:8081/service/rest/atlas/system-information', auth=HTTPBasicAuth('admin', 'admin123'))
		
		json_data = json.loads(response.text)
		metric.add_metric("", json_data['system-runtime']['availableProcessors'])
		yield metric
		
		metric = GaugeMetricFamily('free_Memory','free_Memory',labels=["free_Memory"])
		metric.add_metric("", json_data['system-runtime']['freeMemory'])
		yield metric
		
		metric = GaugeMetricFamily('total_Memory','total_Memory',labels=["total_Memory"])
		metric.add_metric("", json_data['system-runtime']['totalMemory'])
		yield metric
		
		metric = GaugeMetricFamily('max_Memory','max_Memory',labels=["max_Memory"])
		metric.add_metric("", json_data['system-runtime']['maxMemory'])
		yield metric
		
		metric = GaugeMetricFamily('The_1XX_Request_Count','1XX_Request_Count',labels=["1XX_Request_Count"])
		response=requests.get('http://localhost:8081/service/metrics/data', auth=HTTPBasicAuth('admin', 'admin123'))		
		json_data = json.loads(response.text)
		print (json_data)
		metric.add_metric("", json_data['meters']['org.eclipse.jetty.webapp.WebAppContext.1xx-responses']['count'])
		yield metric
		
		metric = GaugeMetricFamily('The_2XX_Request_Count','2XX_Request_Count',labels=["2XX_Request_Count"])
		metric.add_metric("", json_data['meters']['org.eclipse.jetty.webapp.WebAppContext.2xx-responses']['count'])
		yield metric

		metric = GaugeMetricFamily('The_3XX_Request_Count','3XX_Request_Count',labels=["3XX_Request_Count"])
		metric.add_metric("", json_data['meters']['org.eclipse.jetty.webapp.WebAppContext.3xx-responses']['count'])
		yield metric
		
		metric = GaugeMetricFamily('The_4XX_Request_Count','4XX_Request_Count',labels=["4XX_Request_Count"])
		metric.add_metric("", json_data['meters']['org.eclipse.jetty.webapp.WebAppContext.4xx-responses']['count'])
		yield metric
		
		metric = GaugeMetricFamily('The_5XX_Request_Count','5XX_Request_Count',labels=["5XX_Request_Count"])
		metric.add_metric("", json_data['meters']['org.eclipse.jetty.webapp.WebAppContext.5xx-responses']['count'])
		yield metric
		
		

if __name__ == "__main__":
  
  REGISTRY.register(NexusCollector())
  start_http_server(1234)
  while True: time.sleep(1)