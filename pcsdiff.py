import sys
filenames = sys.argv[1:]
if len(filenames) != 2:
  print 'usage: python pcsdiff.py file1 file2'
  quit()

print filenames
data = []
for name in filenames:
  f = open(name, "r")
  data.append([line.split() for line in f])
  f.close()

for f in data:
  for l in f:
    for i, item in enumerate(l):
      if item.isdigit():
        ival = int(item)
        l[i] = ival 
      else:
        try:
          xval = float(item)
          l[i] = xval
        except:
          pass

data = zip(data[0], data[1])

relative = (0,0,0.,0.)
absolute = (0,0,0.,0.)
tag = "tag"
atag = tag
rtag = tag
for i, pair in enumerate(data):
  if type(pair[0][0]) == str:
    tag = " ".join([str(v) for v in pair[0]])
  if pair[0] != pair[1]:
    z = zip(pair[0], pair[1])
    for j, values in enumerate(z):
      if values[0] != values[1]:
        assert(type(values[0]) == float)
        x = abs(values[0] - values[1])
        y = x/(abs(values[0]) + abs(values[1]))
        if (x > absolute[3]):
          absolute = (i+1, j, values[0], x)
          atag = tag
        if (y > relative[3]):
          relative = (i+1, j, values[0], y)
          rtag = tag

if relative[3] > 0.:
    print "%d %d %.12g   diff %g relative : " % relative, rtag
    print "%d %d %.12g   diff %g absolute : " % absolute, atag
else:
    print 'files identical'
