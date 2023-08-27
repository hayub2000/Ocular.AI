# from google.colab import drive
# drive.mount('/content/drive')
from happytransformer import HappyGeneration, GENSettings, GENTrainArgs,  GENEvalArgs
import numpy

# import googletrans
from googletrans import Translator
def Ocular_Method(initial_txt):
  
  happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M",  load_path="D:/UNI SEM 8/FYP-II/Backend/text gen/TrainedModels/GPT_NEO_SCARY_DATA075_EPOCH10")
  translator = Translator()
  # initial_txt = "محسوس کر سکتا تھا کہ وہ مجھ پر تیز نگاہ ڈال رہے ہیں، جیسے کھانے کے لئے بے چین شیر ہیں"
  txt = initial_txt

  if(translator.detect(initial_txt).lang!= "en"):
    translated_text = translator.translate(txt, src = "ur", dest = "en").text
    txt = translated_text
      
  # print(txt)

  # lang = translator.detect(translated_text).lang
  # print(lang)


  # print(txt)

  beam_args = GENSettings(no_repeat_ngram_size=2, num_beams=5,  min_length=60, max_length=100)
  greedy_args = GENSettings(no_repeat_ngram_size=2, min_length=60, max_length=100)
  top_kp_sampling_args = GENSettings(do_sample=True, top_k=50, top_p=0.95, temperature=0.7, min_length=60,  max_length=100)

  # print("Setting hogai puri")
  result0 = happy_gen.generate_text(txt, args=top_kp_sampling_args)
  # print("Result generated")
  # print('result is:' + result0)
  print(f"{txt}{result0.text}")
  

  txt = txt + result0.text

  if(translator.detect(initial_txt).lang != "en"):
    translated_text = translator.translate(f"{txt}{result0.text}", src = "en", dest = "ur").text
    txt = translated_text
  print('who are you' + txt)
  # txt=initial_txt
  return txt

# Ocular_Method("ادرینالائن سے میری جیکٹ سے پسینہ نکلنے لگا، حتیٰ کہ منجمد ٹھنڈے میں بھی۔ کرولا میں چڑھنے سے پہلے، میں نے پیچھے کی جانب دیکھا تو ہمارے پیچھے والی شیطانی گاڑی کی جانب جھکیں۔ میں صرف دو افراد کو گاڑی کے سامنے کی سیٹوں میں بیٹھا دیکھ سکا۔ میں کوئی خصوصی نشانیاں نہیں دیکھ سکا تھا، مگر میں ان کے نظروں میں محسوس کر سکتا تھا کہ وہ مجھ پر تیز نگاہ ڈال رہے ہیں، جیسے کھانے کے لئے بے چین شیر ہیں۔")
# py -c "from gpt_neo import Ocular_Method; Ocular_Method('ادرینالائن سے میری جیکٹ سے پسینہ نکلنے لگا، حتیٰ کہ منجمد ٹھنڈے میں بھی۔ کرولا میں چڑھنے سے پہلے، میں نے پیچھے کی جانب دیکھا تو ہمارے پیچھے والی شیطانی گاڑی کی جانب جھکیں۔ میں صرف دو افراد کو گاڑی کے سامنے کی سیٹوں میں بیٹھا دیکھ سکا۔ میں کوئی خصوصی نشانیاں نہیں دیکھ سکا تھا، مگر میں ان کے نظروں میں محسوس کر سکتا تھا کہ وہ مجھ پر تیز نگاہ ڈال رہے ہیں، جیسے کھانے کے لئے بے چین شیر ہیں۔')"