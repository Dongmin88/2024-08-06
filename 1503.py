import read_text
import transtest

rt=read_text.read_text()
tt=transtest.Translator()
response = tt.translate(rt.analyze_read())
print(tt.get_translated_text(response))