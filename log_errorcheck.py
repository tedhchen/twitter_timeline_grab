# Parameters
OUT_FILE = ''
IN_FILE = ''

with open(IN_FILE, 'r') as data:
	with open(OUT_FILE, 'a+', encoding='utf-8') as outfile:
		for x in data:
			if str(x)[12:33] == 'tweet_collector ERROR':
				outfile.write(
					"'" + str(x)[70:-2] + "'" + ', '
				)
