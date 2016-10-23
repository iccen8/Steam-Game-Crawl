import csv
with open("tableBfromStage1.csv", "rb") as source:
	rd = csv.reader(source)
	with open("tableB.csv", "wb") as result:
		wr = csv.writer(result)
		for row in rd:
			wr.writerow((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))