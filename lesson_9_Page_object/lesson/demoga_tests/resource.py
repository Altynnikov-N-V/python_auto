from pathlib import Path

def image_path(file_name):
  return  str((Path(__file__).resolve().parents[1] / 'demoga_tests' / file_name).absolute())