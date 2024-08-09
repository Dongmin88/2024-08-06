import readtext
import transtest

rt=readtext.read_text()
tt=transtest.Translator()
response = tt.translate(rt.analyze_read('https://arxiv.org/pdf/2408.02960'))
print(tt.get_translated_text(response))

#번역하고 싶은 url 입력하면 한글로 자동으로 번역됨.