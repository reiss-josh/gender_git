import csvmapper
import json

fields = ("name", "gs_email", "as_pc_chair", "as_pc", "as_session_chair", "as_panelist", "as_keynote_speaker", "as_author", "pc_chairs", "pcs", "session_chairs", "panels", "keynotes", "papers", "gender", "country", "sector")
parser = csvmapper.CSVParser('file.csv', csvmapper.FieldMapper(fields))

converter = csvmapper.JSONConverter(parser)

x = (converter.doConvert(pretty=True))
g = open("outfile.txt", "w+")
g.write(x)
g.close()
