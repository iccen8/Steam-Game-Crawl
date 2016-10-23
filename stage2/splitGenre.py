import csv
with open("tableA.csv", "rb") as source:
	rd = csv.reader(source)
	with open("genre.csv", "wb") as result:
		wr = csv.writer(result)
		for row in rd:
			genreList = row[5].split('/')
			for genre in genreList:
				wr.writerow((row[0], genre))