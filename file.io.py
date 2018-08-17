def getMenue():
  parsedCSV = []
  menue = []
  with open('./assets/menue.csv', 'r') as rf:
    for line in rf:
      new_line = line.replace('\n', ' ').split(',')
      parsedCSV.append(new_line)

  for dictonary in range(2,len(parsedCSV)):
    menue.append(
    {parsedCSV[1][0] : parsedCSV[dictonary][0], 
    parsedCSV[1][1] : parsedCSV[dictonary][1], 
    parsedCSV[1][2] : parsedCSV[dictonary][2], 
    parsedCSV[1][3] : parsedCSV[dictonary][3], 
    parsedCSV[1][4] : parsedCSV[dictonary][4], 
    parsedCSV[1][5] : parsedCSV[dictonary][5]})
    
  # print(parsedCSV)
  print(menue)
    


getMenue()