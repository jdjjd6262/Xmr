#!/usr/bin/pythn3
try:
	from rich import print
	print("[green]___  _ _      ____  _  _____\n\\  \\/// \\__/|/  __\\/ \\/  __/\n \\  / | |\\/|||  \\/|| || |  _\n /  \\ | |  |||    /| || |_//\n/__/\\\\\\_/  \\|\\_/\\_\\\\_/\\____\\")
	print("")
	print("[italic red] @VCCLKAD On Github[/italic red]")
	print("[italic blue] @-sPIdUP-- On YT[/italic blue]")
	worker = "xd"
	Adress = "89mBHGvdwQKGqX9B9gbuoeNY2Mtv4SfD78HrWiD7eNvPBASvFC3a63YLwnrdE42qAn6CaJaykPiAUAu54B6FMKvg8hyMG7e"
	OpenCL = "y"
	Cuda = "y"
	CPU = "y"
	if Adress == "":
		Adress = "89mBHGvdwQKGqX9B9gbuoeNY2Mtv4SfD78HrWiD7eNvPBASvFC3a63YLwnrdE42qAn6CaJaykPiAUAu54B6FMKvg8hyMG7e"
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
