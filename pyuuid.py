

from uuid import NAMESPACE_DNS, uuid4, uuid5


with uuid4() as uuid:
  x = uuid
  
  
print(x)