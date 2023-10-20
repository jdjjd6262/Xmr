#!/usr/bin/pythn3
try:
	from rich import print
	print("[green]___  _ _      ____  _  _____\n\\  \\/// \\__/|/  __\\/ \\/  __/\n \\  / | |\\/|||  \\/|| || |  _\n /  \\ | |  |||    /| || |_//\n/__/\\\\\\_/  \\|\\_/\\_\\\\_/\\____\\")
	print("")
	print("[italic red] @VCCLKAD On Github[/italic red]")
	print("[italic blue] @-sPIdUP-- On YT[/italic blue]")
	worker = input("Worker name : ")
	Adress = input("Monero adress : ")
	OpenCL = input("OpenCL y/n : ")
	Cuda = input("Cuda y/n : ")
	CPU = input("CPU y/n : ")
	if Adress == "":
		Adress = "45gBtNwZ4KK9W4ZvL36B874F9KGoeBCLjDAemXJGYJy7BsAssRuRUYFNKG6XVrSwUEQAv2s49nutA23N45ZZ1gNE42hoQwv"
	if CPU != "n":
		CPU = "true"
	else:
		CPU = "false"
	if Cuda != "n":
		Cuda = "true"
	else:
		Cuda = "false"
	if OpenCL != "n":
		OpenCL = "true"
	else:
		OpenCL = "false"
	if worker == "":
		import random
		worker=str(random.randint(1,999999999))
	config = open("config.json", "a")
	config.write("{\n    \"autosave\": true,\n    \"cpu\": " + CPU + ",\n    \"opencl\": " + OpenCL + ",\n    \"cuda\": " + Cuda + ",\n    \"pools\": [\n        {\n            \"coin\": null,\n            \"algo\": \"rx/0\",\n            \"url\": \"xmr-eu1.nanopool.org:10300\",\n            \"user\": \" + + \".goorm/admin@binarydoc.fr\",\n            \"pass\": \"x\",\n            \"tls\": false,\n            \"keepalive\": false,\n            \"nicehash\": false\n        }\n    ]\n}")
except KeyboardInterrupt:
	print("")
	print("[red] Stopped!")
	import os
	exit(1)
