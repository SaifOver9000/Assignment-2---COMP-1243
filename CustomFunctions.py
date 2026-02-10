#contains our custom functions

import statistics

def MedianCost(cost):
  """
  Calculates the median cost of a list of costs

  Arguments:
  cost (list)
  """
  medianCost = statistics.median(costs)
  return(f"The median cost per bag is ${medianCost}")

def MinCost(cost):
  """
  Calculates the min cost from a list of costs

  Arguments:
  cost (list)
  """
  minCost = min(cost)
  return(f"The minimum cost per bag is ${minCost}")
def MaxCost(cost):
  """
  Calculates the max cost from a list of costs

  Arguments:
  cost (list)
  """
  maxCost = max(cost)
  return(f"The maximum cost per bag is ${maxCost}")
