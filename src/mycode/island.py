class Field:
  def __init__(self, xpos, ypos, isWater):
    self.xpos = xpos
    self.ypos = ypos
    self.isWater = isWater

  def __str__(self):
    iswater = "W" if self.isWater else "L" 
    return f"{self.xpos}/{self.ypos}/{iswater}"
  
  def isAdjected(self, anotherField):
    if anotherField is None:
      return False

    if not isinstance(anotherField, Field):
      return False

    if anotherField.xpos == self.xpos and anotherField.ypos+1 == self.ypos:
      return True
    
    if anotherField.xpos == self.xpos and anotherField.ypos-1 == self.ypos:
      return True
    
    if anotherField.xpos+1 == self.xpos and anotherField.ypos == self.ypos:
      return True
    
    if anotherField.xpos-1 == self.xpos and anotherField.ypos == self.ypos:
      return True
      
    return False
  
class Map:
  def __init__(self, data:list): 
    x = 0
    self.fields = list()
    for row in data:
      y = 0
      for column in row:
        a_field = Field(x,y,column=='0')
        self.fields.append(a_field)
        y = y + 1
      x = x + 1 

  def __str__(self):
    return f"island data={self.fields}"
  
  def calculate_number_of_islands(self) -> int: 
    print ("removing all water fields")
    candidates = list(filter(lambda field : not field.isWater, self.fields)) 
    
    islandcounter = 0  
    while len(candidates) > 0 :
      candidate = candidates.pop(0)
      print (f"popping next field {candidate} and expanding an island")
      self.expand_land(candidate, candidates) 
      islandcounter = islandcounter + 1

    return islandcounter
  
  def expand_land(self, candidate, candidates):
    print ("getting neighbour fields") 
    neighbours = list(filter(lambda field : field.isAdjected(candidate), candidates)) 

    for neighbour in neighbours:       
      print (f"  adding {neighbour}")      
      if(neighbour in candidates):
        candidates.remove(neighbour)
        self.expand_land(neighbour, candidates)
        
    return None  
 
