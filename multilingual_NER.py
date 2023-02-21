import spacy


def extract_entities(text, lang_code):
  nlp = spacy.load(f"{lang_code}_core_web_sm")
  doc = nlp(text)
  entities = []
  for ent in doc.ents:
    entity = {"text": ent.text, "type": ent.label_, "start_pos": ent.start_char, "end_pos": ent.end_char}
    entities.append(entity)
  return entities


if __name__ == '__main__':
  text = '''US President Joe Biden declared "Kyiv stands strong" as he marked nearly one year of Russia's invasion of Ukraine with a speech in Poland'''
  print(extract_entities(text, 'en'))