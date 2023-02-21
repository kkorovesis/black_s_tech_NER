import spacy
from spacy.cli import download


def extract_entities(text, lang_code):
  spacy_model_name = f"{lang_code}_core_web_sm"
  try:
    nlp = spacy.load(spacy_model_name)
  except OSError:
    download(spacy_model_name)
    nlp = spacy.load(spacy_model_name)
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
    entity = {"text": ent.text, "type": ent.label_, "start_pos": ent.start_char, "end_pos": ent.end_char}
    entities.append(entity)
  return entities


if __name__ == '__main__':

  # Run some tests
  text = '''US President Joe Biden declared "Kyiv stands strong" as he marked nearly one year of Russia's invasion of Ukraine with a speech in Poland'''
  print(extract_entities(text, 'en'))

  text = '中华人民共和国是一个伟大的国家。'
  print(extract_entities(text, 'zh'))
