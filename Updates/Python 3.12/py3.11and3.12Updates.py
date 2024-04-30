
#region 3.11 updates
# Summary. https://www.youtube.com/watch?v=b3_THpKM4EU&ab_channel=ArjanCodes
# Add notes to exceptions
if False:
    try:
        raise TypeError("bad type")
    except TypeError as te:
        te.add_note("Added note here. E.g., \"Type error since u da noob\"")
        raise

# Other changes as well, but I don't really use them.

#endregion 

#region 3.12 Updates
# Better error messages
# Better performance
# Comprehensions are now inline, so faster
# Immortal objects
# Per interpreter GIL?

# F strings are now better
print(f"This is an example {"using double quotes"} inside an f-string")


# PEP 692 – Using TypedDict for more precise **kwargs typing
## https://peps.python.org/pep-0692/

# PEP 698: Override Decorator for Static Typing
from typing import override

class Base:
  def get_color(self) -> str:
    return "blue"

class GoodChild(Base):
  @override  # ok: overrides Base.get_color
  def get_color(self) -> str:
    return "yellow"

class BadChild(Base):
  @override  # type checker error: does not override Base.get_color
  def get_colour(self) -> str:
    return "red"


# PEP 695: Type Parameter Syntax
## Seems nice. Worth looking more into.

#endregion
