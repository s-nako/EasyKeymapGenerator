class Bidict(dict):
  """ The bidirectional mapping dictionary """
  def __init__(self, init_dict):
    self.inverse = {}
    dict.__init__(self, init_dict)
    for key, value in init_dict.items():
      self.inverse[value] = key
  def __setitem__(self, key, value):
    dict.__setitem__(self, key, value)
    self.inverse.__setitem__(value, key)
