def search4letters(phrase:str,letters:str='aeiou') -> set:  #为letter赋一个默认值
  """Return a set of letters found in a supplied phrase."""
  return set(letters).intersection(set(phrase))  #取消依赖示例十四的letters变量
